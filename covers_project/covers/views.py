from django.shortcuts import render

def home(request):
	# Home displaying top covers on all time 
	""" show youtbe link ? 
	ask the user questions about their idol and show the atrists on the 
	home scrren depending on that ? """
	return render(request, 'covers/home.html')

def about(request):
	return render(request, 'covers/about.html', {'title': 'About'})

def artists_list(request):
	# Artists list route 
	return render(request, 'covers/artists.html', {'title': 'Artists'})


def artist_profile(request):
	return render(request, 'covers/artist.html', {'title': 'Artist Profile'})

# def login(request):
	# Plan 
	'''for thoes how wanna comment or share their own covers link
	and in the future an account for the artists him/her self ''' 
	# return render(request, 'covers/login.html', {'title':'login.html'})

# def logout(request):
	# redirect to main page 

