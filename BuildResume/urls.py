from django.urls import path
from . import views
# Giving paths to the different web pages available in our Django project
urlpatterns= [
    path("resume/",views.resume),
    path("login/",views.login),
    path("",views.login),
    path("signup/",views.signup),
    path("design/",views.design),
    path("details/",views.details)
]
