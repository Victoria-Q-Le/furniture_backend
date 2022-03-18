#map request URLs to the views created in views.py
from django.urls import path
from . import views


urlpatterns = [
    path('api/users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/users/register', views.registerUser, name = 'register'), ###this route will use in the post request of the frontend to register new User
    path('api/users/profile', views.getUserProfile, name = 'user_profile'),
    path('api/furnitures', views.FurnitureList.as_view(), name = 'furniture_list'),
    path('api/furnitures/<int:pk>', views.FurnitureDetail.as_view(), name = 'furniture_detail'),
]
