from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('problem/<str:questionId>/',views.problemDetail,name='problemDetails'),
    path('problem/<str:questionId>/submit',views.submit,name='submit')
  

]