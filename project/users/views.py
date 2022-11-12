from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponseRedirect




class CreateView(LoginRequiredMixin, generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('list')
    template_name = 'user_create.html'
    login_url = 'login'

def ChangeView(request):
    password_form = PasswordChangeForm(request.user)
    user_form = UserChangeForm(instance=request.user)

    if request.method == 'POST':
        if request.GET.get('type', 'password'):
            password_form = PasswordChangeForm(request.user, request.POST)
            if not password_form.is_valid():
                return HttpResponseRedirect('%s' % (request.path))
        if request.GET.get('type', 'details'):
            user_form = PasswordChangeForm(request.POST, instance=request.user)
            if not user_form.is_valid():
                return HttpResponseRedirect('%s' % (request.path))

    context = {
        'password_form': password_form,
        'user_form': user_form
    }
    return render(request, 'edit_user.html', context)

class UsersListView(LoginRequiredMixin, TemplateView):
    template_name = 'users.html'
    login_url = 'login'
    def get_context_data(self,**kwargs):
        context = super(UsersListView,self).get_context_data(**kwargs)
        context['object_list'] = User.objects.all()
        return context

