from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from catalog.models import LiteraryFormat, Book, Author
from django.db.models import F



class BookInline(admin.TabularInline):
    model = Book
    extra = 1

class BookAuthorInline(admin.TabularInline):
    model = Book.authors.through
    extra = 1

@admin.register(LiteraryFormat)
class LiteryFormatAdmin(admin.ModelAdmin):
    search_fields = ["name",]
    list_display = ["name",]
    inlines = [BookInline,]


@admin.register(Author)
class AuthorAdmin(UserAdmin):
    list_display = ["username", "first_name", "last_name", "is_staff"]
    list_filter = ["is_staff"]
    search_fields = ["username"]
    inlines = [BookAuthorInline]
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional info",
            {
                "fields": ("pseudonym",)
            }
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": ("pseudonym",)
            }
        ),
    )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title", "price", "format"]
    actions = ["get_discount"]
    inlines = [BookAuthorInline]

    def get_discount(self, request, queryset):
        queryset.update(price=F("price") * 0.8)
    
    get_discount.short_description = "Get 20 discount"
