from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class catgry(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def get_url(self):
        return reverse('prod_cat', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)  # for return value -->here we return the name


class products(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    img = models.ImageField(upload_to='product')
    desc = models.TextField()
    stock = models.IntegerField()
    available = models.BooleanField()
    price = models.IntegerField()
    category = models.ForeignKey(catgry, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)


    def get_url(self):
        return reverse('prod_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.name)
# Create your models here.
