from django.conf.global_settings import SESSION_FILE_PATH
from django.shortcuts import render

from dp43.settings import BASE_DIR


# Create your views here.
def set_session(request):
    request.session['name'] = 'manish'
    request.session['lname'] = 'sharma'
    return render(request, 'student/set_session.html')


def get_session(request):
    # name = request.session.get('name')
    # lname = request.session.get('lname')
    keys = request.session.keys()
    items = request.session.items()
    request.session.modified = True
    return render(request, 'student/get_session.html',{'keys':keys,'items':items})


def delete_session(request):
    request.session.flush()
    return render(request, 'student/del_session.html')



# file based session in django
#
# in settings.py
# SESSION_ENGINE = 'django.contrib.sessions.backend.file'
# SESSION_FILE_PATH = os.path.join(BASE_DIR,'folder_name')
