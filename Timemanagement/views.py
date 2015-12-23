from django.shortcuts import render,HttpResponseRedirect,HttpResponse,render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from django.contrib.auth.models import User
from.models import *
from .forms import *


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def home(request):
    user_data = User.objects.all()
    clients_data = Clients.objects.all()
    project_data = Projects.objects.filter(client = clients_data)
    course_data = Courses.objects.filter(client = clients_data)
    timesheet_data = User_Timesheet.objects.filter()
    return render_to_response('home.html',{'user': request.user,'UserData':user_data,'ProjectData':project_data,'ClientData':clients_data,'CourseData':course_data,'UserTimesheet':timesheet_data})

def user_statustimesheet(request):
    if request.method == 'POST':
        form = User_TimesheetForm(request.POST)
        if form.is_valid():
            user_status = User_Timesheet.objects.create(
            client = form.cleaned_data['client'],
            project = form.cleaned_data['project'],
            course = form.cleaned_data['course'],
            department = form.cleaned_data['department'],
            task_description = form.cleaned_data['task_description'],
            task_type = form.cleaned_data['task_type'],
            effort_hours = form.cleaned_data['effort_hours'],
            effort_minutes = form.cleaned_data['effort_minutes']
            )
            user_status.save()
            return HttpResponseRedirect('/home')
    else:
        form = User_TimesheetForm()
    return render(request,"userstatus.html",locals())

def create_user(request):
    if request.method  == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password1']
            )
            user.save()
            return HttpResponseRedirect('/home')
    else:
        form = UserProfileForm()
    return render(request, 'createuser.html', locals())


def create_client(request):
    if request.method  == 'POST':
        form = ClientsForm(request.POST)
        if form.is_valid():
            clients = Clients.objects.create(
            clientname = form.cleaned_data['clientname'])
            return HttpResponseRedirect('/home')
    else:

        form = ClientsForm()
    return render(request, 'createclint.html', locals())


@csrf_exempt
def create_project(request):
    if request.method  == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            projects = Projects.objects.create(
            projectname = form.cleaned_data['projectname'],
            client = form.cleaned_data['client'],)
            return HttpResponseRedirect('/home')

    else:
        form = ProjectForm()
    return render(request, 'createproject.html', locals())


@csrf_exempt
def create_course(request,id = None):
    clients = Clients.objects.all()
    projects =  Projects.objects.filter(client = clients)
    if request.method  == 'POST':
        form = CourseForm(request.POST)
        print "hi"
        if form.is_valid():

            courses = Courses.objects.create(
                client = form.cleaned_data['client'],
                project = form.cleaned_data['project'],
                coursename = form.cleaned_data['coursename'],
            )
            return HttpResponseRedirect('/home')
    else:
        form = CourseForm()
    return render(request, 'createcourse.html',{'form':form,'clients':clients,'projects':projects})


@csrf_exempt
def p_ajax(request, id = None):
    clint_id = request.POST['varclientid']

    html_string = "<option value="">projects</option>"

    projects = Projects .objects.filter(client = clint_id)
    for  p in projects:
        #s =  s + '<option value=" '+ p.id +' ">' + p.projectname + '</option>'
        #s =  s + '<option value=" ">' + p.projectname + '</option>'
        html_string += '<option value="%s">%s</option>' % (p.pk, p.projectname)


    return HttpResponse(html_string)

