from django.contrib import admin
from .models import Genre, Cast, Language, Film, FilmInstance, Director

# Register your models here.

admin.site.register(Genre)
admin.site.register(Cast)
admin.site.register(Language)
#admin.site.register(Film)
#admin.site.register(FilmInstance)
#admin.site.register(Director)


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    

admin.site.register(Director, DirectorAdmin)

class FilmsInstanceInline(admin.TabularInline):
    model = FilmInstance

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'display_genre', 'display_cast')
    inlines = [FilmsInstanceInline]


@admin.register(FilmInstance)
class FilmInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'release_date')
    list_display = ('film', 'status', 'release_date', 'id')

    fieldsets = (
        (None, {
            'fields': ('film', 'release_date', 'id')
        }),
        ('Availability',{
            'fields': ('status', 'location')
        }),
    )