# django
from django.db import router
from django.urls import path

# rest framework
from rest_framework.routers import DefaultRouter

# views Sets
from .views import RatonViewSet, TecladoViewSet, MonitorViewSet, ComputadoraViewSet, OrdenViewSet

router = DefaultRouter()
router.register(r'Raton', RatonViewSet)
router.register(r'Teclado', TecladoViewSet)
router.register(r'Monitor', MonitorViewSet)
router.register(r'Computadora', ComputadoraViewSet)
router.register(r'Orden', OrdenViewSet)

urlpatterns = router.urls

urlpatterns += [

]