from django.shortcuts import render, redirect
from collection.models import Thing
from collection.forms import ThingForm
# Create your views here.
# def index(request):
# 	#defining a variable
# 	number = 9
# 	thing = "Thing name"
# 	#this is our new def def view
# 	return render(request, 'index.html', {'number':number,})

# def index(request):
# 	number = 6
# 	# Dont forget the quotes because its a string,
# 	# Not an interger
# 	thing = "Thing name"
# 	return render(request, 'index.html',{
# 		'number':number,
# 		#Donot forget to pass it in tand the last comma
# 		'thing':thing,


def index(request):
	things = Thing.objects.all()
	return render(request, "index.html", {
		'things':things,
	})

def thing_detail(request, slug):
	#grab the object...
	thing = Thing.objects.get(slug=slug)


	# and pass to the template 
	return render(request, 'things/thing_detail.html', {
	'thing': thing,
	})

def edit_thing(request, slug):
	#grab the object
	thing = Thing.objects.get(slug=slug)
	#set the form we're Using
	form_class = ThingForm


	#if we're coming to this view from a submited format
	if request.method == 'POST':
		#grab the data from the submitted form and apply to the form
		form = form_class(data=request.POST, instance=thing)
		if form.is_valid():
			#save the new data
			form.save()
			return redirect('thing_detail', slug=thing.slug)
	# otherwise just create the form
	else:
		form = form_class(instance=thing)

	#and render the template
	return render(request, 'things/edit_thing.html', {
		'thing': thing,
		'form': form,
	}) 