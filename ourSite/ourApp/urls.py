from django.urls import path
from . import views
urlpatterns = [
    path("",views.ViewNews.as_view(),)
]