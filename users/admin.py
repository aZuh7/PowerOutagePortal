
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from outages.models import OutageReport

'''
The OutageReportInline class is used to display the OutageReport model as an inline
in the User model admin page. This makes it easier for administrators and developers
to view OutageReports associated with a particular user.
'''
class OutageReportInline(admin.TabularInline):
    model = OutageReport
    extra = 0

'''
The CustomUserAdmin class is used to customize the Django admin panel view for administrators
and developers to have a graphical representation of the backend database by registering the User model to the admin site.
'''
class CustomUserAdmin(UserAdmin):
    model = User
    inlines = (OutageReportInline,)
    list_display = ('user_id', 'first_name', 'last_name', 'username', 'email', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'first_name', 'last_name', 'phone', 'address', 'zip')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser')}
        ),
    )
    search_fields = ('email', 'username')
    ordering = ('user_id',)

admin.site.register(User, CustomUserAdmin)

'''
The CustomOutageAdmin class is used to customize the Django admin panel view for administrators
and developers to view Outage Report objects stored on the database with a graphical representation by registering the OutageReport model to the admin site.
'''

class CustomOutageAdmin(admin.ModelAdmin):
    model = OutageReport
    list_display = ('report_id', 'user_id', 'report_date', 'location', 'zip_code', 'description', 'planned', 'estimated_restoration_time')
    list_filter = ('report_id', 'user_id', 'report_date', 'planned')

    search_fields = ('report_id', 'user_id', 'report_date')
    ordering = ('report_date',)

admin.site.register(OutageReport, CustomOutageAdmin)
