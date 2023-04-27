from django.urls import path
from . import views

# define the urls that will be used under the members/ domain
urlpatterns = [
    path('login_user', views.login_user, name="login"),
]