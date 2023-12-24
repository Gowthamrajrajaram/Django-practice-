from django.shortcuts import render

# Create your views here.
#cookies
'''def cookies_count(request):
    count=request.COOKIES.get('count',0)
    total_count=int(count)+1
    response= render(request, 'app/cookies.html' ,{'count':total_count})
    response.set_cookie('count',total_count)
    return response'''

#session

def cookies_count(request):
    count=request.session.get('count',0)
    total_count=int(count)+1
    request.session['count']=total_count
    print(request.session.get_expiry_date())
    return render(request, 'app/cookies.html' ,{'count':total_count})