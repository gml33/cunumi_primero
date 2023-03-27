from importlib.resources import path
from django.conf.urls.static import static
from operator import index
from django.conf import settings
from django.urls import path, include
from .views import agregar_historiaClinica, agregar_paciente, index, listar_historiaClinicas, listar_pacientes, \
    modificar_paciente, eliminar_paciente, agregar_historiaClinica, listar_historiaClinicas, modificar_historiaClinica, eliminar_historiaClinica, \
    registro, agregar_evolucion, listar_evoluciones, modificar_evolucion, eliminar_evolucion, detalle_paciente, detalle_historiaClinica,\
    detalle_evolucion, agregar_derivacion, detalle_derivacion, listar_derivaciones, modificar_derivacion, eliminar_derivacion
from rest_framework import routers
from .api import PacienteViewset, HistoriaClinicaViewset, evolucionViewset, DerivacionViewset

app_name = 'gestion'

router = routers.DefaultRouter()
router.register('api/v1/pacientes', PacienteViewset, 'pacientes')
router.register('api/v1/historiaClinicas',
                HistoriaClinicaViewset, 'historiaClinicas')
router.register('api/v1/evoluciones', evolucionViewset, 'evoluciones')
router.register('api/v1/derivaciones', DerivacionViewset, 'derivaciones')


urlpatterns = [
    path('', index, name='index'),
    path('registro/', registro, name="registro"),
    # ------------pacientes----------------------
    path('agregar-paciente/', agregar_paciente, name='agregar_paciente'),
    path('detalle-paciente/<id>/', detalle_paciente, name='detalle_paciente'),
    path('listar-pacientes/', listar_pacientes, name='listar_pacientes'),
    path('modificar-paciente/<id>/', modificar_paciente, name='modificar_paciente'),
    path('eliminar-paciente/<id>/', eliminar_paciente, name='eliminar_paciente'),
    # ------------historiaClinicas----------------------------
    path('agregar-historiaClinica/', agregar_historiaClinica,
         name='agregar_historiaClinica'),
    path('detalle-historiaClinica/<id>/',
         detalle_historiaClinica, name='detalle_historiaClinica'),
    path('listar-historiaClinicas/', listar_historiaClinicas,
         name='listar_historiaClinicas'),
    path('modificar-historiaClinica/<id>/',
         modificar_historiaClinica, name='modificar_historiaClinica'),
    path('eliminar-historiaClinica/<id>/',
         eliminar_historiaClinica, name='eliminar_historiaClinica'),
    # ------------evoluciones----------------------------
    path('agregar-evolucion/', agregar_evolucion, name='agregar_evolucion'),
    path('detalle-evolucion/<id>/', detalle_evolucion, name='detalle_evolucion'),
    path('listar-evoluciones/', listar_evoluciones, name='listar_evoluciones'),
    path('modificar-evolucion/<id>/',
         modificar_evolucion, name='modificar_evolucion'),
    path('eliminar-evolucion/<id>/', eliminar_evolucion, name='eliminar_evolucion'),
    # -----------------------derivaciones---------------------------------
    path('agregar-derivacion/', agregar_derivacion, name='agregar_derivacion'),
    path('detalle-derivacion/<id>/', detalle_derivacion, name='detalle_derivacion'),
    path('listar-derivacion/', listar_derivaciones, name='listar_derivaciones'),
    path('modificar-derivacion/<id>/',
         modificar_derivacion, name='modificar_derivacion'),
    path('eliminar-derivacion/<id>/',
         eliminar_derivacion, name='eliminar_derivacion'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls
