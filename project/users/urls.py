from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('<int:pk>/change/', views.ChangeUserView.as_view(), name='edit_user'),
    path('<int:pk>/password/', views.ChangePasswordView.as_view()),
    path('<int:pk>/delete/', views.DeleteUserView.as_view(), name='delete_user'),
    path('list/', views.UsersListView.as_view(), name='list'),
]