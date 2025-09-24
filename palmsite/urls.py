from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views
from main.admin import custom_admin_site

urlpatterns = [
    path("", views.home, name="home"),  # الصفحة الرئيسية
    path("admin/", custom_admin_site.urls),
    path("", include("main.urls")),  # روابط التطبيق
    path("i18n/", include("django.conf.urls.i18n")),  # دعم تعدد اللغات
]

# في وضع التطوير فقط
if settings.DEBUG:
    # عرض الملفات الإعلامية (media)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # عرض الملفات الثابتة (static)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
