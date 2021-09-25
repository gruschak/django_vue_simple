from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "body", "created_at")
    list_display_links = ("title", "body", "created_at")


admin.site.register(Note, NoteAdmin)
