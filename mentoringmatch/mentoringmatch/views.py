from django.shortcuts import render_to_response
import datetime

def index(request):
    return render_to_response('base.html', {
        'title': 'SSE Mentoring Match',
    })
