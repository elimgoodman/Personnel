# Create your views here.
from people.models import Person
from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import HttpResponse

def index(request):
    return render_to_response('index.jinja', {'foo': 2})

def people(request):
    people = Person.objects.all()
    return render_to_response('people.jinja', {'people': people})

def edit_person(request):
    return render_to_response('edit_person.jinja', {})
