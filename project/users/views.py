from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.shortcuts import render
from django.template import RequestContext

from .models import CustomUser



class CreateView(LoginRequiredMixin, generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('list')
    template_name = 'user_create.html'
    login_url = 'login'

class ChangeView(LoginRequiredMixin, generic.UpdateView):
    login_url = 'login'
    def settings(request):
        if request.method == 'POST':
            postdata = request.POST.copy()
            form = CustomUserChangeForm(postdata)
            if form.is_valid():
                form.save()
        else:
            form = CustomUserChangeForm()
        return render(form)

class UsersListView(LoginRequiredMixin, TemplateView):
    template_name = 'users.html'
    login_url = 'login'
    def get_context_data(self,**kwargs):
        context = super(UsersListView,self).get_context_data(**kwargs)
        context['object_list'] = CustomUser.objects.all()
        return context

