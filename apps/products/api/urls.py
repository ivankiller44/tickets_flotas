from django.urls import path

from apps.products.api.views.general_views import DepartamentoListAPIView, Departamento1ListAPIView, NumeroDeBusListAPIView, TipoDeBusListAPIView, FechaDeSalidaListAPIView, HoraDeSalidaListAPIView
from apps.products.api.views.product_views import ViajeListAPIView

urlpatterns = [
    path('departamento/', DepartamentoListAPIView.as_view(), name = 'departamento'),
    path('departamento1/', Departamento1ListAPIView.as_view(), name = 'departamento1'),
    path('numerodebus/', NumeroDeBusListAPIView.as_view(), name = 'numerodebus'),
    path('tipodebus/', TipoDeBusListAPIView.as_view(), name = 'tipodebus'),
    path('fechadesalida/', FechaDeSalidaListAPIView.as_view(), name = 'fechadesalida'),
    path('horadesalida/', HoraDeSalidaListAPIView.as_view(), name = 'horadesalida'),
    path('viaje/', ViajeListAPIView.as_view(), name = 'viaje'),
]
