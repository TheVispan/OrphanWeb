from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

#Создание имени пользователя
class CreateUserView(LoginRequiredMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/create_user.html'
    success_url = reverse_lazy('list')


#Изменение имени пользователя
class ChangeUserView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'users/change_user.html'
    success_url = reverse_lazy('list')
#Изменение пароля пользователя
def UpdatePassword(request, pk):
    user1 = User.objects.get(id=pk)
    form = AdminPasswordChangeForm(user=user1)
    if request.method == 'POST':
        form = AdminPasswordChangeForm(user=user1, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse_lazy('list'))
    return render(request, 'users/change_password.html', {
        'form': form,
    })
#Удаление пользователя
class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'users/delete_user.html'
    success_url = reverse_lazy('list')
#Показывает пользователей в таблице
class UsersListView(LoginRequiredMixin, TemplateView):
    template_name = 'users/users.html'
    login_url = 'login'
    def get_context_data(self,**kwargs):
        context = super(UsersListView, self).get_context_data(**kwargs)
        context['object_list'] = User.objects.filter(is_superuser__icontains='0')
        return context

