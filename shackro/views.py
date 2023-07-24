from django.shortcuts import render
from .models import student


# Create your views here.
def home(request):
    data2 = student.objects.all()
    return render(request, 'home.html', {
        "di": data2
    })


def insert(request):
    if request.method == "post":
        name = request.POST.get('name')
        school = request.POST.get('school')
        theclass = request.POST.get('class')
        email = request.POST.get('email')
        number = request.POST.get('number')

        # print(name,school,theclass,email,number)

        data = student(name=name, school=school, theclass=theclass, email=email, number=number)
        data.save()
    return render(request, 'home.html')
