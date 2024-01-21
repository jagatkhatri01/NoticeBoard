from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Notice
from .forms import CRNoticeForm
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


def notice_detail(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    return render(request, 'notice_details.html', {'notice': notice})

def add_cr_notice(request):
    if request.user.is_authenticated and request.user.is_cr:
        if request.method == 'POST':
            form = CRNoticeForm(request.POST)
            if form.is_valid():
                notice = form.save(commit=False)
                notice.author = request.user
                notice.save()
                return redirect('notices')
        else:
            form = CRNoticeForm()
        return render(request, 'add_cr_notice.html', {'form': form})
    else:
        return redirect('login')

