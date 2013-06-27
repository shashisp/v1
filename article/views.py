from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context


def hello(request):
	name = "Shashi Essp"
	html = "<html><body> Hi %s, This seems to have worked </body></html>" %name
	return HttpResponse(html)