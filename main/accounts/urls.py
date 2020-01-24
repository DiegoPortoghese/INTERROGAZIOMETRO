from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
        path('<int:pk>/', views.DetailProfileView.as_view()),
        path('force/',views.CleateProfileView.as_view()),
        
        path('preferenze/', views.ListProfilePreferenzeMateriaView.as_view()),
        path('preferenze/<int:pk>/', views.DetailProfilePreferenzeMateriaView.as_view()),
        
        path('interrogazione/', views.ListProfileInterrogazioneView.as_view()),
        path('interrogazione/<int:pk>/', views.DetailProfileInterrogazioneView.as_view()),

    ]