from django.shortcuts import render

def home(request):
    """
    Главная страница (замена или дополнение к старой index).
    """
    return render(request, 'polls/index.html')

def strategy(request):
    """
    Страница с формой "Калькулятор маны и стратегии".
    """
    return render(request, 'polls/strategy.html')

def history(request):
    """
    Страница с "Хронологией" (если хотите её использовать).
    """
    return render(request, 'polls/history.html')
