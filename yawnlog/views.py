# Django imports
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response
# Yawnlog imports
from yawnlog.models import *
# Python imports
from datetime import datetime, timedelta

########################################
# Application information
########################################

## Multi-app views

@login_required()
def dashboard(request):
    """
    Home screen, allows posting a sleep, and shows the basic graphs. 
    Messages (will) show up here.
    yawnlog.com/sleeps
    """
    # TODO find user_id via request (login) for arb user via request.?, not just my account


    # Sleeps list
    last_sleeps = Sleeps.objects.filter(user_id=2).order_by('stop').reverse().all()[:7]

    return render_to_reponse('interface/home.html', {
            'last_sleeps': last_sleeps,


        }

def sleep_submit(request):
    """
    Store a sleep. Where a form posts. Should make abstract-ish as an API.
    """
    # TODO modify Sleeps to allow for reporting IP
    # TODO set this up for authentication (via request?)

    if request.method == 'POST':
        #sleep.VALUE = request.POST.get('POST_VALUE', 'OR_THIS')

        # check if sleep.start is before sleep.stop and < 24 hrs


        sleeps.start = request.POST.get('start', '')
        sleeps.stop = request.POST.get('stop', '')

        if sleeps.stop < sleeps.start:
            # flipflop start/stop
            sleeps.start = request.POST.get('stop', '')
            sleeps.stop = request.POST.get('start', '')


        if (sleeps.stop - sleeps.start) < timedelta (days = 1):
            # make sure the sleep is less than 24 hours

            sleeps.zip = request.POST.get('zip', '')
            sleeps.note = request.POST.get('note', '')
            sleeps.quality = request.POST.get('quality', '3')
            sleeps.user_id = request.POST.get('user_id', '')

            sleeps.reporter_ip = request.META['REMOTE_ADDR']
            sleeps.created_at = datetime.now()
            sleeps.save()
            
        else:
            # don't save it?
            pass

    # TODO: choose return template
    return render_to_response('TEMPLATE??', {})






"""
    queryset = []
    for package in packages:
        q = Crashreport.objects.filter(app_package__name=package).all()
        [queryset.append(x) for x in q]
    if len(queryset) is 0:
        hashes_list = []
    else:
        hashes = [(r.stacktrace.trace_hash_short, r.stacktrace.stacktrace) for r in queryset]
        hash_set = set(hashes)
        hashes_list = []
        for tuple in hash_set:
            hashes_list.append((tuple[0], tuple[1], hashes.count(tuple)))

    return render_to_response('interface/dashboard.html', {
            'hashes': hashes_list,
            'reports': queryset,

            # Metadata
            'user': user,
            'cat': 'dash',
            'packages': packages,
            'gravatar': hashlib.md5(request.user.email.lower()).hexdigest()
        })
"""
