from django.shortcuts import render

# Create your views here.
def home(request):
    data1 = {'name':{'1st':{'name':"Nikhil",'age':35},'2nd':"Ram",'3rd':"Raj"}}
    data2 = {'name':'Nikhil','age':37,'qualification':'B.com'}
    data3 = {'name':'Nikhil','age':37,'qualification':'B.com'}
    data4 = {'name':'Nikhil','age':37,'qualification':'B.com'}
    return render (request,'home.html',data2)
