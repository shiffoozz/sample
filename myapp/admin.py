from django.contrib import admin

from myapp.models import ComplaintTable, FeedbackTable, NotificationTable, StaffTable, UserTable, WorkTable

# Register your models here.

admin.site.register(UserTable)
admin.site.register(StaffTable)
admin.site.register(FeedbackTable)
admin.site.register(NotificationTable)
admin.site.register(WorkTable)
admin.site.register(ComplaintTable)
