from django.db import models

class sleep(models.Model):
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
