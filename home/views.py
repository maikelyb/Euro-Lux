from django.shortcuts import render
from .models import Carousel
from about import models as ab
# Create your views here.

def home(request):
    carousels = Carousel.objects.all()
    about = ab.About.objects.first()
    fact = ab.Fact.objects.last()
    feature = ab.Feature.objects.first()
    team = ab.Team_member.objects.all()
    testimonial = ab.Tesimonial.objects.all()
    
    context = {
        "carousels":carousels,
        "about":about,
        "fact":fact,
        "feature":feature,
        "team":team,
        "testimonial":testimonial       
        }
    
    return render(request,'home/home.html', context=context)
