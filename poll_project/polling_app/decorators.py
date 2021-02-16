from datetime import date
from functools import wraps

from django.shortcuts import Http404, get_object_or_404

from polling_app.models import Survey


def survey_available(func):
    """
    Checks if a survey is available (published and not expired). Use this as a decorator for view functions.
    """

    @wraps(func)
    def survey_check(self, request, *args, **kwargs):
        survey = get_object_or_404(
            Survey.objects.prefetch_related("related_question"), isPublished=True, id=kwargs["id"]
        )
        # if not survey.isPublished:
        #     raise Http404
        # if survey.expiryDate < date.today():
        #     raise Http404
        # if survey.publishDate > date.today():
        #     raise Http404
        return func(self, request, *args, **kwargs, survey=survey)

    return survey_check
