from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('neworphan/', views.OrphanCreateView.as_view(), name='create_orphan'),
    path('<int:pk>/delete/', views.DeleteOrphanView.as_view(), name='delete_orphan'),
    path('relative/', views.RelativeView.as_view(), name='relative'),
    path('search/', views.search, name="search"),
]
