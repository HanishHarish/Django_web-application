from django.shortcuts import render,HttpResponse
from.models import employee

# Create your views here.
def home(request):
    # dt={'title':'Home_page',
    #      'content':'HOme content',
    #       'para':'sfhsjjfkjfklfaflffljfsk'}
    d={
        'tabledata':{'haresh':{'name':'Haresh','email':'hresh@gmail.com'},
        'naveen':{'name':'naven','email':'naveen@gmail.com'}}}
    return render(request,'home.html',d)

def save(request):
    e=employee()
    e.name="naveen"
    e.mobile="99999999"
    e.email="dabbuharish@109"
    e.address="nellore"
    e.save()
    return HttpResponse("not in ")
