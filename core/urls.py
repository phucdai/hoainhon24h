from django.urls import path, include
from .views import *

app_name = 'core'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('baiviet/<slug:slug>', View.as_view(), name='post-detail'),
    path('danhmuc/<slug:slug>', Categories.as_view(), name='category')
]
