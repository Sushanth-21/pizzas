from django.urls import path
from .views import create_regular, create_square, filterBySize, filterByType, register, login, logout, all, update

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('logout/', logout),
    path('square/', create_square),
    path('regular/', create_regular),
    path('all/', all),
    path('update/<int:pk>/', update),
    path('filterByType/<str:pk>/', filterByType),
    path('filterBySize/<str:pk>/', filterBySize),

]
