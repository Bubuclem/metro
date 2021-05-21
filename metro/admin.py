from django.contrib import admin

from .models import Station, Ligne, Trajet

class StationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nom']}),
        (None, {'fields': ['x_coord']}),
        (None, {'fields': ['y_coord']})
    ]
    search_fields = ['nom']

admin.site.register(Station, StationAdmin)

class StationInline(admin.TabularInline):
    model = Station
    extra = 3

class LigneAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nom']}),
        (None, {'fields': ['stations']}),
    ]
    list_display = ('nom', 'get_stations')
    
admin.site.register(Ligne,LigneAdmin)

class TrajetAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['FromStation']}),
        (None, {'fields': ['ToStation']}),
        (None, {'fields': ['distance']}),
        (None, {'fields': ['time']}),
    ]
    list_display = ('__str__', 'distance','time')
    search_fields = ['FromStation__nom','ToStation__nom']

admin.site.register(Trajet,TrajetAdmin)