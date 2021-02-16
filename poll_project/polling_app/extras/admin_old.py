from django.contrib import admin,messages
from django.utils.translation import ngettext
#from .models import Category,Response,Respondent
from polling_app.models.survey import Survey
from polling_app.models.question import Question
#from .models import SurveyQuestion
from polling_app.views import export_view
import nested_admin
admin.site.site_header = 'Fraunhofer Survey Administration'
admin.site.site_title = 'Smart Surveys'
admin.site.index_title = 'Welcome to the Smart Survey Website'
# Register your models here.


#class CategoryInline(admin.TabularInline):
    #model = Category

# class QuestionInline(nested_admin.NestedStackedInline):
#     model = Question
#     extra = 1
    
#admin.site.register(Category,CategoryAdmin)
# class SurveyQuestionInline(nested_admin.NestedStackedInline):
#     model = SurveyQuestion
#     sortable_field_name = "ID"
#     inlines = ['QuestionInline']

# class SurveyAdmin(admin.ModelAdmin):
#     list_display = ['name','isPublished','publishDate','relatedQuestion']
#     #sortable_field_name = "ID"
#     ordering = ['name']
#     #inlines = ['SurveyQuestionInline']
    # def make_published(self,request,queryset):
    #     updated=queryset.update(isPublished=1)
    #     self.message_user(request,ngettext(
    #         '%d survey was successfully marked as published.',
    #         '%d surveys were successfully marked as published.',
    #         updated,
    #         )% updated,messages.SUCCESS)
    # make_published.short_description = "Mark selected surveys as published"

    # def make_unpublished(self,request,queryset):
    #     updated=queryset.update(isPublished=0)
    #     self.message_user(request,ngettext(
    #         '%d survey was successfully marked as unpublished.',
    #         '%d surveys were successfully marked as unpublished.',
    #         updated,
    #         )% updated,messages.SUCCESS)
    # make_unpublished.short_description = "Mark selected surveys as unpublished"

    # actions = [make_published,make_unpublished,export_view]
# admin.site.register(Survey,SurveyAdmin)



#class ResponseInline(admin.StackedInline):
   # list_display = ("respondent_id", "survey_id","age",)
    #readonly_fields = ("question",)
    #extra = 0
    #model = Response

#class RespondentAdmin(admin.ModelAdmin):
    #fields = ("age", "location","gender")
    #list_filter = ("survey", "created")
    #date_hierarchy = "created"
    #inlines = [ResponseInline]
    # specifies the order as well as which fields to act on
    #readonly_fields = ("survey", "created", "updated", "interview_uuid", "user")

# class ResponseAdmin(admin.ModelAdmin):
#     model=Response
#     readonly_fields =('interview_id',)
# admin.site.register(Response, ResponseAdmin)



