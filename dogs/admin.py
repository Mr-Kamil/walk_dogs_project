from django.contrib import admin
from .models import *

admin.site.register(Dog)
admin.site.register(Owner)
admin.site.register(Walker)
admin.site.register(Walk)
