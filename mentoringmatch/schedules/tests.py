from django.test import TestCase
from whitelist.models import Mentor
from schedules.models import Template


class SchedulesTests( TestCase ):

    def test_overridden_template_unicode( self ):
        """Ensures the template unicode contains useful info"""
        template = Template( name="Some template" )
        self.assertNotEqual( str( template ), 'Template object' )
