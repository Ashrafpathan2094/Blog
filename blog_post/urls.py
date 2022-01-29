
from django.urls import path

from . import views


urlpatterns = [

    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('post/<str:pk>',views.post,name='post'),
    path('user_profile/',views.user_profile,name='user_profile'),
    
]
