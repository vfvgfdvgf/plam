from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Product, Service, BlogPost, GalleryImage

# ---------------------------
# الصفحات الثابتة
# ---------------------------
class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['home', 'services', 'products', 'blog', 'gallery', 'contact']

    def location(self, item):
        return reverse(item)


# ---------------------------
# المنتجات
# ---------------------------
class ProductSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('product_detail', args=[obj.id])


# ---------------------------
# الخدمات
# ---------------------------
class ServiceSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Service.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('service_detail', args=[obj.id])


# ---------------------------
# مقالات المدونة
# ---------------------------
class BlogPostSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.7

    def items(self):
        return BlogPost.objects.all()

    def lastmod(self, obj):
        return obj.publish_date

    def location(self, obj):
        return reverse('blog_detail', args=[obj.id])


# ---------------------------
# معرض الأعمال: صور المنتجات والخدمات والمقالات
# ---------------------------
class GallerySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        gallery_items = []
        for p in Product.objects.all():
            gallery_items.append({'type': 'product', 'id': p.id})
        for s in Service.objects.all():
            gallery_items.append({'type': 'service', 'id': s.id})
        for b in BlogPost.objects.all():
            gallery_items.append({'type': 'blog', 'id': b.id})
        for g in GalleryImage.objects.all():
            # إذا كان مضاف يدوياً أو من أي نوع، نضيفه حسب id
            gallery_items.append({'type': 'gallery', 'id': g.id})
        return gallery_items

    def location(self, obj):
        if obj['type'] == 'product':
            return reverse('product_detail', args=[obj['id']])
        elif obj['type'] == 'service':
            return reverse('service_detail', args=[obj['id']])
        elif obj['type'] == 'blog':
            return reverse('blog_detail', args=[obj['id']])
        else:  # gallery
            return reverse('gallery_detail', args=[obj['id']])
