from django.db import models

from taggit.managers import TaggableManager


class Category(models.Model):  # type: ignore
    name = models.CharField(max_length=255, unique=True, null=False)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):  # type: ignore
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tags = TaggableManager(blank=True)

    def __str__(self) -> str:
        return f"{self.category}: {self.name}"
