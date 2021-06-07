
from django.urls import path
from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import *

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('login', LogIn.as_view(), name="login"),
    path('registration', Registraion.as_view(), name="registration"),
    path('add_new_user', login_required(AddUser.as_view()), name="add_new_user"),
    path('update-user/<int:id>', login_required(UpdateUser.as_view()), name="update_user"),
    path('delete-user/<int:id>', login_required(delete_User), name="delete_user"),

    ]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)