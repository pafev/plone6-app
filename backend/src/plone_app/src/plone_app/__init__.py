"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "plone_app"

_ = MessageFactory("plone_app")

logger = logging.getLogger("plone_app")
