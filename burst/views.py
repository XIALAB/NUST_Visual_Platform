from django.shortcuts import render


def show(request):
    cnt = 0
    burst = []
    day = ''
    word = ''
    url = ''
    days = []
    for line in open('burst/shuju', 'r').readlines():
        if cnt % 3 == 0:
            day = line.strip('\n')
            days.append(day)
        if cnt % 3 == 1:
            word = line.strip('\n').decode('utf-8').encode('utf-8').split()
        if cnt % 3 == 2:
            url = line.strip('\n')
            burst.append((day, word, url))
        cnt += 1
    return render(request, 'burst/show.html',
            {
                'burst': burst,
                'names': days,
            }
    )


