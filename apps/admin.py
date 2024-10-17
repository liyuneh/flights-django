from django.contrib import admin

from .models import Airport, Flight,Passenger,Food

admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Food)
# Register your models here.
