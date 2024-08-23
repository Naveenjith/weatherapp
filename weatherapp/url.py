from django.urls import include, path

from weatherapp import views

urlpatterns = [
    path('',views.home)
]
