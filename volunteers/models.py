from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Day(models.Model):
    day = models.CharField(max_length=100)

    def __unicode__(self):
        return self.day


class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    hours_desired = models.CharField(max_length=100)

    def total_hours(self):
        return sum(self.task_set.all().values_list('hours', flat=True))

    def __unicode__(self):
        return self.name


class Task(models.Model):
    name = models.ForeignKey(Type)
    volunteers = models.ManyToManyField(Volunteer, blank=True)
    day = models.ForeignKey(Day)
    time = models.CharField(max_length=100)
    hours = models.DecimalField(max_digits=3, decimal_places=1)

    def __unicode__(self):
        return '%s %s %s %s' % (self.volunteers, self.name, self.time, self.day)


