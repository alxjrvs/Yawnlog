from django.db import models

# TODO: import more as needed from yawnlog-rails/app/models/

class Sleep(models.Model):
    """
    Sleep stores two times, that go forward in time and don't overlap other sleep times for that user.
    Also doesn't go over 86400 seconds (1 day).
    """
    #TODO: Make functions that sanitize data for the above things
    user_owner = ForeignKey(User)

    sleep_start = models.DateTimeField()
    sleep_stop = models.DateTimeField()
    duration = models.IntegerField() #calculated

    quality = models.CharField(max_length=5) #foreignkey
    #{"5 - Serene" => 5, "4 - Restful" => 4, "3 - Okay" => 3, "2 - Restless" => 2, "1 - Abysmal" => 1, " "=>" "}

    def __unicode__(self):
        return self.user_owner + '
        return u'%s slept %s hours' %(self.user_owner, self.duration)

class Profile(models.Model):
    """
    A one-to-one relationship to the User model, extending data defined for user.
    """
    user = models.ForeignKey(User, unique=True)
    gravatar = models.URLField(blank=True) # Profile glitter

class Friend(models.Model):
    """
    I think this is a graph database, with foreign keys to each user who have friended.
    Request is accepted = F, and notifies user_2. User_1 is the initiator.
    """
    # TODO: check if user_2 (not you) exists.
    user_1 = models.ForeignKey(User)
    user_2 = models.ForeignKey(User)
    is_accepted = models.BooleanField()
