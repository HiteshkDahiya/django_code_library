from django.shortcuts import render
from .forms import UserEditForm
from django.contrib.auth.decorators import login_required

@login_required
def enroll(request):
    user = request.user
    if request.method == "POST":
        fm = UserEditForm(request.POST, instance=user)
        if fm.is_valid():
            fm.save()
    else:
        fm = UserEditForm(instance=user)

    return render(request, 'enroll/enroll.html', {'form': fm})
