from django.contrib import admin

from models import Volunteer, Task, Day, Type

# Register your models here.
admin.site.register(Volunteer)
admin.site.register(Task)
admin.site.register(Day)
admin.site.register(Type)