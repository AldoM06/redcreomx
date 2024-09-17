#
from django.urls import path
from . import views
from applications.users.views import LoginUser


app_name = "home_app"

urlpatterns = [
    path(
        '',
        views.IndexView.as_view(),
        name='index-home',
        ),
    path(
        'home/about',
        views.AboutView.as_view(),
        name='index-about',
        ),
        
]
