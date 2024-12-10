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
        'game1': games[0],
        'game2': games[1],
        'game3': games[2],
        'comeback': comeback
    }
    return render(request, 'third_task/games.html', context)
