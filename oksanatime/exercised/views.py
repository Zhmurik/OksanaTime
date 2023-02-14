from django.shortcuts import get_object_or_404, render

from django.template import loader

from .models import Exercise, Equipment


def index(request):
    latest_exercise_list = Exercise.objects.all()
    context = {
        'latest_exercise_list': latest_exercise_list,
    }
    return render(request, 'exercised/index.html', context)


def detail(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    return render(request, 'exercised/detail.html', {'exercise': exercise})


def equipmentViews(request):
    equipment_list = Equipment.objects.all()
    context = {
        'equipment_list': equipment_list,
    }
    return render(request, 'exercised/equipment.html', context)
