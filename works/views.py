from django.shortcuts import render, get_object_or_404
from .models import Work

# Create your views here.
def home_view(request):
    works = Work.objects
    return render(request, 'works/home.html', {'works': works})


def work_view(request, work_id):
    work_detail = get_object_or_404(Work, pk=work_id)
    return render(request, 'works/detail.html' , {'work':work_detail})