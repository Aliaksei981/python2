from django.contrib import admin
from django.urls import path, include
from books_shop import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("shop/", include("sales_manager.urls")),
    path("accounts/", include("sales_manager.urls")),
    path("hotel/", include("hotel.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
