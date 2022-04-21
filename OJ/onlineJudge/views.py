from django.shortcuts import render
from django.http import HttpResponse,Http404
# Create your views here.
from .models import questions



def home(request):
    problems = questions.objects.all()
    context ={'problem': problems}
    return render(request,'home.html',context)


 

def problemDetail(request,questionId):
    problems = questions.objects.get(id=questionId)
    
    context ={'problem': problems}
      
    return render(request, 'problemDetail.html', context)
   


