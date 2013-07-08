from django.contrib import admin

from models import Profile
from models import Organization
from models import Opportunity
from models import Collaboration

admin.site.register(Profile)
admin.site.register(Organization)
admin.site.register(Opportunity)
admin.site.register(Collaboration)
