from django.contrib import admin
from django.contrib.auth.models import Group
from my_app.models import Category, Contact, Place, City

admin.site.unregister(Group)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):

    list_display = ("name", "place_counts")

    def place_counts(self, instance):
        return instance.city.count()
    place_counts.short_description = "Количество школ"


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):

    list_display = ("id", "title", "city", "address", "description", "my_categories")
    list_filter = ("city", "address")
    search_fields = ("title", "address")
    list_display_links = ("id", "title")
    list_per_page = 10
    date_hierarchy = "create_time"

    def my_categories(self, instance):
        return instance.categories
    my_categories.short_description = "Категории"
