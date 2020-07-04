from django.shortcuts import render
from .models import ToolBox

def index(request):
    tools = ToolBox.objects.all()
    context = {"tools" : tools}
    return render(request, "toolbox/main.html", context)