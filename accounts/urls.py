from django.urls import path
from .views import RegisterAPIView,UserListCreateView,UserRetrieveUpdateDeleteView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('users/',UserListCreateView.as_view(),name='user-list-create'),
    path('users/<int:pk>',UserRetrieveUpdateDeleteView.as_view(),name='user-detail'),
]
