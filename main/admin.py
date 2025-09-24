from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from .models import Category, Service, Product, BlogCategory, BlogPost, GalleryImage


# ---------------------------
# تسجيل الموديلات في admin العادي
# ---------------------------

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'is_featured', 'is_best_seller')
    list_filter = ('category', 'is_featured', 'is_best_seller')
    search_fields = ('name', 'description')
    ordering = ('name',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', 'description')


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'source_type', 'created_at')
    list_filter = ('source_type', 'created_at')
    search_fields = ('title',)


# ---------------------------
# إنشاء لوحة تحكم مخصصة
# ---------------------------

class CustomAdminSite(admin.AdminSite):
    site_header = "لوحة إدارة مؤسسة النخيل والشبوك"
    site_title = "لوحة الإدارة"
    index_title = "الصفحة الرئيسية"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("dashboard/", self.admin_view(self.dashboard), name="dashboard"),
        ]
        return custom_urls + urls

    def dashboard(self, request):
        context = dict(
            self.each_context(request),
            total_products=Product.objects.count(),
            total_services=Service.objects.count(),
            total_blogs=BlogPost.objects.count(),
            latest_products=Product.objects.order_by("-created_at")[:5],
            latest_services=Service.objects.order_by("-created_at")[:5],
            latest_blogs=BlogPost.objects.order_by("-created_at")[:5],  # <-- صححت هنا
        )
        return TemplateResponse(request, "admin/dashboard.html", context)


# نسجل الأدمين الجديد
custom_admin_site = CustomAdminSite(name="custom_admin")
custom_admin_site.register(Product)
custom_admin_site.register(Service)
custom_admin_site.register(BlogPost)
custom_admin_site.register(Category)
custom_admin_site.register(BlogCategory)
custom_admin_site.register(GalleryImage)
