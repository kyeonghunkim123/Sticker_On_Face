from django.shortcuts import render

# Create your views here.
def h_list(request):
    return render(request, "board/h_list.html")


def h_register(request):
    return render(request, "board/h_register.html")