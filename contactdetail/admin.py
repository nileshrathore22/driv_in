from django.contrib import admin
from contactdetail.models import Contactform
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=('username','usermail','usersubject','usermessage','usersubject')
admin.site.register(Contactform,ContactAdmin)
