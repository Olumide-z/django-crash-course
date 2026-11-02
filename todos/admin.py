from django.contrib import admin

from .models import Todo, Person

admin.site.register(Person)


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'done', 'deadline', 'priority')
    list_filter = ('done', 'priority')
    search_fields = ('title',)
