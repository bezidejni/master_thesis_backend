from django.contrib import admin
from .models import CPUInfo, NetworkInfo, DOMElementCount


class CPUInfoModelAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'value')


class NetworkInfoModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'source_url', 'destination_url', 'type', 'method')
    list_filter = ('method', 'http_status', 'type')
    search_fields = ('source_url', 'destination_url')


class DOMElementCountModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'element_name', 'count', 'timestamp')
    list_filter = ('element_name',)


admin.site.register(CPUInfo, CPUInfoModelAdmin)
admin.site.register(NetworkInfo, NetworkInfoModelAdmin)
admin.site.register(DOMElementCount, DOMElementCountModelAdmin)
