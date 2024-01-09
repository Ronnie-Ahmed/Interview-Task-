from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import TaskDetails,UserDetails
from .forms import TaskForm,CreateTaskForm
from django.utils import timezone

# Create your views here.

def Home(request):
    Backlog = TaskDetails.objects.filter(phases__iexact="Backlog").select_related('user')
    ToDo = TaskDetails.objects.filter(phases__iexact="ToDo").select_related('user')
    Doing = TaskDetails.objects.filter(phases__iexact="Doing").select_related('user')
    Completion = TaskDetails.objects.filter(phases__iexact="Completion").select_related('user').order_by('-completed_at')
    Backlog_count=Backlog.count()
    ToDo_count=ToDo.count()
    Doing_count=Doing.count()
    Completion_count=Completion.count()
    Backlog.first=Backlog.first()
    ToDo.first=ToDo.first()
    Doing.first=Doing.first()
    Completion.first=Completion.first()
    if request.method=='POST':
        form=CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=CreateTaskForm()
    context={
        'Backlog':Backlog,
        'ToDo':ToDo,
        'Doing':Doing,
        'Completion':Completion,
        'Backlog_count': Backlog_count,
        'ToDo_count': ToDo_count,
        'Doing_count': Doing_count,
        'Completion_count': Completion_count,
        'Backlog_first':Backlog.first,
        'ToDo_first':ToDo.first,
        'Doing_first':Doing.first,
        'Completion_first':Completion.first,
        'form':form  
        
    }
    
   
    return render(request,'app/Home.html',context)


def editTask(request,pk):
    Task=TaskDetails.objects.get(id=pk)
    if request.method=='POST':
        form=TaskForm(request.POST,instance=Task)
        if form.is_valid():
            # data=form.cleaned_data['phases']
            # print(data)
            # if data=='Completion':
            #     Task.completed_at=timezone.now()
            #     Task.save()
            #     form.save()
            #     return redirect('/')
            form.save()
            return redirect('/')
    else:
        form=TaskForm(instance=Task)
    context={
        'form':form
    }
    return render(request,'app/editTask.html',context)



def makeComplete(request,pk):
    task=TaskDetails.objects.get(id=pk)
    
    tasks=TaskDetails.objects.filter(phases__iexact=task.phases)
    tasks.update(phases='Completion',completed_at=timezone.now()  + timezone.timedelta(hours=6))
    
    return redirect('/')
 
 
 
def deleteTask(request,pk):
     TaskDetails.objects.get(id=pk).delete()
     return redirect('/')
 
 
def markAsComplete(request,pk):
        task=TaskDetails.objects.get(id=pk)
        task.phases='Completion'
        task.save()
        return redirect('/')