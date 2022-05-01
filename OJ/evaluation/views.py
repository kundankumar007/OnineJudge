from django.shortcuts import render
from onlineJudge.models import questions,testCase,verdict
import os
import subprocess
import sys
from datetime import datetime

def evaluationPython(request,variableId):
    testCases = testCase.objects.filter(questions__id = variableId)
    code = request.POST['solution']
    for inputs in testCases:

        input = testCases.testcase
        expectedOutput = testCases.output
        try:
            with open("sol.py") as file:
                 file.write(code)
            output = subprocess.run([sys.executable, 'temp.py'], capture_output=True, text=True, input=input, check=True, timeout=1)
            actualOutput = output.stdout
            if(output.returncode!=0):
                verdict = verdict.COMPILATION_ERROR
            elif (actualOutput == expectedOutput):
                verdict = verdict.AC
            elif subprocess.TimeoutExpired:
                verdict= verdict.TLE
            else:
                verdict = verdict.WA
            

        except Exception as e:

            return e
        verdict(
            problemId = questions.objects.get(pk = variableId),
            verdict = verdict,
            submittedAt = datetime.now
            


        ).save()

        return verdict



        

        
           

       

    

