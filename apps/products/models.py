from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel
# Create your models here.


class Ubicacion(BaseModel):

    # TODO> Define Fields Here
    ubicacion = models.CharField('Ubicacion', max_length=50, blank=False, null=True, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = ("Ubicacion")
        verbose_name_plural = ("Ubicaciones")

    def __str__(self):
        return self.ubicacion

class Descripcion(BaseModel):

    # TODO> Define Fields Here
    descripcion = models.CharField('Departamento', max_length=50, blank=False, null=True, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = ("Descripcion")
        verbose_name_plural = ("Descripciones")

    def __str__(self):
        return self.descripcion

class Fotos(BaseModel):

    # TODO> Define Fields Here
    fotos = models.CharField('Despartamento1', max_length=50, blank=False, null=True, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = ("Foto")
        verbose_name_plural = ("Fotos")

    def __str__(self):
        return self.fotos


class Viaje(BaseModel):

    name = models.CharField('Nombre Del Viaje', max_length=150, unique=True, blank=False, null=True)
    #name = models.CharField('Nombre de Producto', max_length=150, unique=True, blank=False, null=False)

    origen = models.ForeignKey(Origen, on_delete=models.CASCADE, verbose_name='Origen')
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE, verbose_name='Destino')

    tipo_de_bus = models.ForeignKey(TipoDeBus, on_delete=models.CASCADE, verbose_name='Tipo de Bus')
    numero_de_bus = models.ForeignKey(NumeroDeBus, on_delete=models.CASCADE, verbose_name='Numero de Bus')
    fecha_de_salida = models.ForeignKey(FechaDeSalida, on_delete=models.CASCADE, verbose_name='Fecha de Salida')
    hora_de_salida = models.ForeignKey(HoraDeSalida, on_delete=models.CASCADE, verbose_name='Hora de Salida')
    estado = models.BooleanField('Estado del Bus', null=True)
    precio = models.PositiveIntegerField(default = 0)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = ("Viaje")
        verbose_name_plural = ("Viajes")

    def __str__(self):
        return self.name
