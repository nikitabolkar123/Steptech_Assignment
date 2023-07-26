from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('users/', views.users_details, name='users'),
    path('new_user/', views.new_user, name='new_user'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
]
