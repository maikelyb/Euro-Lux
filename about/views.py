from django.shortcuts import render
from .models import *

# Create your views here.

def about(request):
    about = About.objects.first()
    fact = Fact.objects.first()
    features = Feature.objects.all()
    
    context = {
        "about":about,
        "fact":fact,
        "features":features,
    }
    return render(request, 'about/about.html', context=context)
