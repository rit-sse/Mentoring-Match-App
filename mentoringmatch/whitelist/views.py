from whitelist.forms import LoginForm
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def login(request):
  if request.method == 'POST':  #if the form has been submitted
    form = None
  else:
    form = LoginForm()
      
  csrfContext = RequestContext(request, {'form': form,})  
  return render_to_response('whitelist/login.html', csrfContext)
