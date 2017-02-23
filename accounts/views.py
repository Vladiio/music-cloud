from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from registration.backends.simple.views import RegistrationView
from .models import UserProfile

class MyRegistrationView(RegistrationView):

    def get_success_url(self, user):
        return reverse('user_profile', kwargs={'username': user.username})




class UserProfileView(generic.View):
    template_name = 'registration/profile.html'

    def get(self, request, username):
        username = username
        user = get_object_or_404(User, username=username)
        user_profile = UserProfile.objects.get_or_create(user=user)[0]
        return render(request, self.template_name, {'selected_user': user,
                                                    'user_profile': user_profile})



