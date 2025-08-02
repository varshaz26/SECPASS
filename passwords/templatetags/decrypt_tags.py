from django import template
from passwords.encrypt import decrypt_password

register = template.Library()

@register.filter
def decrypt_template_tag(value):
    return decrypt_password(value)

