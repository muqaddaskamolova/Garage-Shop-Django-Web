from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from garage import settings


# Create your models here.
class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True,
                            help_text='Unique value for product page URL, created from name.')
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField("Meta Keywords", max_length=255,
                                     help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField("Meta Description", max_length=255,
                                        help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # products = models.ManyToManyField("Product", verbose_name=("Products"),
    #                                  blank=True, null=True, related_name="+")

    class Meta:
        db_table = 'categories'

    ordering = ['-created_at']
    verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name

    # @models.permalink
    def get_absolute_url(self):
        return reverse('store:category_list', kwargs={'slug': self.slug})


class Product(models.Model):
    CONDITION = (('New', 'New Product'), ('Last', 'Last Product'))
    STATUS = (('Published', 'Published Product'), ('Draft', 'Draft Product'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category',
                                 related_name='product')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE,
                                   related_name='product_creator')
    name = models.CharField(max_length=255, unique=True)
    author = models.CharField(max_length=255, default='admin')
    slug = models.SlugField(max_length=255, unique=True,
                            help_text='Unique value for product page URL, created from name.')
    brand = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', default='/images/car1.jpg')
    sku = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    old_price = models.DecimalField(max_digits=9, decimal_places=2,
                                    blank=True, default=0.00)
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    in_stock = models.BooleanField(default=True)
    quantity = models.CharField(max_length=255)
    description = models.TextField(default='Description coming soon', verbose_name='Description', blank=True)
    meta_keywords = models.CharField(max_length=255,
                                     help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField(max_length=255,
                                        help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    color = models.CharField(max_length=30, default='white', verbose_name='Color')
    material = models.CharField(max_length=30, default='Leather', verbose_name='Material')
    condition = models.CharField(choices=CONDITION, max_length=100)
    status = models.CharField(choices=STATUS, max_length=200)
    info = models.TextField(default='Information coming soon', verbose_name='Additional Information')
    objects = models.Manager()
    products = ProductManager()

    # categories = models.ManyToManyField("Category", verbose_name=("categories"),
    #                                     blank=True, null=True, related_name="+")
    def get_first_image(self):
        if self.images:
            try:
                return self.images.first().image.url
            except:
                return 'https://avatars.mds.yandex.net/i?id=64a306848159675833371ba4a08fa3bb655cfd8a-6971541-images-thumbs&n=13'
        else:
            return 'https://avatars.mds.yandex.net/i?id=64a306848159675833371ba4a08fa3bb655cfd8a-6971541-images-thumbs&n=13'

    class Meta:
        db_table = 'products'

    ordering = ['-created_at']
    verbose_name = 'Product'
    verbose_name_plural = 'Products'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:product_detail', kwargs={'slug': self.slug})

    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None
