from django.contrib import admin
from .models import paciente, historiaClinica, evolucion,  derivacion


class pacienteAdmin(admin.ModelAdmin):
    list_display = ["nombre", "apellido", "edad", 'dni', "estado"]
    list_editable = ["estado"]
    search_fields = ["nombre", 'apellido', 'estado']
    list_filter = ["estado"]
    list_per_page = 30


class historiaClinicaAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'fecha', 'detalle']
    list_editable = ['detalle']
    search_fields = ['fecha']
    list_per_page = 10


class evolucionAdmin(admin.ModelAdmin):
    list_display = ["fecha", "paciente", 'detalle']
    search_fields = ["fecha", "paciente"]
    list_filter = ["fecha", "paciente"]


class derivacionAdmin(admin.ModelAdmin):
    list_display = ["paciente", 'fecha']
    search_fields = ["paciente", "fecha"]
    list_filter = ['paciente', 'fecha']
    list_per_page = 50

    # Register your models here.
admin.site.register(paciente, pacienteAdmin)
admin.site.register(historiaClinica, historiaClinicaAdmin)
admin.site.register(evolucion, evolucionAdmin)
admin.site.register(derivacion, derivacionAdmin)
