from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    info = models.TextField()
    next_notes = models.TextField()
    active = models.BooleanField(default=True)
    
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    def pending_feedback(self):
        return Feedback.objects.filter(
            recipient=self, 
            communicated=False,
            closed_loop=False
        )

    def communicated_feedback(self):
        return Feedback.objects.filter(
            originator=self, 
            communicated=True,
            closed_loop=False
        )

    def get_url(self):
        return "/people/%s" % (self.nickname)
    
    def has_things_to_address(self):
        return bool(self.pending_feedback()) or bool(self.communicated_feedback())
    
class Entry(models.Model):
    content = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    subject = models.ForeignKey(Person)
    
    def feedback(self):
        return Feedback.objects.filter(entered_with=self)

class Feedback(models.Model):
    content = models.TextField()
    originator = models.ForeignKey(Person, related_name="feedback_given")
    recipient = models.ForeignKey(Person, related_name="feedback_recieved")
    communicated = models.BooleanField(default=False)
    communicated_on = models.DateTimeField(null=True)
    closed_loop = models.BooleanField(default=False)
    closed_loop_on = models.DateTimeField(null=True)
    entered_with = models.ForeignKey(Entry)
    created = models.DateTimeField()
    updated = models.DateTimeField()
