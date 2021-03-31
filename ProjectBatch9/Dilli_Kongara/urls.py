from django.urls import path
from Dilli_Kongara import views
urlpatterns = [
path('',views.home),
path('ProjectDemo/',views.chk),
path('home/',views.homepage),
path('lg/',views.lgn),
path('rg/',views.reg),
]