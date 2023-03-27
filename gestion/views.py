from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User

from .forms import pacienteForm
from .models import paciente, historiaClinica, evolucion, derivacion
from django.contrib import messages

from .forms import pacienteForm, historiaClinicaForm, CustomUserCreationForm, evolucionForm, derivacionForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required


@login_required
def index(request):
    pacientes = paciente.objects.all()[:5]
    historiaClinicas = historiaClinica.objects.all()[:5]
    total_pacientes = paciente.objects.all().count()
    total_historiaClinicas = historiaClinica.objects.all().count()
    data = {
        'pacientes': pacientes,
        'historiaClinicas': historiaClinicas,
        'total_pacientes': total_pacientes,
        'total_historiaClinicas': total_historiaClinicas,
    }
    return render(request, 'gestion/index.html', data)


@permission_required('api.add_paciente')
def agregar_paciente(request):
    data = {
        'form': pacienteForm()
    }
    if request.method == 'POST':
        formulario = pacienteForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "paciente agregado correctamente")
            return redirect(to="gestion:listar_pacientes")
        else:
            data["form"] = formulario
    return render(request, 'gestion/paciente/agregar.html', data)


@permission_required('api.view_paciente')
def listar_pacientes(request):
    pacientes = paciente.objects.all().order_by('apellido')
    data = {
        'pacientes': pacientes
    }
    return render(request, 'gestion/paciente/listar.html', data)


@permission_required('api.view_paciente')
def detalle_paciente(request, id):
    pelotudo = get_object_or_404(paciente, pk=id)
    evoluciones = evolucion.objects.filter(paciente=pelotudo)
    hcs = historiaClinica.objects.filter(paciente=pelotudo)
    data = {
        'paciente': pelotudo,
        'evoluciones': evoluciones,
        'hcs': hcs
    }
    return render(request, 'gestion/paciente/detalle.html', data)


@permission_required('api.change_paciente')
def modificar_paciente(request, id):
    pelotudo = get_object_or_404(paciente, id=id)
    data = {
        'form': pacienteForm(instance=pelotudo)
    }
    if request.method == 'POST':
        formulario = pacienteForm(
            data=request.POST, instance=pelotudo, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "paciente modificado correctamente")
            return redirect(to="gestion:listar_pacientes")
        else:
            data["form"] = formulario

    return render(request, 'gestion/paciente/modificar.html', data)


@permission_required('api.delete_paciente')
def eliminar_paciente(request, id):
    pacienteVar = get_object_or_404(paciente, pk=id)
    identificador = str(pacienteVar.pk)
    pacienteVar.delete()
    messages.success(request, "paciente eliminado correctamente")
    return redirect(to="gestion:listar_pacientes")


# ------------historiaClinicas-------------------------------------------
@permission_required('api.add_historiaClinica')
def agregar_historiaClinica(request):
    data = {
        'form': historiaClinicaForm()
    }
    if request.method == 'POST':
        formulario = historiaClinicaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "historiaClinica agregada correctamente")
            return redirect(to="gestion:listar_historiaClinicas")
        else:
            data["form"] = formulario
    return render(request, 'gestion/historiaClinica/agregar.html', data)


@permission_required('api.view_historiaClinica')
def listar_historiaClinicas(request):
    historiaClinicas = historiaClinica.objects.all().order_by('fecha')
    data = {
        'historiaClinicas': historiaClinicas
    }
    return render(request, 'gestion/historiaClinica/listar.html', data)


@permission_required('api.view_historiaClinica')
def detalle_historiaClinica(request, id):
    historiaClinicaVar = get_object_or_404(historiaClinica, id=id)
    #pacienteVar = paciente.objects.filter(historiaClinica=historiaClinica).order_by('fecha')
    data = {
        'historiaClinica': historiaClinicaVar,
        #'paciente': pacienteVar
    }
    return render(request, 'gestion/historiaClinica/detalle.html', data)


@permission_required('api.change_historiaClinica')
def modificar_historiaClinica(request, id):
    historiaClinicaVar = get_object_or_404(historiaClinica, id=id)
    data = {
        'form': historiaClinicaForm(instance=historiaClinicaVar)
    }
    if request.method == 'POST':
        formulario = historiaClinicaForm(
            data=request.POST, instance=historiaClinicaVar)
        if formulario.is_valid():
            formulario.save()
            messages.success(
                request, "historiaClinica modificada correctamente")
            return redirect(to="gestion:listar_historiaClinicas")
        else:
            data["form"] = formulario

    return render(request, 'gestion/historiaClinica/modificar.html', data)


@permission_required('api.delete_historiaClinica')
def eliminar_historiaClinica(request, id):
    historiaClinicaVar = get_object_or_404(historiaClinica, pk=id)
    historiaClinicaVar.delete()
    messages.success(request, "historiaClinica eliminada correctamente")
    return redirect(to="gestion:listar_historiaClinicas")

# ------------evoluciones-----------------------------------


@permission_required('api.add_evolucion')
def agregar_evolucion(request):
    data = {
        'form': evolucionForm()
    }
    if request.method == 'POST':
        formulario = evolucionForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "evolucion agregado correctamente")
            return redirect(to="gestion:listar_evoluciones")
        else:
            data["form"] = formulario
    return render(request, 'gestion/evolucion/agregar.html', data)


@permission_required('api.view_evolucion')
def listar_evoluciones(request):
    evoluciones = evolucion.objects.all().order_by('fecha')
    data = {
        'evoluciones': evoluciones
    }
    return render(request, 'gestion/evolucion/listar.html', data)


@permission_required('api.view_evolucion')
def detalle_evolucion(request, id):
    evolucionVar = evolucion.objects.get(id=id)
    data = {
        'evolucion': evolucionVar
    }
    return render(request, 'gestion/evolucion/detalle.html', data)


@permission_required('api.change_evolucion')
def modificar_evolucion(request, id):
    evolucion = get_object_or_404(evolucion, pk=id)
    data = {
        'form': evolucionForm(instance=evolucion)
    }
    if request.method == 'POST':
        formulario = evolucionForm(data=request.POST, instance=evolucion)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "evolucion modificado correctamente")
            return redirect(to="gestion:listar_evoluciones")
        else:
            data["form"] = formulario
    return render(request, 'gestion/evolucion/modificar.html', data)


@permission_required('api.delete_evolucion')
def eliminar_evolucion(request, id):
    evolucion = get_object_or_404(evolucion, id=id)
    evolucion.delete()
    messages.success(request, "evolucion eliminado correctamente")
    return redirect(to="gestion:listar_evoluciones")

    # ------------------------derivaciones-----------------------------------


@permission_required('api.add_derivacion')
def agregar_derivacion(request):
    derivacion = []
    data = {
        'form': derivacionForm()
    }
    if request.method == 'POST':
        formulario = derivacionForm(data=request.POST)
        if formulario.is_valid():
            derivacion = formulario.save(commit=False)
            derivacion.autor = User.objects.get(pk=request.user.id)
            derivacion.fecha = timezone.now()
            derivacion.status = 'activo'
            derivacion.save()
            messages.success(request, "derivacion agregado correctamente")
            return redirect(to="gestion:listar_derivaciones")
        else:
            data["form"] = formulario
    return render(request, 'gestion/derivacion/agregar.html', data)


@permission_required('api.view_derivacion')
def listar_derivaciones(request):
    derivaciones = derivacion.objects.all().order_by('fecha')
    data = {
        'derivaciones': derivaciones
    }
    return render(request, 'gestion/derivacion/listar.html', data)


@ permission_required('api.view_derivacion')
def detalle_derivacion(request, id):
    derivacionVar = get_object_or_404(derivacion, id=id)
    data = {
        'derivacion': derivacionVar,
    }
    return render(request, 'gestion/derivacion/detalle.html', data)


@ permission_required('api.change_derivacion')
def modificar_derivacion(request, id):
    derivacionVar = get_object_or_404(derivacion, id=id)
    data = {
        'form': derivacionForm(instance=derivacionVar)
    }
    if request.method == 'POST':
        formulario = derivacionForm(data=request.POST, instance=derivacionVar)
        if formulario.is_valid(commit=False):
            formulario.save()
            messages.success(request, "derivacion modificada correctamente")
            return redirect(to="gestion:listar_derivaciones")
        else:
            data["form"] = formulario

    return render(request, 'gestion/derivacion/modificar.html', data)


@ permission_required('api.delete_derivacion')
def eliminar_derivacion(request, id):
    derivacionVar = get_object_or_404(derivacion, id=id)
    derivacionVar.delete()
    messages.success(request, "derivacion eliminada correctamente")
    return redirect(to="gestion:listar_derivaciones")


# ------------------registro de usuarios--------------------

# ------------------turnos----------------------------------


def registro(request):
    data = {
        'form': CustomUserCreationForm
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(
                username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request, "El registro fue exitoso")
            return redirect(to='gestion:listar_historiaClinicas')
        else:
            data['form'] = formulario
    return render(request, 'registration/registro.html', data)
