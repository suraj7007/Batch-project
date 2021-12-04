from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path('login/', loginuser, name='login'),
    path('logout/', logoutuser, name='logout'),
    path('signup/', signupuser, name='signup'),

]
