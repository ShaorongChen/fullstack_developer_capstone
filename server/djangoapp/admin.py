from django.contrib import admin
from .models import CarMake, CarModel

# Register your models here.


class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 3


class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'year', 'car_make')
    list_filter = ('type', 'year', 'car_make')


class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
