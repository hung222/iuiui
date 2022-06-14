from django.http import HttpResponse
from django.template import loader
from .models import chunhas

def index(request):
  chunha = chunha.objects.filter(firstname='Emil').values()
  template = loader.get_template('index.html')
  context = {
    'mychunhas': mychunhas,
  }
  return HttpResponse(template.render(context, request))
