from django.shortcuts import render, get_object_or_404
from .models import Soldier, Barrack

def index(request):
    """
    Главная страница, отображает списки военных и казарм.
    """
    soldiers = Soldier.objects.all()
    barracks = Barrack.objects.all()
    context = {
        'soldiers': soldiers,
        'barracks': barracks,
    }
    return render(request, 'polls/index.html', context)

def soldier_detail(request, pk):
    """
    Детальная информация о конкретном военном.
    """
    soldier = get_object_or_404(Soldier, pk=pk)
    return render(request, 'polls/soldier_detail.html', {'soldier': soldier})

def barrack_detail(request, pk):
    """
    Детальная информация о казарме с списком военных, которые в ней размещены.
    """
    barrack = get_object_or_404(Barrack, pk=pk)
    soldiers_in_barrack = Soldier.objects.filter(barrack=barrack)
    return render(request, 'polls/barrack_detail.html', {'barrack': barrack, 'soldiers': soldiers_in_barrack})
