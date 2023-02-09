from django.contrib import admin

# Register your models here.
from .models import Category, Dish, About, Events, PhotoGallery, Reservation

admin.site.register(Reservation)


class DishAdmin(admin.TabularInline):
    model = Dish
    raw_id_fields = ['category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'position',
        'is_visible',

    ]
    list_editable = [
        'position',
        'is_visible',

    ]
    inlines = [DishAdmin]


@admin.register(Dish)
class DishModel(admin.ModelAdmin):
    model = Dish
    list_display = [
        'title',
        'position',
        'is_visible',
        'ingredients',
        'description',
        'price',
        'photo',
        'category',
        'is_special',
        'weight'

    ]
    list_filter = [
        'position',
        'is_visible',
        'is_special',

    ]

    list_editable = [
        'position',
        'is_visible',
        'price',
        'weight'

    ]


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    model = About
    list_display = [
        'title',
        'description',
        'photo',
    ]

    list_editable = [
        'description',
        'photo',
    ]


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    model = Events
    list_display = [
        'title',
        'price',
        'description',
        'date',
        'is_visible',
    ]

    list_filter = [
        'date',
        'is_visible'
    ]

    list_editable = [
        'date',
        'price',
        'is_visible',
    ]


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = [
        'photo',
    ]

    list_filter = [
        'is_visible',
    ]
