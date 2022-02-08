from . import views
from django.urls import path

app_name = 'pure_html'

urlpatterns = [
    path('', views.index, name="index"),
    path('interval', views.interval, name="interval"),
    path('button', views.button, name = "button"),
    path('button2', views.button2, name = "button2")

]