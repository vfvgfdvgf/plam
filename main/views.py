from decimal import Decimal
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from .models import Service, Product, BlogPost, Category, BlogCategory, GalleryImage

# ---------------------------
# الصفحة الرئيسية
# ---------------------------
def home(request):
    latest_products = Product.objects.all().order_by('-created_at')[:5]
    latest_services = Service.objects.all().order_by('-created_at')[:5]
    latest_posts = BlogPost.objects.all().order_by('-created_at')[:3]
    
    return render(request, 'home.html', {
        'latest_products': latest_products,
        'latest_services': latest_services,
        'latest_posts': latest_posts,
    })

# ---------------------------
# صفحة الخدمات
# ---------------------------
def services_view(request):
    services = Service.objects.all().order_by('-created_at')
    return render(request, 'services.html', {'services': services})

# ---------------------------
# صفحة تفاصيل الخدمة
# ---------------------------
def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'service_detail.html', {'service': service})

# ---------------------------
# صفحة المنتجات
# ---------------------------
def products_view(request):
    category_id = request.GET.get('category')
    categories = Category.objects.all()
    
    products = Product.objects.all().order_by('-created_at')
    if category_id:
        products = products.filter(category_id=category_id)
    
    return render(request, 'products.html', {
        'products': products,
        'categories': categories,
        'selected_category': int(category_id) if category_id else None
    })

# ---------------------------
# صفحة تفاصيل المنتج
# ---------------------------
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    price_range_min = product.price * Decimal('0.8')
    price_range_max = product.price * Decimal('1.2')

    related_products = Product.objects.filter(
        Q(category=product.category) |
        Q(price__gte=price_range_min, price__lte=price_range_max)
    ).exclude(id=product.id).distinct()[:4]

    return render(request, 'product_detail.html', {
        'product': product,
        'related_products': related_products
    })

# ---------------------------
# صفحة المدونة
# ---------------------------
def blog_view(request):
    category_id = request.GET.get('category')
    categories = BlogCategory.objects.all()
    
    posts = BlogPost.objects.all().order_by('-created_at')
    if category_id:
        posts = posts.filter(category_id=category_id)
    
    return render(request, 'blog.html', {
        'posts': posts,
        'categories': categories,
        'selected_category': int(category_id) if category_id else None
    })

# ---------------------------
# صفحة المقال المفصل
# ---------------------------
def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    keywords = [word for word in post.title.split() if len(word) > 3]

    query = Q()
    if post.category:
        query |= Q(category=post.category)
    for word in keywords:
        query |= Q(title__icontains=word)

    related_posts = BlogPost.objects.filter(query).exclude(id=post.id).distinct().order_by('-created_at')[:6]

    return render(request, 'blog_detail.html', {
        'post': post,
        'related_posts': related_posts
    })

# ---------------------------
# صفحة اتصل بنا
# ---------------------------
def contact_view(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        send_mail(
            f"رسالة من {name} - {subject}",
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL],
            fail_silently=False,
        )
        success = True

    return render(request, 'contact.html', {'success': success})

# ---------------------------
# صفحة المعرض (Gallery)
# ---------------------------
def gallery(request):
    gallery_images = []

    # المنتجات
    for product in Product.objects.all():
        if product.image:
            gallery_images.append({'title': product.name, 'image': product.image.url, 'type': 'product'})
        elif getattr(product, 'image_url', None):
            gallery_images.append({'title': product.name, 'image': product.image_url, 'type': 'product'})

    # الخدمات
    for service in Service.objects.all():
        if service.image:
            gallery_images.append({'title': service.title, 'image': service.image.url, 'type': 'service'})
        elif getattr(service, 'image_url', None):
            gallery_images.append({'title': service.title, 'image': service.image_url, 'type': 'service'})

    # المقالات
    for post in BlogPost.objects.all():
        if post.image:
            gallery_images.append({'title': post.title, 'image': post.image.url, 'type': 'blog'})
        elif getattr(post, 'image_url', None):
            gallery_images.append({'title': post.title, 'image': post.image_url, 'type': 'blog'})

    # صور المعرض المضافة يدوياً
    for img in GalleryImage.objects.all():
        if img.image:
            gallery_images.append({'title': img.title or f"صورة {img.id}", 'image': img.image.url, 'type': 'manual'})
        elif img.image_url:
            gallery_images.append({'title': img.title or f"صورة {img.id}", 'image': img.image_url, 'type': 'manual'})

    return render(request, 'gallery.html', {'gallery_images': gallery_images})
