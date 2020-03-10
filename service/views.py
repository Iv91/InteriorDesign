from django.shortcuts import render
from .models import Service, TeamMember
# Create your views here.
def home(request):
    teammembers = TeamMember.objects.all()
    services = Service.objects.all()
    return render(request, 'service/home.html', {'services':services, 'teammembers':teammembers})
