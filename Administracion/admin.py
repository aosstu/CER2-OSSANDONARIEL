from django.contrib import admin
from .models import Residencia
# Register your models here.
#admin.site.register(Residencia)
@admin.register(Residencia)
class ResidenciaAdministracion(admin.ModelAdmin):
    list_display=('d3','nResidencia','d2')
    ordering=('nResidencia',)
    search_fields=('d2',)
    
    def d2(self,obj):
        return obj.titularResidencia
    def d3(self,obj):
        return obj.tDestinatario