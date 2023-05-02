from django.http import HttpResponse
from .models import Message


# Create your views here.

def homePageView(request):
	aId = request.GET.get("id")
	message = Message.objects.get(id = aId)

		
	return HttpResponse(message.content)
