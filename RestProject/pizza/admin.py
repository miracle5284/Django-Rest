from django.contrib import admin
from .models import Pizza, Size


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):

    model = Pizza


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):

    model = Size
