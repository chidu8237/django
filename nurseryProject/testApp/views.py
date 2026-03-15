from django.shortcuts import render
import datetime

# Create your views here.
def dateinfo(request):
    date=datetime.datetime.now()
    name='chidu'
    h=int(date.strftime('%H'))
    if h<12:
        msg='Good Morning'
    elif h<16:
        msg='Good Afternoon'
    elif h<21:
        msg='Good Evening'
    else:
        msg='Good Night'
    my_dict={'date':date,'guest':name,'msg':msg}
    return render(request,'testApp/test.html',context=my_dict)
