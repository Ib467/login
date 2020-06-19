from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("registration", views.regUpdate), #home page registration or login
    path("login",views.loginProcess), #login page
    path("logout", views.loggingOut), 
    path('Add-a-book-review', views.addingBook)
]