from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from .models import Park


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'userprofiles'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )


class ParkAdmin(admin.ModelAdmin):
    exclude = ('official', 'special','washroom', 'advisory', 'rating')
    fields = ('name','lat_long','size', 'address', 'neighbourhood', 'nurl', 'problems')


admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Park, ParkAdmin)
admin.site.register(User, UserAdmin)
