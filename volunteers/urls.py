
from django.conf.urls import url, include
from views import volunteers, addvolunteer, editvolunteer, task, edittask, addtask, deletetask, masterschedule, addday, \
    deletevolunteer, login, invalid_login, loggedin, logout, auth_view

urlpatterns = [
    url(r'^$', volunteers, name='volunteers'),
    url(r'^volunteers/$', volunteers, name="volunteers"),
    url(r'^volunteers/add/$', addvolunteer, name="addvolunteer"),
    url(r'^volunteers/edit/(?P<volunteer_id>[0-9]+)/$', editvolunteer, name="editvolunteer"),
    url(r'^volunteers/delete/(?P<volunteer_id>[0-9]+)/$', deletevolunteer, name="deletevolunteer"),
    url(r'^tasks/$', task, name="task"),
    url(r'^tasks/add/$', addtask, name="addtask"),
    url(r'^tasks/edit/(?P<task_id>[0-9]+)/$', edittask, name="editask"),
    url(r'^tasks/delete/(?P<task_id>[0-9]+)/$', deletetask, name="deletetask"),
    url(r'^home/$', volunteers, name="volunteers"),
    url(r'^schedule/$', masterschedule, name="masterschedule"),
    url(r'^days/add/$', addday, name="addday"),
    url(r'^days/$', addday, name="adday"),
    url(r'^accounts/login/$', login, name="login"),
    url('^', include('django.contrib.auth.urls')),
    url(r'^accounts/auth/$', auth_view, name="authview"),
    url(r'^accounts/logout/$', logout, name="logout"),
    url(r'^accounts/loggedin/$', loggedin, name="loggedin"),
    url(r'^accounts/invalid/$', invalid_login, name="invalidlogin"),
]
