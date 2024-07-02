from django.urls import path
from . import views

urlpatterns = [
    path('', views.getUsers),
    path('signup/', views.signup),
    path('login/', views.login),
    path('dining-place/', views.display),
    path('dining-place/create/', views.create),
    path('dining-place/<str:name>/', views.search),
    path('dining-place/availability/', views.availability),
    path('dining-place/book/', views.book),
]
