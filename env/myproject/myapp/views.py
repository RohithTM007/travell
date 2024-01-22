from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def dayout(request):
    return render(request,'dayout.html')
def entertainment(request):
    return render(request,'entertainment.html')
def houseboat(request):
    return render(request,'houseboat.html')
def resort(request):
    return render(request,'resort.html')
def tour(request):
    return render(request,'tour.html')


