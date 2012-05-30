from django.test import TestCase
from django.core.exceptions import ValidationError
from whitelist.models import Mentor
from schedules.models import Template, Slot, Schedule, Assignment
from datetime import datetime

class TemplateTests( TestCase ):
    """Tests schedules.models.Template"""

    def setUp( self ):
        self.template = Template( name="Some template" )

    def test_overridden_unicode( self ):
        """Ensures the unicode method isn't the default"""
        self.assertNotEqual( str( self.template ), 'Template object' )

    def test_name_exists_valid( self ):
        """Ensures that a template that contains only a name is valid.

        No exception should be thrown.
        """
        self.template.full_clean()

    def test_name_missing_invalid( self ):
        """Ensures that a template that is missing a name should be invalid

        No exception should be thrown.
        """
        self.template.name = None
        with self.assertRaises( ValidationError ):
            self.template.full_clean()


class SlotTests( TestCase ):
    """Tests schedules.models.Slot"""

    def setUp( self ):
        self.pattern = Template.objects.create( name="Some template" )
        self.begin, self.finish = datetime.now(), datetime.now()
        self.slot = Slot( template=self.pattern, 
            start=self.begin, end=self.finish, day="MON" )

    def test_overridden_unicode( self ):
        """Ensures the slot unicode is not default"""
        self.assertNotEqual( str( self.slot ), 'Slot object' )

    def test_allfields_valid( self ):
        """Tests that a Slot with all fields is valid.
        
        No exception should be thrown"""
        self.slot.full_clean()

    def test_template_missing_invalid( self ):
        """Tests that a Slot with no template is invalid"""
        with self.assertRaises( ValueError ):
            self.slot.template = None

    def test_start_missing_invalid( self ):
        """Tests that a Slot with no start time is invalid"""
        self.slot.start = None
        with self.assertRaises( ValidationError ):
            self.slot.full_clean()

    def test_end_missing_invalid( self ):
        """Tests that a Slot with no end time is invalid"""
        self.slot.end = None
        with self.assertRaises( ValidationError ):
            self.slot.full_clean()

    def test_end_missing_invalid( self ):
        """Tests that a Slot with no day is invalid"""
        self.slot.day = None
        with self.assertRaises( ValidationError ):
            self.slot.full_clean()


class ScheduleTests( TestCase ):
    """Tests schedules.models.Schedule"""

    def setUp( self ):
        self.pattern = Template.objects.create( name="Some template" )
        self.begin, self.finish = datetime.now(), datetime.now()
        self.sched = Schedule( template=self.pattern,
            start=self.begin, end=self.finish )
    
    def test_overridden_unicode( self ):
        """Ensures the schedule unicode is not default"""
        self.assertNotEqual( str( self.sched ), 'Schedule object' )

    def test_template_missing_invalid( self ):
        """Tests that a Schedule with no template is invalid"""
        with self.assertRaises( ValueError ):
            self.sched.template = None

    def test_start_missing_invalid( self ):
        """Tests that a Schedule with no start time is invalid"""
        self.sched.start = None
        with self.assertRaises( ValidationError ):
            self.sched.full_clean()

    def test_end_missing_invalid( self ):
        """Tests that a Schedule with no end time is invalid"""
        self.sched.end = None
        with self.assertRaises( ValidationError ):
            self.sched.full_clean()


class AssignmentTests( TestCase ):
    """Tests schedules.models.Assignment"""

    def setUp( self ):
        self.person = Mentor.objects.create( dce="abc1234",
            first_name="Bob", last_name="Smith" )
        self.pattern = Template.objects.create( name="Some template" )
        self.begin, self.finish = datetime.now(), datetime.now()
        self.sched = Schedule( template=self.pattern,
            start=self.begin, end=self.finish )
        self.place = Slot( template=self.pattern,
            start=self.begin, end=self.finish, day="MON" )

        self.assignment = Assignment( mentor=self.person,
            slot=self.place, schedule=self.sched )

    def test_overridden_unicode( self ):
        """Ensures the assignment unicode is not default"""
        self.assertNotEqual( str( self.assignment ), 'Schedule object' )

    def test_mentor_missing_invalid( self ):
        """Tests that a Schedule with no template is invalid"""
        with self.assertRaises( ValueError ):
            self.assignment.mentor = None

    def test_slot_missing_invalid( self ):
        """Tests that a Schedule with no template is invalid"""
        with self.assertRaises( ValueError ):
            self.assignment.slot = None

    def test_schedule_missing_invalid( self ):
        """Tests that a Schedule with no template is invalid"""
        with self.assertRaises( ValueError ):
            self.assignment.schedule = None
