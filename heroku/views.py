import django.shortcuts as render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})