from main.admin import custom_admin_site
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from main import views
from django.shortcuts import redirect

urlpatterns = [
    path('', views.home, name='home'),  # الصفحة الرئيسية
    path('admin/', custom_admin_site.urls),
    path('', include('main.urls')),  # توجيه كل الطلبات لتطبيق main
    path('i18n/', include('django.conf.urls.i18n')),  # دعم تغيير اللغة
]

# السماح بعرض الملفات الإعلامية أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# التقاط أي رابط غير معروف وإعادة توجيهه للصفحة الرئيسية
urlpatterns += [
    re_path(r'^.*$', lambda request: redirect('home')),
]
