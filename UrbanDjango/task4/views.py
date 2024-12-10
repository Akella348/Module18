from django.shortcuts import render

# Create your views here.

def games_view(request):
    title = "Магазин"
    title2 = "Игры"
    comeback = "Вернуться обратно"
    games = ['Warface', 'WoT', "Dota2"]
    context = {
        'title': title,
        'title2': title2,
        'games': games,
        'comeback': comeback
    }
    return render(request, 'fourth_task/games.html', context)
