from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateView.as_view(), name='create'),
    path('change/', views.UsersListView.as_view(), name='edit_user'),
    path('list/', views.UsersListView.as_view(), name='list'),
]