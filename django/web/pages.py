from django.http import HttpResponse
import django.template

def index(request):
    t = django.template.loader.get_template('test.html')
    c = django.template.Context({})
    return HttpResponse(t.render(c))
