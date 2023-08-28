# Generated by Django 4.2.4 on 2023-08-28 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='product_images', verbose_name='Images')),
            ],
        ),
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='Image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='review',
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Image',
            field=models.ImageField(upload_to='products', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_brand', to='product.brand', verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=4000, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='flag',
            field=models.CharField(choices=[('Sale', 'Sale'), ('New', 'New'), ('Feature', 'Feature')], max_length=10, verbose_name='Falge'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=12, verbose_name='Sku'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subtitle',
            field=models.CharField(max_length=300, verbose_name='Subtitle'),
        ),
        migrations.AlterField(
            model_name='review',
            name='create_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Create At'),
        ),
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_product', to='product.product', verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.IntegerField(verbose_name='Rate'),
        ),
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.TextField(max_length=3000, verbose_name='Review'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='review_auther', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='productimages',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='product.product', verbose_name='Product Images'),
        ),
        migrations.AddField(
            model_name='brand',
            name='image',
            field=models.ImageField(default=1, upload_to='brand', verbose_name='Image'),
            preserve_default=False,
        ),
    ]
