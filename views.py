from django.shortcuts import render
data =[
    {'id':1,'name':'ram','age':40},
    {'id':2,'name':'sita','age':50},
    {'id':3,'name':'arjun','age':60},
]
def table(request):
    return render(request,'table.html',{'data':data})
