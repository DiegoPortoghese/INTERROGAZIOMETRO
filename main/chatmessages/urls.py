from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

#rooms_router = DefaultRouter()
#rooms_router.register(r'rooms', views.RoomViewSet)

urlpatterns = [
    #path("",include(rooms_router.urls)), # ROOM default CRUD
    path('', views.ListChatMessageView.as_view()),
    path('<int:pk>/', views.DetailChatMessageView.as_view()),
    path('chatgroup/<int:group_id>/', views.ListGroupChatMessageView.as_view()),
    path('chatgroup/limit/<int:group_id>/', views.ListGroupLimitChatMessageView.as_view()),
]
