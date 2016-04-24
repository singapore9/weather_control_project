from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from weather_control_app import models


def index(request):
    return render(request, 'weather_control_app/index.html', {})


def home(request):
    msg = models.home(request)
    return render(request, 'weather_control_app/home.html', msg)


class SignUpFormView(FormView):
    form_class = UserCreationForm

    template_name = 'weather_control_app/signup.html'

    success_url = '/login/'

    def form_valid(self, form):
        form.save()

        return super(SignUpFormView, self).form_valid(form)


# def login_or_logout(request):
#     if request.user.is_authenticated():
#         return LogoutFormView.as_view()(request)
#     else:
#         return LoginFormView.as_view()(request)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = 'weather_control_app/login.html'

    success_url = '/home/'

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutFormView(FormView):
    def get(self, request):
        logout(request)

        return HttpResponseRedirect('/')