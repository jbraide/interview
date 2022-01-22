from django.urls import path
from . import views 

urlpatterns = [
    path('', views.CreateShortURLView.as_view()), 
    path('<str:short_url>/', views.GetLongURLView.as_view())
]