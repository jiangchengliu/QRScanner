from allauth.account.adapter import DefaultAccountAdapter
from .models import User

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)
        if sociallogin.account.provider == 'google':
            extra_data = sociallogin.account.extra_data
            existing_user = User.objects.filter(email=extra_data['email']).first()
            if not existing_user:
                user.first_name = extra_data['given_name']
                user.last_name = extra_data['family_name']
                user.email = extra_data['email']
                user.save()
        return user