from django.contrib import admin
from .models import Correspondencia
# Register your models here.
#admin.site.register(Correspondencia)

@admin.register(Correspondencia)
class CorrespondenciaConserjeria(admin.ModelAdmin):
    list_display=('nResidencia','tipo','d3','estado')
    #ordering = ('nResidencia','tipo')
    #search_fields=('nResidencia',)
    list_editable=('estado',)
    list_filter=('estado',)


    
    def d3(self,obj):
        return obj.nDestinatario.upper()
    d3.short_description = "Nombre Destinatario"
    
    d3.admin_order_field = 'nDestinatario'