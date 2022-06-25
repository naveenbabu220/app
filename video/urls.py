from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= "index"),
    path('serializer/', views.Listview.as_view())
]