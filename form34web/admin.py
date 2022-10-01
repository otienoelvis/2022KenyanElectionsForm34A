from django.contrib import admin

from form34web.models import Region, Pdfpath


class RegionAdmin(admin.ModelAdmin):
    list_display = ('iebc_region',)
    search_fields = ('iebc_region',)
    readonly_fields = ('iebc_region',)
    filter_horizontal = ()
    list_per_page = 100
    list_filter = ()
    fieldsets = ()


class PdfpathAdmin(admin.ModelAdmin):
    list_display = ('polling_station_code', 'form_34_path', 'date_posted',)
    search_fields = ('polling_station_code', 'form_34_path',)
    readonly_fields = ('polling_station_code', 'form_34_path', 'date_posted',)
    filter_horizontal = ()
    list_per_page = 100
    list_filter = ()
    fieldsets = ()


admin.site.register([Region], RegionAdmin)
admin.site.register([Pdfpath], PdfpathAdmin)
