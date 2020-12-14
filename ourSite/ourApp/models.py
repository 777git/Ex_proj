from django.db import models

# Create your models here.
class New(models.Model):
    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новина'
    def __str__(self):
        return self.title
     title = models.TextField()