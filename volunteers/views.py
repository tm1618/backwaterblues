from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, render_to_response, RequestContext
from models import Volunteer, Task, Day, Type
from django.db.models import Sum, F
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from forms import TaskForm, VolunteerForm, DayForm

# Create your views here.

@login_required
def volunteers(request):

    volunteer = Volunteer.objects.all()

    return render(request, 'volunteers.html', locals())


@login_required
def addvolunteer(request):
    if request.POST:
            form = VolunteerForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Volunteer added!')
                return HttpResponseRedirect('/volunteers/')
    else:
        form = VolunteerForm()

    return render(request, 'addvolunteer.html', locals())


@login_required
def editvolunteer(request, volunteer_id):
    vol = get_object_or_404(Volunteer, pk=volunteer_id)
    t = "Edit"
    tasks = Task.objects.filter(volunteers__id=volunteer_id)

    if request.POST:
        form = VolunteerForm(request.POST, instance=vol)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated!')
            return HttpResponseRedirect('/volunteers/')

    else:
        form = VolunteerForm(instance=vol)

    return render_to_response("editvolunteer.html", {
        'form': form,
        't': t,
        'vol': vol,
        'tasks': tasks,
    }, context_instance=RequestContext(request))


@login_required
def deletevolunteer(request, volunteer_id):
    vol = get_object_or_404(Volunteer, pk=volunteer_id).delete()

    messages.success(request, 'Volunteer Removed!')
    return render(request, 'removed.html', locals())


@login_required
def task(request):

    tasks = Task.objects.all().order_by('time')

    return render(request, 'tasks.html', locals())


@login_required
def addtask(request):
    if request.POST:
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Task added!')
                return HttpResponseRedirect('/tasks/')
    else:
        form = TaskForm()

    return render(request, 'addtask.html', locals())


@login_required
def edittask(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    volunteers = Task.objects.filter(volunteers=task_id)
    t = "Edit"

    if request.POST:
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated!')
            return HttpResponseRedirect('/schedule/')

    else:
        form = TaskForm(instance=task)

    return render_to_response("edittask.html", {
        'form': form,
        't': t,
        'task': task,
        'volunteers': volunteers,
    }, context_instance=RequestContext(request))


@login_required
def deletetask(request, task_id):
    task = get_object_or_404(Task, pk=task_id).delete()

    messages.success(request, 'Task Removed!')
    return render(request, 'removed.html', locals())


@login_required
def addday(request):
    days = Day.objects.all()
    if request.POST:
            form = DayForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Day added!')
                return HttpResponseRedirect('/days/')
    else:
        form = DayForm()

    return render(request, 'addday.html', locals())


@login_required
def masterschedule(request):
    volunteers = Volunteer.objects.all()
    fridaysetup = Task.objects.filter(day=1, name=3)
    fridaydance = Task.objects.filter(day=1, name=2)
    fridaybreakdown = Task.objects.filter(day=1, name=4)
    saturdaymorningsetup = Task.objects.filter(day=2, name=3)
    saturdaymorning = Task.objects.filter(day=2, name=1)
    saturdayafternoon = Task.objects.filter(day=3, name=1)
    saturdaydancesetup = Task.objects.filter(day=4, name=3)
    saturdaydance = Task.objects.filter(day=4, name=2)
    saturdaybreakdown = Task.objects.filter(day=4, name=4)
    sundaymorningsetup = Task.objects.filter(day=5, name=3)
    sundaymorning = Task.objects.filter(day=5, name=1)
    sundayafternoon = Task.objects.filter(day=6, name=1)
    sundaynight = Task.objects.filter(day=7, name=2)
    sundaybreakdown = Task.objects.filter(day=7, name=4)

    return render(request, 'schedule.html', locals())


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)


def auth_view(request):
    username = request.POST.get("username", '')
    password = request.POST.get("password", '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/volunteers/')
    else:
        return HttpResponseRedirect('/accounts/invalid')


@login_required
def loggedin(request):
    return render_to_response('loggedin.html',
                              {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')


@login_required
def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

