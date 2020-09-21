from django.urls import path
from . import views

# Template tagging
app_name = "user"

urlpatterns = [
    path("register/", views.register, name = "register"),
    path("login/", views.login, name="login"),

]