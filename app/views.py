from django.shortcuts import render
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from app.models import *
from django.urls import reverse_lazy
# Create your views here.

class home(View):
    def get(self,request):
        return render(request,'app1/home.html')

class School_list(ListView):

    template_name='app1/School_list.html'
    model=School
    context_object_name='schools'
    #ordering=['name']

class School_detail(DetailView):
    template_name='app1/School_detail.html'
    model=School
    context_object_name='schools'

class School_create(CreateView):
    template_name='app1/School_form.html'
    model=School
    fields='__all__'



class Student_create(CreateView):
    template_name='app1/Student_form.html'
    model=Student
    fields='__all__'

class School_update(UpdateView):
    template_name='app1/Student_form.html'
    model=School
    fields='__all__'

class School_delete(DeleteView):
    template_name='app1/School_confirm_delete.html'
    model=School
    context_object_name='schools'
    success_url=reverse_lazy('School_list')



    
    