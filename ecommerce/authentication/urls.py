from django.contrib.auth import views as auth_view
from django.urls import path
from . import views

app_name = 'authenticate'

urlpatterns = [
    path('login/',auth_view.LoginView.as_view(template_name='authentication/login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(),name='logout'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('detail/<int:pk>/',views.CustomUserDetail.as_view(),name='user_detail'),
    path('update/<int:pk>/',views.CustomUserUpdate.as_view(),name='user_update'),
]
