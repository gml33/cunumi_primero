from .models import paciente, historiaClinica, derivacion, evolucion
from rest_framework import serializers


class pacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = paciente
        fields = '__all__'


class historiaClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = historiaClinica
        fields = '__all__'


class derivacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = derivacion
        fields = '__all__'


class evolucionserializer(serializers.ModelSerializer):
    class Meta:
        model = evolucion
        fields = '__all__'
