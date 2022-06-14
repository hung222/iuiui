from django.http import HttpResponse
from django.template import loader
from .models import chunha

def index(request):
  mydata = chunha.objects.filter.values()
  template = loader.get_template('index.html')
  context = {
    'mychunha': mydata,
  }
  return HttpResponse(template.render(context, request))
