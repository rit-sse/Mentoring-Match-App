from whitelist.models import Mentor
from django.contrib import admin

class MentorAdmin(admin.ModelAdmin):
  #Rearrange fields in the administrative panel
  fields = ['first_name', 'last_name', 'dce']
  #List fields in the admin listing nicely
  list_display = ('dce', 'first_name', 'last_name')
  search_fields = ['dce', 'first_name', 'last_name']

admin.site.register(Mentor, MentorAdmin)
