from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Notice
from django.db.models import Q

# Create your views here.
def noticesView(request):
    query = request.GET.get('search')
    notices = Notice.objects.order_by('-datetime')

    if query:
        # Filter notices based on search query
        notices = notices.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__icontains=query)
        )

    paginator = Paginator(notices, 5)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)
    context = {'notices':notices,
                'title':'College',
                'site_name':'Notices',
                'page_obj':page_obj,
                'search_query':query
                }
    return render(request, 'home.html', context)

