from django.db import models
from datetime import datetime

from django.contrib.auth.models import User

'''
class UserProfile(models.Model):
    departments = (
        ('Elearning', 'Elearning'),
        ('software', 'Software'),
        ('multimedia', 'Multimedia'),
        ('qa', 'QA'),
    )
    username = models.CharField(max_length=20)
    department = models.CharField(max_length=20,choices=departments)

    def __unicode__(self):
        return self.username   '''



class Clients(models.Model):
    clientname = models.CharField(max_length=20)

    def projects(self):
        return Projects .objects.filter(client=self)


    def __unicode__(self):
        return self. clientname


class Projects(models.Model):
    client = models.ForeignKey(Clients, related_name="projects_clint")
    projectname = models.CharField(max_length=20)

    def courses(self):
        return Courses .objects.filter(project=self)

    def __unicode__(self):
        return self.projectname

class Courses(models.Model):
    client = models.ForeignKey(Clients, related_name="projectsunderclint")
    project = models.ForeignKey(Projects, related_name="coursesunderprojects")
    coursename = models.CharField(max_length=20)

    def __unicode__(self):
        return self.coursename




class Department(models.Model):
     departments = (
        ('Elearning', 'Elearning'),
        ('software', 'Software'),
        ('multimedia', 'Multimedia'),
        ('qa', 'QA'),
        )

     department = models.CharField(max_length=20,choices=departments)


class User_Timesheet(models.Model):
    departments = (
        ('Elearning', 'Elearning'),
        ('software', 'Software'),
        ('multimedia', 'Multimedia'),
        ('qa', 'QA'),
        )

    TASK_CHOICES = (
        ('Fresh', 'FRESH'),
        ('Change Order', 'CHANGE ORDER'),
     )

    HOURS_CHOICES = (
        ('0', '00'),
        ('1', '01'),
        ('2', '02'),
        ('3', '03 '),
        ('4', '04'),
        ('5', '05 '),
        ('6', '06'),
        ('7', '07'),
        ('8', '08'),
        ('9', '09'),
     )
    MINUTES_CHOICES = (
        ('00', '00 m'),
        ('25', '25 m'),
        ('50', '50 m'),
        ('75', '75 m'),
        ('100', '100 m'),
    )

    date = models.DateField(default=datetime.now, editable=False)
    client = models.ForeignKey(Clients)
    project = models.ForeignKey(Projects)
    course = models.ForeignKey(Courses)
    department = models.CharField(max_length=20,choices=departments,null=True,default='software')
    task_description = models.CharField(max_length=50)
    task_type = models.CharField(max_length=20, choices=TASK_CHOICES,default='Fresh')
    effort_hours = models.CharField(max_length=10, choices=HOURS_CHOICES,default='0')
    effort_minutes = models.CharField(max_length=10, choices=MINUTES_CHOICES,default='00')


    def __unicode__(self):
        return '%s-%s' % (self.date, self.project)












