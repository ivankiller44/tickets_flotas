from django.urls import path

from apps.products.api.views.general_views import OrigenListAPIView, DestinoListAPIView, NumeroDeBusListAPIView, TipoDeBusListAPIView, FechaDeSalidaListAPIView, HoraDeSalidaListAPIView
from apps.products.api.views.product_views import ViajeListAPIView

urlpatterns = [
    path('origen/', OrigenListAPIView.as_view(), name = 'origen'),
    path('destino/', DestinoListAPIView.as_view(), name = 'destino'),
    path('numerodebus/', NumeroDeBusListAPIView.as_view(), name = 'numerodebus'),
    path('tipodebus/', TipoDeBusListAPIView.as_view(), name = 'tipodebus'),
    path('fechadesalida/', FechaDeSalidaListAPIView.as_view(), name = 'fechadesalida'),
    path('horadesalida/', HoraDeSalidaListAPIView.as_view(), name = 'horadesalida'),
    path('viaje/', ViajeListAPIView.as_view(), name = 'viaje'),
]
