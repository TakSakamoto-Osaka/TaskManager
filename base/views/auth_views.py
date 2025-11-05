from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm


class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'pages/login.html'


class AuthLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'top/login.html'

