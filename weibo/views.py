from django.shortcuts import render


def show(request):
    data = [[100, 200, 300], [88, 99, 111], [120, 119, 110], [111, 222, 333]]
    return render(request, 'weibo.html', {'data': data}
    )

def test(request):
    return render(request, 'noob.html')


