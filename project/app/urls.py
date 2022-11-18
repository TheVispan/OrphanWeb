from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('create/', views.OrphanCreateView.as_view(), name='create_orphan'),
    path('<int:pk>/change/', views.OrphanChangeView.as_view(), name='change_orphan'),
    path('delete/', views.delete),
    path('search/', views.search, name="search"),
    #path('deduct/<int:pk>/', views.deduct)
]
