from django.contrib import admin

from .models import Airport, Flight,Passenger,Food

admin.site.register(Airport)
admin.site.register(Passenger)
admin.site.register(Food)


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ['id', 'origin', 'destination', 'duration']
# Register your models here.
