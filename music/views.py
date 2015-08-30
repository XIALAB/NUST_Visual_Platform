from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import WangyiMusic

def show(request):
    song_menu = WangyiMusic.objects.order_by('-pnum')
    """
    paginator = Paginator(song_menu, 10)
    page = request.GET.get('page')
    try:
        menu = paginator.page(page)
    except PageNotAnInteger:
        menu = paginator.page(1)
    except EmptyPage:
        menu = paginator.page(paginator.num_pages)
    """
    return render(request, 'music/show.html',
            {
                'song_menu': song_menu,
            }
    )


