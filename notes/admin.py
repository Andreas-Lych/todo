from django.contrib import admin

from notes.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    author = ("name")
    title = ("title")
    created_at = ("created_at",)
    text = ("description")



from django.contrib import admin

# Register your models here.
