from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    body = RichTextField(null=True, blank=True, features=['bold','italic','link','stock'])

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
