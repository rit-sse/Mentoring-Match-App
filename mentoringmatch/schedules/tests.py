from django.test import TestCase
from whitelist.models import Mentor
from schedules.models import Template, Slot, Schedule, Assignment
from datetime import datetime

class SchedulesOutputTests( TestCase ):

    def test_overridden_template_unicode( self ):
        """Ensures the template unicode contains useful info"""
        template = Template( name="Some template" )
        self.assertNotEqual( str( template ), 'Template object' )


    def test_overridden_slot_unicode( self ):
        """Ensures the slot unicode is not default"""
        pattern = Template.objects.create( name="Some template" )
        begin, finish = datetime.now(), datetime.now()

        slot = Slot( template=pattern, start=begin, end=finish, day="MON" )

        self.assertNotEqual( str( slot ), 'Slot object' )

    
    def test_overridden_schedule_unicode( self ):
        """Ensures the schedule unicode is not default"""

        pattern = Template.objects.create( name="Some template" )
        begin, finish = datetime.now(), datetime.now()

        sched = Schedule( template=pattern, start=begin, end=finish )

        self.assertNotEqual( str( sched ), 'Schedule object' )


    def test_overridden_assignment_unicode( self ):
        """Ensures the assignment unicode is not default"""

        person = Mentor.objects.create( dce="abc1234",
            first_name="Bob", last_name="Smith" )
        pattern = Template.objects.create( name="Some template" )
        begin, finish = datetime.now(), datetime.now()
        place = Slot( template=pattern, start=begin, end=finish, day="MON" )
        sched = Schedule( template=pattern, start=begin, end=finish )

        assignment = Assignment( mentor=person, slot=place, schedule=sched )

        self.assertNotEqual( str( assignment ), 'Schedule object' )

