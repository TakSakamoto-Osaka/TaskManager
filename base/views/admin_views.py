from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..mixins import AdminRequiredMixin
from ..models.site_user import SiteUser


class UserCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    template_name = 'pages/user_create.html'
    model = SiteUser
    fields = ('username', 'password', 'first_name', 'last_name', 'email', 'department')

