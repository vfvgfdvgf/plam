from django.db import models

# ---------------------------
# تصنيفات المنتجات
# ---------------------------
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم التصنيف")

    def __str__(self):
        return self.name


# ---------------------------
# المنتجات
# ---------------------------
class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="اسم المنتج")
    description = models.TextField(verbose_name="وصف المنتج")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="صورة المنتج")
    image_url = models.URLField(blank=True, null=True, verbose_name="رابط صورة المنتج")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products', verbose_name="التصنيف")
    is_featured = models.BooleanField(default=False, verbose_name="منتج مميز")
    is_best_seller = models.BooleanField(default=False, verbose_name="الأكثر مبيعاً")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخر تعديل")  # تم إضافة هذا الحقل

    def __str__(self):
        return self.name


# ---------------------------
# الخدمات
# ---------------------------
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان الخدمة")
    description = models.TextField(verbose_name="وصف الخدمة")
    image = models.ImageField(upload_to='services/', blank=True, null=True, verbose_name="صورة الخدمة")
    image_url = models.URLField(blank=True, null=True, verbose_name="رابط صورة الخدمة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخر تعديل")  # تم إضافة هذا الحقل

    def __str__(self):
        return self.title


# ---------------------------
# تصنيفات المدونة
# ---------------------------
class BlogCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم تصنيف المدونة")

    def __str__(self):
        return self.name


# ---------------------------
# مقالات المدونة
# ---------------------------
class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان المقال")
    content = models.TextField(verbose_name="محتوى المقال")
    image = models.ImageField(upload_to='blog/', blank=True, null=True, verbose_name="صورة المقال")
    image_url = models.URLField(blank=True, null=True, verbose_name="رابط صورة المقال")
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts', verbose_name="تصنيف المقال")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخر تعديل")  # تم إضافة هذا الحقل
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ النشر")  # مفيد للسيت ماب

    def __str__(self):
        return self.title


# ---------------------------
# صور المعرض (Gallery)
# ---------------------------
class GalleryImage(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name="عنوان الصورة")
    image = models.ImageField(upload_to='gallery/', blank=True, null=True, verbose_name="الصورة")
    image_url = models.URLField(blank=True, null=True, verbose_name="رابط الصورة")  # رابط خارجي
    source_type = models.CharField(
        max_length=20,
        choices=(
            ('product', 'منتج'),
            ('service', 'خدمة'),
            ('blog', 'مقال'),
            ('manual', 'مضاف يدوياً')
        ),
        default='manual',
        verbose_name="نوع المصدر"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخر تعديل")  # تم إضافة هذا الحقل

    def __str__(self):
        return self.title or f"صورة {self.id}"
