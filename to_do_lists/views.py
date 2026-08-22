from django.shortcuts import render

def index(request):

    context = {}
    return render(request, 'to_do_lists/index.html', context)
