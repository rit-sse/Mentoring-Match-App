from django.contrib import admin
from django import forms
from django.shortcuts import render
from schedules.models import Template, Slot, Schedule, Assignment
import logging


class TemplateAdmin( admin.ModelAdmin ):

    def add_view( self, request ):
        
        if not self.has_change_permission(request):
            raise PermissionDenied

        # Display from 8 AM to 8 PM (no label on end time)
        time_range = list( range( 8, 20 ) )

        def convert_time( time ):
            """Generates a label for a 24-hour time"""
            hour = time
            if hour % 12 == 0:
                hour = 12
            else:
                hour = hour % 12


            return str( hour ) +" "+ ( "AM" if time // 12 == 0 else "PM" )

        time_labels = map( convert_time, time_range )

        return render( request, 'admin/schedules/template/edit_form.html', { 
            'app_label': self.model._meta.app_label,
            'opts': self.model._meta,
            'change': False,
            'is_popup': '_popup' in request.REQUEST,
            'save_as': False,
            'has_add_permission': True,
            'has_delete_permission': False,
            'has_change_permission': True,
            'has_file_field': False,
            'has_absolute_url': False,
            'auto_populated_fields': (),
            'add': True,
            'time_range': time_range,
            'time_labels': time_labels,
        })


admin.site.register( Template, TemplateAdmin )
admin.site.register( Slot )
admin.site.register( Schedule )
admin.site.register( Assignment )
