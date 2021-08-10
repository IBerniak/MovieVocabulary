from django.urls import path
from . import views

urlpatterns = [
    path('', views.searching, name='searching'),
    path('search/<str:pk>', views.search_response, name='search_response'),
]
