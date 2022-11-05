from django.contrib import admin
from app.models import UsersData
from app.models import Reports
from app.models import ReportStates
from app.models import ReportTypesToAccept
from app.models import ReportTypes


admin.site.register(UsersData)
admin.site.register(Reports)
admin.site.register(ReportStates)
admin.site.register(ReportTypesToAccept)
admin.site.register(ReportTypes)
