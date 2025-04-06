from django.shortcuts import render

def load_message(request):
    return render(request, 'messages.html')

def index_view(request):
    return render(request, 'index.html')
