from django.db import models

class Status(models.Model):
    msg = models.CharField(max_length=255)

    def __unicode__(self):
        return u"{}".format(self.msg)
