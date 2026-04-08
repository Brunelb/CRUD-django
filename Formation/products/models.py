from django.urls import reverse
from django.db import models


# # Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    actif = models.BooleanField(default=True)
    slug =models.SlugField(null=True)

    class Meta:
        verbose_name = ("product")
        verbose_name_plural = ("products")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("product_update", kwargs={"my_id":self.pk})
    
    