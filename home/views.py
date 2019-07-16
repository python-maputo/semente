from django.shortcuts import render


def home_view(request):
    data = {}
    data['value'] = 20000
    return render(request, 'home/index.html', data)
