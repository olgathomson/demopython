from django.urls import reverse_lazy
from . models import Tasks
from django.shortcuts import render, redirect
from django .shortcuts import HttpResponse
from . forms import TodoForm
from django .views.generic import ListView
from django . views.generic . detail import DetailView
from django . views.generic.edit import UpdateView,DeleteView


class Tasklistview(ListView):
    model=Tasks
    template_name='home.html'
    context_object_name = 'task'
#     task is the key of value in dictionary.
# home.html is redirect page and model is Tasks.

class Taskdetailview(DetailView):
    model=Tasks
    template_name = 'detail.html'
    context_object_name = 'task'
#     task is the value in detail.html page.
# this is the detaile view.

class Taskupdateview(UpdateView):
    model=Tasks
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
         return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

# this is the update view..fields are used to update...
class Taskdeleteview(DeleteView):
    model=Tasks
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')
# this is the delete view
def add(request):
    task1 = Tasks.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Tasks(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task':task1})
# def detail(request):
#
#     return render(request,'detail.html',)
def delete(request, taskid):
    task=Tasks.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task=Tasks.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})









