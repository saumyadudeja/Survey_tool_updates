from django.contrib import admin,messages
from django.utils.translation import ngettext
from polling_app.models.survey import Survey
from polling_app.models.question import Question
from polling_app.models.category import Category
from polling_app.models.answerOption import AnswerOption
import nested_admin
from polling_app.views import export_view as export

admin.site.site_header = "Fraunhofer's Survey Creation Tool"
admin.site.site_title = 'Surveys'
admin.site.index_title = "Welcome"

class SurveyQuestionInline(admin.TabularInline):
    model = Survey.related_question.through

class QuestionInline(admin.ModelAdmin):
    inlines = [SurveyQuestionInline,]
    exclude = ('related_question')

class SurveyAdmin(admin.ModelAdmin):
    list_display = ['name','isPublished','publishDate']
    sortable_field_name = "ID"
    ordering = ['name']
    exclude = ('related_question',)
    inlines = [
        SurveyQuestionInline,
        ]
    def make_published(self,request,queryset):
        updated=queryset.update(isPublished=1)
        self.message_user(request,ngettext(
            '%d survey was successfully marked as published.',
            '%d surveys were successfully marked as published.',
            updated,
            )% updated,messages.SUCCESS)
    make_published.short_description = "Mark selected surveys as published"

    def make_unpublished(self,request,queryset):
        updated=queryset.update(isPublished=0)
        self.message_user(request,ngettext(
            '%d survey was successfully marked as unpublished.',
            '%d surveys were successfully marked as unpublished.',
            updated,
            )% updated,messages.SUCCESS)
    make_unpublished.short_description = "Mark selected surveys as unpublished"

    actions = [make_published,make_unpublished,export]

admin.site.register(Survey,SurveyAdmin)

class AnswerOptionInline(nested_admin.NestedStackedInline):
    model = AnswerOption
    extra = 0


class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    extra = 0
    inlines = [AnswerOptionInline,]


class CategoryAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionInline,]

admin.site.register(Category,CategoryAdmin)

#class ResponseAdmin():


