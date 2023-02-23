from django.urls import path
from user import views


urlpatterns = [
    path('', views.index, name="user_index"),
    path('login/', views.Login_form, name='login'),
    path('logout/', views.Log_Out, name='logout'),
    path('signup/',views.Sign_Up, name = 'signup'),
]