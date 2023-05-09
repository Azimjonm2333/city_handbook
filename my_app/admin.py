from django.contrib import admin
from django.contrib.auth.models import Group
from my_app.models import Category, Contact, School, Town

admin.site.unregister(Group)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Town)
class TownAdmin(admin.ModelAdmin):

    list_display = ("name", "school_counts")

    def school_counts(self, instance):
        return instance.town.count()
    school_counts.short_description = "Количество школ"


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):

    list_display = ("id", "title", "town", "address", "description", "my_categories")
    list_filter = ("town", "address")
    search_fields = ("title", "address")
    list_display_links = ("id", "title")
    list_per_page = 10
    date_hierarchy = "create_time"

    def my_categories(self, instance):
        return instance.categories
    my_categories.short_description = "Категории"
