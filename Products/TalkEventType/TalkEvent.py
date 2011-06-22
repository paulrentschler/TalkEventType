"""Definition of the Talk Event content type
"""

from zope.interface import implements
from Products.Archetypes import atapi
from Products.ATContentTypes.content.event import ATEvent
#from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from Products.ATContentTypes.lib.historyaware import HistoryAwareMixin

from Products.TalkEventType import TalkEventTypeMessageFactory as _
from Products.TalkEventType.interfaces import ITalkEvent

#from Products.CMFCore.permissions import View, ModifyPortalContent
#from AccessControl import ClassSecurityInfo


TalkEventSchema = ATEvent.ATEventSchema.copy() + atapi.Schema((

    atapi.StringField(
        name = 'speakerInstitution',
        required = False,
        searchable = True,
        widget = atapi.StringWidget(
            label = _(u'Speaker\'s institution/affiliation'),
            label_msgid = 'TalkEventType_label_speakerInstitution',
            description = _(u'The full name of the institution, no abbreviations except for Penn State use "Penn State".'),
            i18n_domain = 'TalkEventType',
        ),
    ),
    
    atapi.BooleanField(
        name = 'eventCanceled',
        widget = atapi.BooleanWidget(
            label = _(u'The event has been canceled'),
            label_msgid = 'TalkEventType_label_eventCanceled',
            description = _('If the event is canceled, check this box and CHANGE NOTHING ELSE!'),
            i18n_domain = 'TalkEventType',
        )
    ),

),
)

# finalizeATCTSchema moves 'location' into 'categories', we move it back:
#TalkEvent_schema.changeSchemataForField('location', 'default')


class TalkEvent(ATEvent, HistoryAwareMixin):
    """A Talk Event"""
    implements(interfaces.ITalkEvent)


    meta_type = 'TalkEvent'
#    _at_rename_after_creation = True
    schema = TalkEventSchema
#    security = ClassSecurityInfo()

    # update the labels and descriptions of existing fields
    schema['title'].widget.label = 'Speaker\'s name'
    schema['title'].widget.description = 'NO PUNCTATION and NO SUFFIXES! e.g. Joanna A Bloggs'
    schema['eventUrl'].widget.description = 'Web address (url) with more info about the speaker. Use addresses starting http://'
    schema['location'].widget.description = 'Where will the talk take place?'
    schema['description'].widget.description = 'Enter the talk title here'
    schema['description'].default = 'Title to be announced'
    schema['text'].widget.label = 'Talk details'
    schema['text'].widget.description='If the speaker has an abstract, or there are special instructions for this talk, enter it here.'
    
    # move some fields around
    schema.moveField('eventCanceled', before = 'title')
    schema.moveField('speakerInstitution', after = 'title')
    schema.moveField('eventUrl', after = 'speakerInstitution')
    schema.moveField('location', after = 'description')
    
    # hide the attendees cause we don't use them
    schema['attendees'].widget.visible={'edit':'invisible', 'view':'invisible'}



atapi.registerType(TalkEvent, 'TalkEventType')