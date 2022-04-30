from django.shortcuts import redirect, render
from django.http import HttpResponse,Http404
# Create your views here.
from .models import questions,solution
from .forms import  solutionForm



def home(request):
    problems = questions.objects.all()
    context ={'problem': problems}
    return render(request,'home.html',context)


 

def problemDetail(request,questionId):
    problems = questions.objects.get(id=questionId)
    lang = ['C++', 'Python']
    
    context ={'problem': problems,
                'language':lang
     }

     
      
    return render(request, 'problemDetail.html', context)
   
def submit(request,questionId):
    langChoice = request.POST.get('langChoice', False);
    LangChoice = request.POST['langChoice']
    if LangChoice == 'c++':
        print("c++")
        #result=(request,questionId)
    if LangChoice == 'python':
        print('python')
       # result=(request,questionId)
   

    
    context = {
        #'output' : result,
    }
  
    return render(request, 'leaderboard.html', context)



