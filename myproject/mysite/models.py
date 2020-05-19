
from django.db import models
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey

# Create your models here.

class Category(MPTTModel):
    name = models.CharField(verbose_name='Название',
                            max_length=255,
                            unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    description = models.TextField(verbose_name='Описание',
                                   max_length=4095,
                                   blank=True)
    is_active = models.BooleanField(default=True,
                                    verbose_name='Активная')
    image = models.ImageField(verbose_name='Изображение',
                              null=False,
                              default='',
                              blank=True,
                              upload_to='images/category')

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    category = TreeForeignKey(Category,
                              on_delete=models.SET_DEFAULT,
                              default=16,
                              null=False,
                              blank=False,
                              verbose_name='Категория'
                              )
    name = models.CharField(verbose_name='Название',
                            max_length=255,
                            default='')
    articul = models.CharField(verbose_name='Артикул',
                               max_length=255,
                               null=True,
                               blank=False,
                               unique=True)
    description = models.TextField(verbose_name='Описание',
                                   max_length=4095,
                                   default='',
                                   blank=True)
    is_active = models.BooleanField(default=True,
                                    verbose_name='Есть на складе')
    preview = models.ImageField(verbose_name='Превью',
                                null=True,
                                blank=True,
                                upload_to='images/product_preview')
    count_product = models.IntegerField(verbose_name='Количество',
                                        null=False,
                                        default=0,
                                        blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Категория')
    image = models.ImageField(verbose_name='Изображение',
                              null=False,
                              default='',
                              blank=True,
                              upload_to='images/product')


    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товара'