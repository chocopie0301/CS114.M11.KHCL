# mask_detection/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mask_detector.urls'))
] + static('/runs/', document_root=settings.BASE_DIR / 'runs')