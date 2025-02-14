from django.urls import path
from . views import predict_image, upload_image

urlpatterns = [
     path('predict/', predict_image, name='predict_image'),
    path('index/', upload_image, name='upload_image'),
 ]

