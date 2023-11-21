from django.shortcuts import render

# Create your views here.

# Create your views here.
def home(request):
    """
        home
    """
    return render(request, 'home/home.html')

def participation(request):
    """
        participation
    """
    return render(request, 'home/participation.html')
