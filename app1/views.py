from django.shortcuts import render

# Create your views here.
def operation1(request):
    d={'a':100,'b':20}
    return render(request,'if-else.html',d)
    