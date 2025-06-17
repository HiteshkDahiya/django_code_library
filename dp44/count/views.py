from django.shortcuts import render

# Create your views here.
def count(request):
    ct = request.session.get('count',0)
    new_count = ct + 1
    request.session['count'] = new_count
    return render(request,'count/count.html',{'count':new_count})


def cnt(request):
    return render(request,'count/practice.html')