from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Mavzu:')
    content = models.TextField(blank=True, null=True, verbose_name='Ma\'lumot')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, )
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    is_published = models.BooleanField(default=True, )
    views = models.ImageField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
