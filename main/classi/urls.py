from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

#rooms_router = DefaultRouter()
#rooms_router.register(r'rooms', views.RoomViewSet)

urlpatterns = [
    #path("",include(rooms_router.urls)), # ROOM default CRUD
    path('upload/', views.ClasseImageView.as_view()),
    path('upload/<int:pk>/', views.DetailClasseImageView.as_view()),
    path('', views.ListClasseView.as_view()),
    path('<int:pk>/', views.DetailClasseView.as_view()),
    path('search/', views.SearchListClasseView.as_view()),
    
    path('oramateria/', views.ClasseOraMateriaView.as_view()),
    path('oramateria/<int:pk>/', views.DetailClasseOraMateriaView.as_view()),

    path('turnointerrogazione/', views.ListClasseTurnoInterrogazioneView.as_view()),
    path('turnointerrogazione/<int:pk>/', views.DetailClasseTurnoInterrogazioneView.as_view()),
    path('previsione/',views.my_view),

    path('my/', views.UserListClasseView.as_view()),
]