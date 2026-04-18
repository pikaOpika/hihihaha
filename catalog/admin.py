from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from catalog.models import LiteraryFormat, Book, Author

# Register your models here.
# admin.site.register(LiteraryFormat)
# admin.site.register(Book)

class BookInline(admin.TabularInline):
    model = Book
    extra = 1

@admin.register(LiteraryFormat)
class LiteraryFormatAdmin(admin.ModelAdmin):
    inlines = [BookInline]

# class AuthorInline(admin.TabularInline):
#     model = Author
#     extra = 1


# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ["title", "price", "format"]
#     search_fields = ["title"]
#     list_filter = ["title"]
#     inlines = [AuthorInline]

admin.site.register(Author, UserAdmin)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "format"]
    ordering = ["title"]
    search_fields = ["title"]
    list_filter = ["format"]
    actions = ["change_format"]

    def change_format(self, request, queryset):
        novel = LiteraryFormat.objects.get(name="novel")
        queryset.update(format=novel)

    change_format.short_description = "Change format"
    # fieldsets = [
    #     ("main information", {
    #         "fields": ["title", "format"]
    #     })
    # ]
