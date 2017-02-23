from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^register/$',
        views.MyRegistrationView.as_view(),
        name='registration_register'),

    url(r'^profile/(?P<username>[\w]+)/$',
        views.UserProfileView.as_view(),
        name='user_profile'),

    url(r'^update_profile/(?P<pk>[\d]+)/$',
        views.UpdateUserProfile.as_view(),
        name='update-user-profile'),

    url(r'^', include('registration.backends.simple.urls')),

]