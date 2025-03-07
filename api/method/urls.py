from django.urls import path
from .views import UserList, UserRegister

urlpatterns = [
    path('user/', UserList.as_view(), name='userlist'),
    path('user/register/', UserRegister.as_view(), name='userregister'),
]