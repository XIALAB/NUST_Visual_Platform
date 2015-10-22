from django.shortcuts import render


def index(request):
    return render(request, 'sample/show.html', {
            'index': True
        })

def show_1(request, month):
    return render(request, 'sample/show.html', {
            'value': month
        })

def show_2(request, year):
    info = {'name': 'newbie', 'enroll': year}
    return render(request, 'sample/show.html', {
            'value': year,
            'info': info,
        })
