# django
from django.db import router
from django.urls import path

# rest framework
from rest_framework.routers import DefaultRouter

# views Sets
from .views import KeyboardViewSet, MouseViewSet, DisplayViewSet, SpeakerViewSet, ComputerViewSet,OrderSet, OrderDetailSet

router = DefaultRouter()
router.register(r'Teclado', KeyboardViewSet)
router.register(r'Raton', MouseViewSet)
router.register(r'Monitor', DisplayViewSet)
router.register(r'Bocina', SpeakerViewSet)
router.register(r'Computadora', ComputerViewSet)
router.register(r'orders', OrderSet)
router.register(r'orderdetails', OrderDetailSet)

urlpatterns = router.urls

urlpatterns += [

]