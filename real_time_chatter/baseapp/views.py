from django.shortcuts import render

def home_view(request):
    context = {}
    return render(request, 'baseapp/home.html', context)