from django.contrib import admin
from django import forms
from django.shortcuts import render
from schedules.models import Template, Slot, Schedule, Assignment
import logging

class SlotInline( admin.TabularInline ):
    model = Slot

class TemplateAdmin( admin.ModelAdmin ):
    inlines = [ SlotInline ]

admin.site.register( Template, TemplateAdmin )
admin.site.register( Slot )
admin.site.register( Schedule )
admin.site.register( Assignment )
