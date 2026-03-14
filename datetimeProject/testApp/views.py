from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def datetimeinfo(request):
    date=datetime.datetime.now()
    h=int(date.strftime("%H"))
    msg='<h1>Hello Chidu Very '
    if h<12:
        msg=msg+'Good Marning'
    elif h<16:
        msg=msg+'Good Afternoon'
    elif h<21:
        msg=msg+'Good Evening'
    else:
        msg=msg+'Good Night!'
    msg=msg+'</h1><hr>'
    msg=msg+'<h1>Now server Time is:'+str(date)+'</h1>'
    return HttpResponse(msg)