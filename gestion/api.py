from .models import paciente, historiaClinica, evolucion, derivacion
from rest_framework import viewsets, permissions
from .serializers import pacienteSerializer, historiaClinicaSerializer, derivacionSerializer, evolucionserializer


class PacienteViewset(viewsets.ModelViewSet):
    queryset = paciente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = pacienteSerializer

    def get_queryset(self):
        pacientes = paciente.objects.all()

        estado = self.request.GET.get('estado')

        if estado:
            pacientes = pacientes.filter(estado=estado)

        return pacientes


class HistoriaClinicaViewset(viewsets.ModelViewSet):
    queryset = historiaClinica.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = historiaClinicaSerializer

    def get_queryset(self):
        historiaClinicas = historiaClinica.objects.all()
        return historiaClinicas


class evolucionViewset(viewsets.ModelViewSet):
    queryset = evolucion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = evolucionserializer

    def get_queryset(self):
        evoluciones = evolucion.objects.all()
        return evoluciones


class DerivacionViewset(viewsets.ModelViewSet):
    queryset = derivacion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = derivacionSerializer

    def get_queryset(self):
        derivaciones = derivacion.objects.all()
        return derivaciones
