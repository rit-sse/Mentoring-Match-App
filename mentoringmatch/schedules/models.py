from django.db import models
from whitelist.models import Mentor


class Template( models.Model ):
    """Defines the layout of slots for any particular week.

    For example, a "normal week" template may exist for most of the weeks in
    the academic quarter, and a separate "finals week" template could account
    for special scheduling during finals week.
    """
    
    name = models.CharField( max_length=30 )

    def __unicode__( self ):
        return self.name


class Slot( models.Model ):
    """Represents a single time slot in the mentoring schedule. 

    Example: One time slot may be on Tuesday, 10 AM to 12 PM
    """

    DAY_CHOICES = (
        (0, 'Sunday'),
        (1, 'Monday'),
        (3, 'Tuesday'),
        (4, 'Wednesday'),
        (5, 'Thursday'),
        (6, 'Friday'),
        (7, 'Saturday'),
    )

    day = models.IntegerField( max_length=3, choices=DAY_CHOICES )
    start = models.TimeField()
    end = models.TimeField()
    template = models.ForeignKey( Template )

    def __unicode__( self ):
        params = {
            'day': self.get_day_display(),
            'start': self.start,
            'end': self.end
        }
        return "%(day)s - %(start)s to %(end)s" % params


class Schedule( models.Model ):
    """Applies a template to a range of weeks.
    
    Each week contained in the date range will have the slots defined in the
    associated template.
    """

    start = models.DateField()
    end = models.DateField()
    template = models.ForeignKey( Template )

    def __unicode__( self ):
        params = {
            'template': self.template,
            'start': self.start,
            'end': self.end
        }
        return "%(template)s - %(start)s to %(end)s" % params

            
class Assignment( models.Model ):
    """Associates a mentor with a specific slot within a session"""

    mentor = models.ForeignKey( Mentor )
    slot = models.ForeignKey( Slot )
    schedule = models.ForeignKey( Schedule )

    def __unicode__( self ):
        params = {
            'first': self.mentor.first_name,
            'last': self.mentor.last_name,
            'slot': self.slot,
        }
        return "%(first)s %(last)s - %(slot)s" % params
