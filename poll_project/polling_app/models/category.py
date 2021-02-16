from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300,default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories of Questions'