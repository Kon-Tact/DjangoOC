from django.contrib import admin
from listings.models import Band, New

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')

class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')

admin.site.register(Band, BandAdmin)
admin.site.register(New, NewAdmin)
# Register your models here.
