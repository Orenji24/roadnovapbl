from django.contrib import admin

from .models import Stop, Trip


class StopInline(admin.TabularInline):
    model = Stop
    extra = 1


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('title', 'origin', 'destination', 'start_date', 'days', 'distance_km', 'is_featured')
    list_filter = ('mood', 'is_featured')
    search_fields = ('title', 'origin', 'destination')
    inlines = [StopInline]


@admin.register(Stop)
class StopAdmin(admin.ModelAdmin):
    list_display = ('name', 'trip', 'order', 'drive_time', 'overnight')
    list_filter = ('overnight',)

# Register your models here.
