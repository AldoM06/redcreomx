from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
#ßfrom applications.users.mixins import AdminPermisoMixin
from django.views.generic import (
    View,
    TemplateView,

)

from django.views.generic.edit import (
    FormView,

)

from .forms import (
    LoginForm,
    UserRegisterForm,


)
from .models import User

# Create your views here.
class UserRegisterView(FormView):
    template_name = 'user/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('user_app:user-panel')

    def form_valid(self, form):
        #
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            Name=form.cleaned_data['Name'],
            LastName=form.cleaned_data['LastName'],
            MiddleName=form.cleaned_data['MiddleName'],
            Curp=form.cleaned_data['Curp'],
        )
        # enviar el codigo al email del user
        return super(UserRegisterView, self).form_valid(form)

class LoginUser(FormView):
    template_name = 'home/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('user_app:user-panel')

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)

class LogoutView(View):

    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'home_app:index-home'
            )
        )


class PanelView(TemplateView):
    template_name = "user/panel.html"

class LogoutView(View):

    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'home_app:index-home'
            )
        )
