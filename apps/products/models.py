from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel
# Create your models here.


class Origen(BaseModel):

    # TODO> Define Fields Here
    origen = models.CharField('Departamento', max_length=50, blank=False, null=True, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = ("Origen")
        verbose_name_plural = ("Origenes")

    def __str__(self):
        return self.origen

class Destino(BaseModel):

    # TODO> Define Fields Here
    destino = models.CharField('Despartamento1', max_length=50, blank=False, null=True, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = ("Destino")
        verbose_name_plural = ("Destinos")

    def __str__(self):
        return self.destino

class TipoDeBus(BaseModel):
    
    tipo = models.CharField('Tipo', max_length=50, unique=True, null=True, blank=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = ("Tipo de Bus")
        verbose_name_plural = ("Tipos de Buses")

    def __str__(self):
        return self.tipo

class NumeroDeBus(BaseModel):

    numero_de_bus = models.CharField('Numero De Bus', max_length=10, unique=True, null=True, blank=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = ("Numero de Bus")
        verbose_name_plural = ("Numeros de Buses")

    def __str__(self):
        return self.numero_de_bus

class FechaDeSalida(BaseModel):

    fecha_de_salida = models.DateField('Fecha de Salida', null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = ("Fecha de Salida")
        verbose_name_plural = ("Fechas de Salidas")

    def __str__(self):
        return str(self.fecha_de_salida)

class HoraDeSalida(BaseModel):

    hora_de_salida = models.TimeField('Hora de Salida', null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = ("Hora de Salida")
        verbose_name_plural = ("Horas de Salidas")

    def __str__(self):
        return str(self.hora_de_salida)


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

    #name = models.CharField('Nombre de Producto', max_length=150, unique=True, blank=False, null=False)
    #description = models.TextField('Descripcion de Producto', blank=False, null=False)
    #image = models.ImageField('Imagen del Producto', upload_to='products/', blank=True, null=True)
    #measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de medida', null=True)
    #category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Categoria de Producto', null=True)
    #historical = HistoricalRecords()

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
