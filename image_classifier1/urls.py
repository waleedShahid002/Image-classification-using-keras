
from django.urls import path
from classifier.views import upload_image
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('predict/',upload_image , name='predict_image'),
    path('api/index', upload_image, name='predict_image'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

