from django.urls import re_path

from main import views

urlpatterns = [
    re_path(r'^$', views.main),
]