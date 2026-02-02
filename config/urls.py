from django.contrib import admin
from django.urls import path, include
from animals.views import pet_list
from django.conf import settings
from django.conf.urls.static import static
from animals.views import register, pet_list, pet_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('register/', register, name='register'),
    path('pet/<int:pk>/', pet_detail, name='pet_detail'),
    path('', pet_list, name='pet_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

