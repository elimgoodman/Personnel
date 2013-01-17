import json, datetime
# Create your views here.
from people.models import Person, Entry, Feedback, Checkin
from django.shortcuts import render_to_response, redirect
from django.template import Context, loader
from django.http import HttpResponse
from django.core.context_processors import csrf

def render(r, template, context = {}):
    always = {
        'people': Person.objects.all().order_by('first_name')
    }
    context.update(csrf(r))
    context.update(always)
    return render_to_response(template, context)

def people(r):
    return render(r, 'manage_people.jinja')

def manage_people(r):
    return render(r, 'manage_people.jinja')

def update_info(r, nickname):
    person = Person.objects.get(nickname=nickname)
    person.info = r.POST['info'];
    person.save()

    return HttpResponse(json.dumps(True), mimetype="application/json" )

def feedback_communicated(r):
    feedback_id = r.POST['feedback_id']
    feedback = Feedback.objects.get(id=feedback_id)
    feedback.communicated = True
    feedback.communicated_on = datetime.datetime.now()
    feedback.save()

    return HttpResponse(json.dumps(True), mimetype="application/json" )

def feedback_closed_loop(r):
    feedback_id = r.POST['feedback_id']
    feedback = Feedback.objects.get(id=feedback_id)
    feedback.closed_loop = True
    feedback.closed_loop_on = datetime.datetime.now()
    feedback.save()

    return HttpResponse(json.dumps(True), mimetype="application/json" )

def journal(r, nickname):
    person = Person.objects.get(nickname=nickname)
    entries = Entry.objects.filter(subject=person).order_by('-created')

    return render(r, 'journal.jinja', {
        'person': person,
        'entries': entries
    })

def feedback(r, nickname):
    person = Person.objects.get(nickname=nickname)
    feedback = Feedback.objects.filter(recipient=person).order_by('-created')

    return render(r, 'feedback.jinja', {
        'person': person,
        'feedback': feedback
    })

def view_person(r, nickname):
    person = Person.objects.get(nickname=nickname)
    return render(r, 'view_person.jinja', {
        'person': person
    })

def add_entry(r, nickname):
    person = Person.objects.get(nickname=nickname)

    if(r.method == "GET"):
        return render(r, 'add_entry.jinja', {
            'person': person,
            'weeks': range(1, 10)
        })
    elif(r.method == "POST"):
        e = Entry(
            content=r.POST['content'],
            created=datetime.datetime.now(),
            updated=datetime.datetime.now(),
            subject=person
        )
        e.save()

        fs = get_json(r, 'feedback');
        for f in fs:
            fdbk = Feedback(
                content = f['content'],
                originator = person,
                recipient_id = f['recipient'],
                entered_with = e,
                created=datetime.datetime.now(),
                updated=datetime.datetime.now()
            )
            fdbk.save()

        cs = get_json(r, 'check_ins')
        for c in cs:
            ci = Checkin(
                content = c['content'],
                recipient = person,
                entered_with = e,
                check_in_on = datetime.datetime.now() + datetime.timedelta(weeks=int(c['weeks'])),
                created=datetime.datetime.now(),
                updated=datetime.datetime.now()
            )
            ci.save()

        return redirect("/people/%s/journal" % (person.nickname))

def get_json(r, param):
    if(r.POST[param]):
        return json.loads(r.POST[param])
    else:
        return []

def edit_person(r, nickname):
    p = Person.objects.get(nickname=nickname)

    if(r.method == "GET"):
        return render(r, 'edit_person.jinja', {
            'person': p
        })
    elif(r.method == "POST"):
        p.first_name=r.POST['fname']
        p.last_name=r.POST['lname']
        p.nickname=r.POST['nickname']

        p.save()
        return redirect(people)
def add_person(r):
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

def checked_in(r):
    checkin_id = r.POST['checkin_id']
    c = Checkin.objects.get(id=checkin_id)
    c.checked_in = True
    c.checked_in_on = datetime.datetime.now()
    c.save()

    return HttpResponse(json.dumps(True), mimetype="application/json" )

