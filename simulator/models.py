from django.db import models

# Create your models here.
class UserProfile(models.Model):
  user = models.OneToOneField(User)
  friends = models.ManyToMany(User)
  jobTitle = models.CharField(max_length=200)
  name = models.CharField(max_length=200)
  age = models.IntegerField()
  balance = models.IntegerField()
  expenditures = models.oneToMany(Expenditures)

  def __unicode__(self):
    return self.user.username

  def __str__(self):
    return self.user.username



class Expenditures(models.Model):
  date = models.DateField(_("Date"), default=datetime.date.today)
  balance = models.IntegerField()