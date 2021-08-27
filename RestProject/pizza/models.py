from django.db import models


class Size(models.Model):

    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'

    def __str__(self):
        return self.title


class Pizza(models.Model):
    topping1 = models.CharField(max_length=100)
    topping2 = models.CharField(max_length=100)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    class Meta:

        verbose_name = 'Pizza'
        verbose_name_plural = 'Pizza Records'

    def __str__(self):
        return '%s %s Pizza' % (self.topping1, self.topping2)
