from django.contrib import admin
from .models import Host, Net, CategoriasNet, Site, Line
# Register your models here.

class HostAdmin(admin.ModelAdmin):
    list_display = ('ip', 'hostname', 'red_num', 'loc', 'alive',)

admin.site.register(Host, HostAdmin)
admin.site.register(Net)
admin.site.register(CategoriasNet)
admin.site.register(Site)
admin.site.register(Line)