from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel
# Create your models here.


class MeasureUnit(BaseModel):

    # TODO> Define Fields Here
    description = models.CharField('Description', max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = ("Unidad de Medida")
        verbose_name_plural = ("Unidades de Medidas")

    def __str__(self):
        return self.description

class CategoryProduct(BaseModel):
    
    description = models.CharField('Description', max_length=50, unique=True, null=False, blank=False)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name= 'Unidad de Medida')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = _("Categoria de Producto")
        verbose_name_plural = _("Categorias de Productos")

    def __str__(self):
        return self.description

class Indicator(BaseModel):

    descount_value = models.PositiveIntegerField(default = 0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name = 'Indicador de Oferta')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = _("Indicador de Oferta")
        verbose_name_plural = _("Indicadores de Ofertas")

    def __str__(self):
        return f'Oferta de la categoria {self.category_product} : {self.descount_value}%'



class Product(BaseModel):

    name = models.CharField('Nombre de Producto', max_length=150, unique=True, blank=False, null=False)
    description = models.TextField('Descripcion de Producto', blank=False, null=False)
    image = models.ImageField('Imagen del Producto', upload_to='products/', blank=True, null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name
