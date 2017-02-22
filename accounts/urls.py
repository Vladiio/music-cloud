from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^register/$',
        views.MyRegistrationView.as_view(),
        name='registration_register'),

    url(r'^profile/$',
        views.UserProfileView.as_view(),
        name='user_profile'),

    url(r'^', include('registration.backends.simple.urls')),

]