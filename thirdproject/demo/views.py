from django.shortcuts import render
import datetime
# Create your views here.

def display(request):
    date=datetime.datetime.now()
    name="Gowthamraj"
    date_dict={'display_date': date,'ownername':name}
    return render(request, 'app/index.html',context =date_dict)
