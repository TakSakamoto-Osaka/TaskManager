from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import Staff


class JoinningContactCreateView(LoginRequiredMixin, CreateView):
    model = Staff
    template_name = "pages/joinning_contact_create.html"
    fields = "__all__" 
     