from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from passwords.models import StoredPassword


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(
        label="Username",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )


class UpdatePasswordForm(forms.ModelForm):
    class Meta:
        model = StoredPassword
        fields = ['category', 'username', 'password', 'application_name', 'description']

        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'placeholder': 'Category'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'application_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Application Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description (Optional)', 'rows': 2}),
        }

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        application_name = cleaned_data.get('application_name')
        description = cleaned_data.get('description')

        if category == 'Social Media' and not application_name:
            raise ValidationError({'platform_name': 'Platform name is required for Social Media.'})

        if category == 'Banking' and not application_name:
            raise ValidationError({'platform_name': 'Platform name (e.g., Bank Name) is required for Banking.'})

        if category == 'Work' and not application_name:
            raise ValidationError({'platform_name': 'Platform name (e.g., Company Name) is required for Work.'})

        if category == 'Other' and not description:
            raise ValidationError({'description': 'Description is required for Other categories.'})

