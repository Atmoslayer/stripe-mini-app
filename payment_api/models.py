from django.db import models
from django.core.validators import MinValueValidator

class Item(models.Model):
    name = models.CharField(
        'Название',
        max_length=200,
    )

    description = models.TextField(
        'Описание',
        max_length=200,
        blank=True,
    )

    price = models.IntegerField(
        'Цена',
        validators=[MinValueValidator(0)],
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
