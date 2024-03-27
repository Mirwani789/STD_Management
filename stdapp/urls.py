from django.urls import path
from .views import *
urlpatterns = [
    path("",Home),
    path("home/",Home),
    path('add-std/',std_add),

]