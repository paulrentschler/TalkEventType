"""Definition of the Talk Event content type
"""

from zope.interface import implements
from Products.Archetypes import atapi
from Products.ATContentTypes.content.event import ATEvent
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
from Products.Relations.field import RelationField
from Products.ATContentTypes.lib.historyaware import HistoryAwareMixin

from Products.TalkEventType import TalkEventTypeMessageFactory as _
from Products.TalkEventType.interfaces import ITalkEvent

from Products.CMFCore.permissions import View, ModifyPortalContent
from AccessControl import ClassSecurityInfo


TalkEventSchema = ATEvent.schema.copy() + atapi.Schema((

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
            description = _(u'If the event is canceled, check this box and CHANGE NOTHING ELSE!'),
            i18n_domain = 'TalkEventType',
        )
    ),
    
    atapi.BooleanField(
        name = 'eventPostponed',
        widget = atapi.BooleanWidget(
            label = _(u'The event has been postponed'),
            label_msgid = 'TalkEventType_label_eventPostponed',
            description = _(u'If the event is postponed and will be rescheduled, check this box and CHANGE NOTHING ELSE!'),
            i18n_domain = 'TalkEventType',
        )
    ),

    RelationField(
        name = 'rescheduledEvent',
        required = False,
        searchable = False,
        widget = ReferenceBrowserWidget(
            label = _(u'Rescheduled event'),
            description = _(u'Click the Add button and find the NEW event that is replacing this one.'),
            base_query = "_search_talk_events",
            allow_browse = 1,
            allow_search = 1,
            show_results_without_query = 1,
            startup_directory_method = "_get_events_path",
        ),
        allowed_types = ('TalkEvent'),
        multiValued = False,
        relationship = 'TalkEventRescheduledEvent',
    ),

),
)

# finalizeATCTSchema moves 'location' into 'categories', we move it back:
#TalkEvent_schema.changeSchemataForField('location', 'default')


class TalkEvent(ATEvent, HistoryAwareMixin):
    """A Talk Event"""
    implements(ITalkEvent)


    meta_type = 'TalkEvent'
    _at_rename_after_creation = True
    schema = TalkEventSchema
    security = ClassSecurityInfo()

    # update the labels and descriptions of existing fields
    schema['title'].widget.label = 'Speaker\'s name'
    schema['title'].widget.description = 'NO PUNCTATION and NO SUFFIXES! e.g. Joanna A Bloggs'
    schema['eventUrl'].widget.description = 'Web address (url) with more info about the speaker. Use addresses starting http://'
    schema['location'].widget.description = 'Where will the talk take place?'
    schema['description'].widget.description = 'Enter the talk title here'
    schema['description'].default = 'Title to be announced'
    schema['text'].widget.label = 'Talk details'
    schema['text'].widget.description = 'If the speaker has an abstract, or there are special instructions for this talk, enter it here.'
    schema['contactName'].widget.description = 'Who should people contact if they have questions about the talk or want to meet the speaker?'
    schema['contactPhone'].widget.description = 'Format: ###-###-####  e.g. 814-555-1212'
    
    # add a validator to the contact e-mail and phone number
    #schema['contactEmail'].validators = ('isEmail',)   <-- TypeError: 'tuple' object is not callable
    #schema['contactPhone'].validators = 'isUSPhoneNumber'  <-- TypeError: 'str' object is not callable
    
    # move some fields around
    schema.moveField('eventCanceled', before = 'title')
    schema.moveField('speakerInstitution', after = 'title')
    schema.moveField('eventUrl', after = 'speakerInstitution')
    schema.moveField('location', after = 'description')
    
    # hide the attendees cause we don't use them
    schema['attendees'].widget.visible={'edit':'invisible', 'view':'invisible'}


    def getRescheduledEvent(self):
        """Returns the referenced event that replaces this one
           """
        return self.getReferences(relationship='TalkEventRescheduledEvent')


    ###
    # Methods to limit the referenceBrowserWidget start directory and search results    
    security.declareProtected(ModifyPortalContent, '_get_events_path')
    def _get_events_path(self):
        """Return the path to the object's parent
           """
        return '/'.join(self.getPhysicalPath())

    security.declareProtected(ModifyPortalContent, '_search_talk_events')
    def _search_talk_events(self):
        """Return a query dictionary to limit the search parameters for a reference browser
           widget query. Search only for TalkEvents.
           """
        return {'portal_type': 'TalkEvent',
                'sort_on': 'sortable_title'}



atapi.registerType(TalkEvent, 'TalkEventType')