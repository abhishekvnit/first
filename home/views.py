from django.shortcuts import render

# Create your views here.
from home.models import TalcherDirect

from django.db.models import Q

from datetime import date, timedelta

def index(request):

    talcherdb= TalcherDirect.objects.all()
    return render(request, 'index.html', {'talcherdb':talcherdb})

def milestone(request):
   

    talcherdb= TalcherDirect.objects.filter(activity='MIL')
    
    return render(request, 'milestone.html', {'talcherdb':talcherdb})

def civil(request):
   

    talcherdb= TalcherDirect.objects.filter(activity='CIV')
    
    return render(request, 'civil.html', {'talcherdb':talcherdb})

def erection(request):
   

    talcherdb= TalcherDirect.objects.filter(Q(activity='ERC') | Q(activity ='COM'))
    
    return render(request, 'civil.html', {'talcherdb':talcherdb})


def ordering(request):
   

    talcherdb= TalcherDirect.objects.filter(Q(activity='ORD') | Q(activity ='ENQ'))
    
    return render(request, 'civil.html', {'talcherdb':talcherdb})


def sixmonth(request):
   

    startdate= date.today()
    enddate= startdate+ timedelta(days=240)

    

    talcherdb= TalcherDirect.objects.filter(finish__range= [startdate,enddate])

    
    
    return render(request, 'civil.html', {'talcherdb':talcherdb})