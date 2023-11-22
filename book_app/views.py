from django.http import HttpResponse
from django.shortcuts import render
from.models import book
from django.db.models import Q
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
        return HttpResponse('BOOK added successfully')
    elif request.method == "GET":
        return render(request,"add.html")
    else:
        return HttpResponse("An exception occurred employee not added")


def remove_book(request):
    if request.method == "POST":
        b_name = request.POST['b_name']
        b1 = book.objects.all()
        if b_name:
            b1 = b1.filter(b_name__icontains=b_name)
            b1.delete()
        return HttpResponse("BOOK REMOVED")
        return render(request, "view.html")
    b1 = book.objects.all()
    context = {
        'b1': b1
    }
    return render(request, "remove.html", context)

def filter_book(request):
    if request.method=="POST":
        b_name=request.POST['b_name']
        a_name = request.POST['a_name']
        b1=book.objects.all()
        if b_name:
            b1=b1.filter(Q(b_name__icontains=b_name))
        if a_name:
            b1 = b1.filter(Q(a_name__icontains=a_name))
        contents={
            'b1':b1
        }
        return render(request,'view.html',contents)
    elif request.method=="GET":
        return render(request,"filter.html")
    else:
        return HttpResponse("INVALID INFORMATION")

