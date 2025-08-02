from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.http import HttpResponseRedirect
from .forms import RegistrationForm, LoginForm, UpdatePasswordForm
from .models import StoredPassword
from django.contrib.auth.base_user import BaseUserManager
from passwords.encrypt import encrypt_password, decrypt_password

def index(request):
    return render(request, 'index.html')

def home_page(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % ('/', request.path))
    return render(request, 'home.html')

class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'index.html'


def user_login_view(request):
    if request.user.is_authenticated:
        return redirect('/home')
    return UserLoginView.as_view()(request)


def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please log in.")
        else:
            messages.error(request, "Registration failed.")
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def add_new_password(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % ('/', request.path))
    
    if request.method == 'POST':
        try:
            category = request.POST['category']
            username = request.POST['username']
            password = encrypt_password(request.POST['password'])
            application_name = request.POST['application_name']
            description = request.POST.get('description', '')

            StoredPassword.objects.create(
                category=category,
                username=username,
                password=password,
                application_name=application_name,
                description=description,
                user=request.user
            )
            messages.success(request, f"New password added for {application_name}")
            return HttpResponseRedirect("/add_password")
        except Exception as e:
            messages.error(request, f"Error: {e}")
            print("Error details:", e)
    
    return render(request, 'add_password.html')


def edit_password(request, pk):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % ('/', request.path))

    password_entry = StoredPassword.objects.get(id=pk)
    password_entry.password = decrypt_password(password_entry.password)
    form = UpdatePasswordForm(instance=password_entry)

    if request.method == 'POST':
        if 'delete' in request.POST:
            password_entry.delete()
            return redirect('/manage_passwords')
        form = UpdatePasswordForm(request.POST, instance=password_entry)
        if form.is_valid():
            try:
                password_entry.password = encrypt_password(password_entry.password)
                form.save()
                messages.success(request, "Password Updated Successfully.")
                password_entry.password = decrypt_password(password_entry.password)
                return HttpResponseRedirect(request.path)
            except ValidationError as e:
                form.add_error(None, e)

    return render(request, 'edit_password.html', {'form': form})


def search(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % ('/', request.path))
    
    user_passwords = StoredPassword.objects.filter(user=request.user)

    if request.method == "POST":
        search_query = request.POST.get("password_search", "")
        search_results = user_passwords.filter(
            Q(application_name__icontains=search_query) | Q(category__icontains=search_query) | Q(description__icontains=search_query) | Q(username__icontains=search_query)
        )

        if search_results.exists():
            return render(request, "search.html", {'passwords': search_results})
        else:
            messages.error(request, "No matching passwords found.")

    return render(request, "search.html", {'pws': user_passwords,})


def manage_passwords(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % ('/', request.path))
    user_passwords = StoredPassword.objects.filter(user=request.user)
    if not user_passwords:
        return render(request, 'manage_passwords.html',
                      {'no_password': "No password available. Please add password."})
    return render(request, 'manage_passwords.html', {'all_passwords': user_passwords})


