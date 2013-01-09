import json
# Create your views here.
from people.models import Person
from django.shortcuts import render_to_response, redirect
from django.template import Context, loader
from django.http import HttpResponse
from django.core.context_processors import csrf

def render(r, template, context = {}):
    always = {
        'people': Person.objects.all()
    }
    context.update(csrf(r))
    context.update(always)
    return render_to_response(template, context)

def people(r):
    return render(r, 'people.jinja')

def manage_people(r):
    return render(r, 'manage_people.jinja')

def update_info(r, nickname):
    person = Person.objects.get(nickname=nickname)
    person.info = r.POST['info'];
    person.save()

    return HttpResponse(json.dumps(True), mimetype="application/json" )

def view_person(r, nickname):
    person = Person.objects.get(nickname=nickname)
    return render(r, 'view_person.jinja', {
        'person': person
    })

def edit_person(r):
    if(r.method == "GET"):
        return render(r, 'edit_person.jinja')
    elif(r.method == "POST"):
        p = Person(
            first_name=r.POST['fname'],
            last_name=r.POST['lname'],
            nickname=r.POST['nickname'],
            active=True,
            info=""
        )
        p.save()
        return redirect(people)

