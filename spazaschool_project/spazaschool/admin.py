from django.contrib import admin
from models import User, City, Module, ModuleSection, Question, Answer, \
    UserQuestion, Badge, UserBadge, PageCopy

admin.site.register(User)
admin.site.register(City)
admin.site.register(Module)
admin.site.register(ModuleSection)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserQuestion)
admin.site.register(Badge)
admin.site.register(UserBadge)
admin.site.register(PageCopy)



