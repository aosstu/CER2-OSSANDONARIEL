from django.db import models

# Create your models here.


class Residencia(models.Model):
    nResidencia = models.PositiveIntegerField()
    titularResidencia = models.CharField(max_length=30)
    tDestinatario = models.PositiveIntegerField()
    def __str__(self):
        return str(self.nResidencia)
    class Meta:
        verbose_name='residencia'
        verbose_name_plural='residencias'
        db_table='residencia'
        