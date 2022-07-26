# django
from django.db import router
from django.urls import path

# rest framework
from rest_framework.routers import DefaultRouter

# views Sets
from .views import AutorViewSet, FotoViewSet, ObraViewSet, ExposicionViewSet

router = DefaultRouter()
router.register(r'Autor', AutorViewSet)
router.register(r'Foto', FotoViewSet)
router.register(r'Obra', ObraViewSet)
router.register(r'Exposicion', ExposicionViewSet)

urlpatterns = router.urls

urlpatterns += [

]