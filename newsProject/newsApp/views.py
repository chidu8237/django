from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'newsApp/index.html')

def moviesinfo(request):
    head_msg='Latest Movies Information'
    msg1='Kantara moive create a history'
    msg2='salman going to marriage soon'
    msg3='KGF3 are launching soon'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3,}
    return render(request,'newsApp/news.html',context=my_dict)

def sportsinfo(request):
    head_msg = 'Latest Sports Information'
    msg1 = 'Kohali gave Left and Right to Brodman Record'
    msg2 = 'MS Dhoni is playing the IPL 2026'
    msg3 = 'IPL starts from 28 march'
    my_dict = {'head_msg': head_msg, 'msg1': msg1, 'msg2': msg2, 'msg3': msg3, }
    return render(request,'newsApp/news.html',my_dict)

def politicsinfo(request):
    head_msg = 'Latest Politics Information'
    msg1 = 'In Maharashtra Elections will come just in 2 months'
    msg2 = 'Achhe Din Kab Ayenge!!!'
    msg3 = 'LPG Gas Price are so expensive'
    my_dict = {'head_msg': head_msg, 'msg1': msg1, 'msg2': msg2, 'msg3': msg3, }
    return render(request, 'newsApp/news.html', my_dict)
