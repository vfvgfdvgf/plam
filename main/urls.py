from django.contrib import admin
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from . import views
from .sitemaps import StaticViewSitemap, ProductSitemap, ServiceSitemap, BlogPostSitemap, GallerySitemap
from django.shortcuts import redirect
from django.conf import settings
# ---------------------------
# تعريف الـ sitemaps
# ---------------------------
sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductSitemap,
    'services': ServiceSitemap,
    'blog': BlogPostSitemap,
    'gallery': GallerySitemap,
}

# ---------------------------
# مسارات الموقع
# ---------------------------
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name='home'),
    path('services/', views.services_view, name='services'),
    path('service/<int:pk>/', views.service_detail, name='service_detail'),
    
    path('products/', views.products_view, name='products'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    
    path('blog/', views.blog_view, name='blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact_view, name='contact'),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django-sitemap'),
]
# معالجة أي رابط غير موجود
def redirect_to_home(request, exception=None):
    return redirect('home')  # نفترض عندك صفحة رئيسية باسم home

handler404 = redirect_to_home
