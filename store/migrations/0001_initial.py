# Generated by Django 4.2.1 on 2023-05-25 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(help_text='Unique value for product page URL, created from name.', max_length=255, unique=True)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('meta_keywords', models.CharField(help_text='Comma-delimited set of SEO keywords for meta tag', max_length=255, verbose_name='Meta Keywords')),
                ('meta_description', models.CharField(help_text='Content for description meta tag', max_length=255, verbose_name='Meta Description')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('author', models.CharField(default='admin', max_length=255)),
                ('slug', models.SlugField(help_text='Unique value for product page URL, created from name.', max_length=255, unique=True)),
                ('brand', models.CharField(max_length=255)),
                ('image', models.ImageField(default='/images/car1.jpg', upload_to='images/')),
                ('sku', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9)),
                ('is_active', models.BooleanField(default=True)),
                ('is_bestseller', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('in_stock', models.BooleanField(default=True)),
                ('quantity', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, default='Description coming soon', verbose_name='Description')),
                ('meta_keywords', models.CharField(help_text='Comma-delimited set of SEO keywords for meta tag', max_length=255)),
                ('meta_description', models.CharField(help_text='Content for description meta tag', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('color', models.CharField(default='white', max_length=30, verbose_name='Color')),
                ('material', models.CharField(default='Leather', max_length=30, verbose_name='Material')),
                ('condition', models.CharField(choices=[('New', 'New Product'), ('Last', 'Last Product')], max_length=100)),
                ('status', models.CharField(choices=[('Published', 'Published Product'), ('Draft', 'Draft Product')], max_length=200)),
                ('info', models.TextField(default='Information coming soon', verbose_name='Additional Information')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='store.category', verbose_name='Category')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
