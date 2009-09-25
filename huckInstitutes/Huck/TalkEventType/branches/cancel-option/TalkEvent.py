# -*- coding: utf-8 -*-
#
# File: TalkEvent.py
#
# Copyright (c) 2008 by []
# Generator: ArchGenXML Version 2.0
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """Catherine Williams"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces
from Products.ATContentTypes.content.event import ATEvent

from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.TalkEventType.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='speakerInstitution',
        searchable=True,
        widget=StringField._properties['widget'](
            label="Speaker's institution/affiliation",
            label_msgid='TalkEventType_label_speakerInstitution',
            i18n_domain='TalkEventType',
        ),
    ),
    
    BooleanField(
        name='eventCanceled',
        widget=BooleanWidget(
            label="The event has been canceled",
            label_msgid='TalkEventType_label_eventCanceled',
            i18n_domain='TalkEventType',
        )
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

TalkEvent_schema = getattr(ATEvent, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
finalizeATCTSchema(TalkEvent_schema)
# finalizeATCTSchema moves 'location' into 'categories', we move it back:
TalkEvent_schema.changeSchemataForField('location', 'default')
##/code-section after-schema

class TalkEvent(ATEvent):
    """
    """
    security = ClassSecurityInfo()
    implements(interfaces.ITalkEvent)

    meta_type = 'TalkEvent'
    _at_rename_after_creation = True

    schema = TalkEvent_schema

    ##code-section class-header #fill in your manual code here
    schema['title'].widget.label='Speaker name'
    schema['title'].widget.description='Enter the name of the speaker here, e.g. Joanna Bloggs'
    schema.moveField('eventCanceled',before='title')
    schema['eventCanceled'].widget.description='Check the box if the event has been canceled. DO NOT DELETE any information.'
    schema.moveField('speakerInstitution',after='title')
    schema['speakerInstitution'].widget.description='For example, Penn State or University of Michigan or Cambridge University, UK'
    schema.moveField('eventUrl',after='speakerInstitution')
    schema['eventUrl'].widget.description='Web address (url) with more info about the speaker. Use addresses starting http://'
    schema.moveField('location',after='description')
    schema['location'].widget.description='Where will the talk take place?'
    schema['description'].widget.description='Enter the talk title here'
    schema['description'].default='Title to be announced'
    schema['text'].widget.description='If the speaker has an abstract, or there are special instructions for this talk, enter it here.'
    schema['attendees'].widget.visible={'edit':'invisible','view':'invisible'}
    ##/code-section class-header

    # Methods

registerType(TalkEvent, PROJECTNAME)
# end of class TalkEvent

##code-section module-footer #fill in your manual code here
##/code-section module-footer



