from django.urls import path, re_path
from chatnote import views

app_name = 'chatnote'
urlpatterns = [
    re_path(r'^$', views.main),
]