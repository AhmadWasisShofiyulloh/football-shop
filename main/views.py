from django.shortcuts import render

def show_main(request):
    context = {
        'app name' : 'Kicks & Giggles',
        'name': 'Ahmad Wasis Shofiyulloh',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)