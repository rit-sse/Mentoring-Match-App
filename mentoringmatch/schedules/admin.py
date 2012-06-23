from django.contrib import admin
from django import forms
from django.shortcuts import render
from schedules.models import Template, Slot, Schedule, Assignment
import logging


class SlotInline( admin.TabularInline ):
    """Enables inline editing of template slots"""
    model = Slot


class TemplateAdmin( admin.ModelAdmin ):
    """Configures SlotInline for the Template admin page"""
    inlines = [ SlotInline ]


class AssignmentInline( admin.TabularInline ):
    """Enables inline editing of assignments in a schedule"""
    model = Assignment


class ScheduleAdmin( admin.ModelAdmin ):
    """Configures the AssignmentInline on the Schedule admin page"""
    inlines = [ AssignmentInline ]

admin.site.register( Template, TemplateAdmin )
admin.site.register( Slot )
admin.site.register( Schedule, ScheduleAdmin )
admin.site.register( Assignment )
