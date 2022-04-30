from django.db import models

# Create your models here.
class questions(models.Model):
   
    difficulty = (('EASY', 'Easy'), ('MEDIUM', 'Medium'), ('HARD', 'Hard'))
    questionName = models.CharField(max_length=200)
    questionStatement = models.TextField()
    difficulty= models.CharField(max_length=10, choices=difficulty)
    tags = models.CharField(max_length=100)
  

class testCase(models.Model):
    problemId = models.ForeignKey(questions, on_delete=models.CASCADE)
    testcase = models.TextField()
    output = models.TextField()

class solution(models.Model):
    problemId = models.ForeignKey(questions, on_delete=models.CASCADE)
    code = models.TextField()
    verdict = models.CharField(max_length=25)
    submitted_at = models.DateTimeField('Submission Time',auto_now_add=True)

class verdict(models.Model):
    Verdict = (
        ('AC','success'),
        ('TLE','timeLimitExceeded'),
        ('WA','wrongAnswer'),
        ('COMPILATION_ERROR','compilationError')
    )
    verdict = models.CharField(max_length = 30,choices = Verdict,default = 'WA')
    submittedAt = models.DateTimeField('Submission Time',auto_now_add=True)
    problemId = models.ForeignKey(questions,on_delete = models.CASCADE)
    