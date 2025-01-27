"""Customizable settings."""

from django.conf import  settings

CHANGE_LINK_CLASS_DEFAULT = 'fa fa-pencil'
CHANGE_LINK_CLASS_REFERENCE = 'RELATION_LINKS_CHANGE_LINK_CLASS'
CHANGE_LINK_CLASS = getattr(
    settings, CHANGE_LINK_CLASS_REFERENCE, CHANGE_LINK_CLASS_DEFAULT
)


CHANGELIST_LINK_CLASS_DEFAULT = 'fa fa-eye'
CHANGELIST_LINK_CLASS_REFERENCE = 'RELATION_LINKS_CHANGELIST_CLASS'
CHANGELIST_LINK_CLASS = getattr(
    settings, CHANGELIST_LINK_CLASS_REFERENCE, CHANGELIST_LINK_CLASS_DEFAULT
)
