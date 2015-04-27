def need_iltlogin(func):
	def login(request):
		if 'user_files' in request.session:
			return func(request)
		else:
			request.session['redirect'] = request.path
			return redirect('ilt_client:run')
	return login