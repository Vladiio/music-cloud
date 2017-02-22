from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from registration.backends.simple.views import RegistrationView
from .models import UserProfile

class MyRegistrationView(RegistrationView):

    def get_success_url(self, user):
        return 'profile'


class UserProfileView(generic.View):
    template_name = 'registration/profile.html'

    def get(self, request):
        username = request.user.username
        user = get_object_or_404(User, username=username)
        user_profile = UserProfile.objects.get_or_create(user=user)
        return render(request, self.template_name, {'selected_user': user,
                                                    'user_profile': user_profile})
