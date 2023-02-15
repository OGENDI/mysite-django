from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='name'),
    path('v1/', views.v1, name='view q'),
]