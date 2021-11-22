from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(TravelCountry)
admin.site.register(TravelCountryDescription)
admin.site.register(TravelCountryInclude)
admin.site.register(TravelCountryProgram)
admin.site.register(TravelMed)
admin.site.register(TravelHot)
#admin.site.register()
