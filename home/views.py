from django.shortcuts import render

def home(request):
    titulo = "ChatBot MHT"
    return render(request, "home.html", {'titulo': titulo})