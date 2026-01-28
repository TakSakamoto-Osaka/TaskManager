from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm


class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'pages/login.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['label_suffix'] = ''  # ここでサフィックスを空にする
        return kwargs

class AuthLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'top/login.html'

