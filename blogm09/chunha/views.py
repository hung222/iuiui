from django.http import HttpResponse
from django.template import loader
from .models import chunha

def index(request):
  mychunhas = mychunha.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mychunha': mychunha,
  }
  return HttpResponse(template.render(context, request))
