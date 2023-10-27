from django.http import HttpResponse
from django.shortcuts import render
from.models import book
def index(request):
    return render(request, 'wel.html')

def view_book(request):
    b1=book.objects.all()
    content={
        'b1':b1
    }
    print(content)
    return render(request,'view.html',content)

def add_book(request):
    if request.method=="POST":
        b_name = request.POST["book_name"]
        a_name = request.POST['author_name']
        cost = int(request.POST['cost'])
        new_book=book(b_name=b_name,a_name=a_name,cost=cost)
        new_book.save()
        return HttpResponse('Employee added successfully')
    elif request.method == "GET":
        return render(request,"add.html")
    else:
        return HttpResponse("An exception occurred employee not added")


def remove_book(request):
    return HttpResponse("EMPLOYEE REMOVED")

def filter_book(request):
    return render(request,'filter.html')
