from django.shortcuts import render

# Create your views here.

def addPageView(request):
	items = request.session.get('items', [])

	# Check if a new note was submitted through the form
	if request.method == 'POST':
		# Get the new note from the form data
		new_item = request.POST.get('content')

        # Add the new note to the list of notes
		items.append(new_item)

        # Save the updated list of notes in the session
		request.session['items'] = items
	
	if len(items) > 10:
		lst_indx = len(items)-1
		recent_items = []
		for i in range(10):
			recent_items.append(items[lst_indx])
			lst_indx -=1
		items = recent_items
	
	return render(request, 'pages/index.html', {'items' : items})


def erasePageView(request):
	request.session['items'] = []
	items = []

	return render(request, 'pages/index.html', {'items' : items})


def homePageView(request):
	# use sessions (the data is stored in a database db.sqlite that is then accessed using a cookie)
	items = request.session.get('items', [])

	if len(items) > 10:
		items = items[-10:]

	# shorter way of writing instead of loader
	return render(request, 'pages/index.html', {'items' : items})
