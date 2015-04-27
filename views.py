from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from .IltOAuthClient import IltOAuthClient as IOC
def run(request):
	if 'token' in request.GET and request.GET['token']:
		data = IOC.getData(request.GET['token'])
		if not data:
			return redirect(reverse('ilt_client:failed'))
		else:
			request.session['user_files'] = data
			if 'redirect' in request.session and request.session['redirect']:
				redirect_local_url = request.session['redirect']
				del request.session['redirect']
				return redirect(redirect_local_url)
			else:
				return redirect('/')
	else:
		return redirect(IOC.ilt_redirect_url)

def show(request):
	if 'user_files' in request.session:
		return JsonResponse(request.session['user_files'])
	else:
		return HttpResponse('user_files not defined')

from .config import *
def getData_failed(request):
	config = {
		'REDIRECT_URL': REDIRECT_URL, 
		'HOST_URL' : HOST_URL, 
		'CLIENT_KEY' : CLIENT_KEY, 
		'CLIENT_SECRET' : CLIENT_SECRET, 
		'SCOPE' : SCOPE, 
	}
	return render(request, 'ilt_client/getData_failed.html', {'config' : config})
