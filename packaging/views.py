from django.shortcuts import render
from .models import Pack
# Create your views here.

def pack(request):
    packs = Pack.objects.all()
    context = {
        'packs': packs,
    }
    return render(request, 'packaging/pack.html', context=context)