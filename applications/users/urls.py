#
from django.urls import path
from . import views

app_name = "user_app"

urlpatterns = [
    path(
        'user/register/',
        views.UserRegisterView.as_view(),
        name='user-register',
    ),
    path(
        'user/login/',
        views.LoginUser.as_view(),
        name='user-login',
        ),
    path(
        'user/login/',
        views.LogoutView.as_view(),
        name='user-logout',
        ),
    path(
        'user/panel/',
        views.PanelView.as_view(),
        name='user-panel',
        ),


]
