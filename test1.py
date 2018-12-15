from django.http import HttpResoponse


def index(request):
	return HttpResponse("idnex")
