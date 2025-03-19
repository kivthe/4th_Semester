from django.urls import path
from . import views

urlpatterns = [
  #path('load/',views.load,name='load'),
  path('',views.main,name='main'),
  path('refresh/',views.refresh,name='refresh'),
  path('query/',views.query,name='query')
]