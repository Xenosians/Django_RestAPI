from django.contrib import admin
from RestAPI.models import * 

class makananadmin (admin.ModelAdmin):
    list_display = ["nama","Daerah_asal"]

admin.site.register(makanan,makananadmin)
