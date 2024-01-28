
from django.shortcuts import render,HttpResponse

def fact(n):
    if n==0:
        return 1
    else :
        return n*fact(n-1)
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def calculate(request):
    if request.method=='POST':
        n=request.POST.get('inp')
        op=request.POST.get('operation')
        if op=='factorial':
           try:
               m=int(n)
               result=fact(m)
               context={'output':result}
               return render(request,'about.html',context)
           except ValueError:
              
          
              
            return HttpResponse('please enter a  valid number to find factorial!!')
        elif op=='reverse':
            result=str(n)[::-1]
            context={'output':result}
            return render(request,'about.html',context)
        
            
            
            
            
            
           
        
    else :
        return HttpResponse('please enter a valid number or a string!!')
    