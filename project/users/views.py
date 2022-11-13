from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView


class CreateUserView(LoginRequiredMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'create_user.html'
    success_url = reverse_lazy('list')

class ChangeUserView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'change_user.html'
    success_url = reverse_lazy('list')


class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    model = User
    form_class = AdminPasswordChangeForm
    template_name = 'change_password.html'
    success_url = reverse_lazy('list')
    def get_form_kwargs(self):
        kwargs = super(ChangePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'delete_user.html'
    success_url = reverse_lazy('list')

class UsersListView(LoginRequiredMixin, TemplateView):
    template_name = 'users.html'
    login_url = 'login'
    def get_context_data(self,**kwargs):
        context = super(UsersListView, self).get_context_data(**kwargs)
        context['object_list'] = User.objects.filter(is_superuser__icontains='0')
        return context

