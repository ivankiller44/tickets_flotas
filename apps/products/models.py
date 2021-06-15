from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel
# Create your models here.


class Departamento(BaseModel):

    # TODO> Define Fields Here
    departamento = models.CharField('Description', max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = ("Departamento")
        verbose_name_plural = ("Departamentos")

    def __str__(self):
        return self.departamento

class Departamento1(BaseModel):

    # TODO> Define Fields Here
    departamento = models.CharField('Description', max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = ("Departamento1")
        verbose_name_plural = ("Departamentos1")

    def __str__(self):
        return self.departamento1

class TipoDeBus(BaseModel):
    
    tipo = models.CharField('Description', max_length=50, unique=True, null=False, blank=False)
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

    numero_de_bus = models.CharField('Numero De Bus', max_length=10, unique=True, null=False, blank=False)
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

    fecha_de_salida = models.DateField('Fecha de Salida')
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
        return self.fecha_de_salida

class HoraDeSalida(BaseModel):

    hora_de_salida = models.TimeField('Hora de Salida')
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
        return self.hora_de_salida


class Viaje(BaseModel):

    origen = models.ForeignKey(Departamento, on_delete=models.CASCADE, verbose_name='Departamento')
    destino = models.ForeignKey(Departamento1, on_delete=models.CASCADE, verbose_name='Departamento1')

    tipo_de_bus = models.ForeignKey(TipoDeBus, on_delete=models.CASCADE, verbose_name='Tipo de Bus')
    numero_de_bus = models.ForeignKey(NumeroDeBus, on_delete=models.CASCADE, verbose_name='Numero de Bus')
    fecha_de_salida = models.ForeignKey(FechaDeSalida, on_delete=models.CASCADE, verbose_name='Fecha de Salida')
    hora_de_salida = models.ForeignKey(HoraDeSalida, on_delete=models.CASCADE, verbose_name='Hora de Salida')
    estado = models.BooleanField('Estado del Bus', null=True)
    precio = models.PositiveIntegerField()

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
        verbose_name = ("Producto")
        verbose_name_plural = ("Productos")

    def __str__(self):
        return self.name
