from django.contrib import admin
from sessions.models import *

admin.site.register( Template )
admin.site.register( Slot )
admin.site.register( Schedule )
admin.site.register( Assignment )
