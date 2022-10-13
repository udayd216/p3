from django.shortcuts import render

# Create your views here.
def app_uday(request):
    dict={'name':'uday'}
    return render(request,'app.html',context=dict)