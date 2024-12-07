from django.contrib import admin
from .models import Category,News

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at", "is_published")
    list_filter = ("category", "is_published")
    search_fields = ("title", "content")
    list_per_page = 10

    fieldsets = (
        (None, {
            "fields":("title", "content", "category")
        }),
        ("Дополнительные настройки",{
            "classes": ("collapse",),
            "fields":("is_published", "created_at", "updated_at")
        }),
    )
    readonly_fields = ("created_at", "updated_at")
