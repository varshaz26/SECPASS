from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class StoredPassword(models.Model):
    CATEGORY_CHOICES = [
        ('Social Media', 'Social Media'),
        ('Banking', 'Banking'),
        ('Work', 'Work'),
        ('Other', 'Other'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=500)
    application_name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stored_passwords")

    def __str__(self):
        return f"{self.application_name} ({self.username})"
    

    




