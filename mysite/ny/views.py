import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "ny/index.html", {
        "ny": now.month == 7 and now.day == 5
    })