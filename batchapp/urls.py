from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path('login/', loginuser, name='login'),
    path('logout/', logoutuser, name='logout'),
    path('signup/', signupuser, name='signup'),
    path("create_batch/", create_batch, name="create_batch"),
    path("batch_detail/<int:id>/", batch_detail, name="batch_detail"),
    path("delete_batch/<int:id>/", delete_batch, name="delete_batch"),

]
