from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Please, add a number to the path to check</h1>")

def odd_or_even(request, n):
    try:
        result = "EVEN" if int(n) % 2==0 else "ODD"
        return HttpResponse(f"<h1 style='text-align:center;'>{n} is <span style='color:blue'>{result}</span></h1>")
    except ValueError:
        return HttpResponse("Please, enter only digit value.")