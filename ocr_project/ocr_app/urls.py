from django.urls import path
from . import views

app_name = 'ocr_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('upload_image/', views.upload_image, name='upload_image'),
]
