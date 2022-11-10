from django.db import models
from Administracion.models import Residencia


class Correspondencia(models.Model):
    nResidencia = models.ForeignKey(Residencia,null=True,blank=True,on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10)
    
    nDestinatario = models.CharField(max_length=30)
    tDestinatario = models.PositiveIntegerField()
    estado_choice = (('Entregado', 'Entregado'),('Pendiente', 'Pendiente'),('Imposible realizacion', 'Imposible realizacion'))
    estado = models.CharField(max_length=30,choices=estado_choice)
    comentario = models.CharField(max_length=100)
    
    def __str__(self):
        texto = "{0} {1}: {2}"
        return texto.format(self.estado,self.nDestinatario,self.tipo)
        