from django.shortcuts import redirect, render
from django.http import HttpResponse,Http404

from .models import questions,solution,testCase,verdict

import os
import subprocess
import sys
from datetime import datetime


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


def evaluationPython(request,variableId):
    testCases = testCase.objects.filter(questions__id = variableId)
    code = request.POST['solution']
   
    input = testCases.testcase
    expectedOutput = testCases.output
    savePath ='D:\OnlineJudge\OJ\code'
    nameOfFile= 'sol'
    completeName =os.path.join(savePath,nameOfFile+".py")
    file =open(completeName,'w') 
    file.write(solution)
    file.close()
    cmd=[sys.executable, 'sol.py']
       
    try:
            output = subprocess.run(cmd, capture_output=True,shell =True, text=True, input=input, check=True, timeout=1)
           
           
         
            actualOutput = output.stdout
            if(output.returncode!=0):
                print('compilation_error')
                return HttpResponse('compilation error')
            elif(output.returncode==0):
                 print('all is well')
                 return HttpResponse('sucessfully compiled')

    except Exception as e:
            print(e)

def evaluationCpp(request,variableId):
    testCases = testCase.objects.filter(questions__id = variableId)
    code = request.POST['solution']
    

    input = testCases.testcase
    expectedOutput = testCases.output
    savePath ='D:\OnlineJudge\OJ\code'
    nameOfFile= 'sol'
    completeName =os.path.join(savePath,nameOfFile+".cpp")
    file =open(completeName,'w') 
    file.write(code)
    file.close()
    cmd =['g++','sol.cpp','-o','a.out']

    try:
            output = subprocess.run(cmd, capture_output=True, Shell =True,text=True, input=input, check=True, timeout=1)
            actualOutput = output.stdout
            if(output.returncode!=0):
                print('compilation_error')
                return HttpResponse('compilation error')
            elif(output.returncode==0):
                 print('all is well')
                 return HttpResponse('sucessfully compiled')
          
    except Exception as e:
             return e
 







   
def submit(request,questionId):
    result=''
    if request.method== 'POST':
         LangChoice = request.POST['langChoice'] 
    try:

        if LangChoice == 'c++':
            result = evaluationCpp(request,questionId)
                
        elif LangChoice == 'python':
                result = evaluationPython(request,questionId)
    except Exception as e:
        return e
    context ={
        'output': result
    }
   
  
    return render(request, 'leaderboard.html', context)







