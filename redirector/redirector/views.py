from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import ExtendedUserCreationForm

def register(request):
	if request.method == 'POST':
		form = ExtendedUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.clean_password2()
			user = authenticate(username=username, password=password)
			if user:
				login(request, user)
			return redirect('URLshortener:index')

	return render(request, 'registration/register.html', {'form': ExtendedUserCreationForm()})