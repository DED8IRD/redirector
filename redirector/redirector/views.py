from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
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
				group = Group.objects.get(name='Linkers')
				user.groups.add(group)
				user.save()
				login(request, user)
			return redirect('URLshortener:index')

	return render(request, 'registration/register.html', {'form': ExtendedUserCreationForm()})