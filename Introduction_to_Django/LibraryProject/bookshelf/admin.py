from django.contrib import admin
from .models import Book  # ✅ This line must be included exactly

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year',)
    search_fields = ('title', 'author')
