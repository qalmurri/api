from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.get, name='get'),
    path('post/', views.post, name='post'),
    path('put/', views.put, name='put'),
    path('delete/', views.delete, name='delete'),
]