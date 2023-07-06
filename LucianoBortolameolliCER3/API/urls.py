from django.urls import path, include
from rest_framework import routers
from . import views


router= routers.DefaultRouter()
router.register("Maquina",views.Maquina_ViewSet)
router.register("Herramienta",views.Maquina_ViewSet)

urlpatterns=[
    path('',include(router.urls))
]
