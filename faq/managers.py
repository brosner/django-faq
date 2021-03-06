import datetime
from django.db import models
from django.db.models.query import QuerySet
import faq.enums as enums

class QuestionQuerySet(QuerySet):
    """
    A basic ''QuerySet'' subclass, provides query functionality and some
    helper methods for an intuitive interface.
    """

    def active(self, **kwargs):
        """
        A utility method that filters results based on ''Question'' models
        that are only ''Active''.
        """
        if kwargs.get('slug'):
            slug = kwargs['slug']
            return self.filter(status__exact=enums.STATUS_ACTIVE,
                               slug__exact=slug)
        else:
            return self.filter(status__exact=enums.STATUS_ACTIVE,)

class QuestionManager(models.Manager):
    """
    A basic ''Manager'' subclass which returns a ''QuestionQuerySet''.
    It provides simple access to helpful utility methods.
    """

    def get_query_set(self):
        return QuestionQuerySet(self.model)

    def active(self, slug=None):
        return self.get_query_set().active(slug=slug)
