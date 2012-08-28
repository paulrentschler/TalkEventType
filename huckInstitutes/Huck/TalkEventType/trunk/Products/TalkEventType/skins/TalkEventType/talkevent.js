/******************************************************************************
 * Written by: Paul Rentschler
 * Created on: 22 June 2011
 *
 * Description: Selectively hides the fields needed for indicating whether
 *               a talk event is canceled, postponed, or rescheduled.
 ******************************************************************************/


function determineAvailableOptions () {
  
  // see if there is a title provided
  if (jq("#archetypes-fieldname-title input#title").val() == "") {
    // the title is blank, we are probably adding, so hide all three choices
    jq("#archetypes-fieldname-eventCanceled").hide();
    jq("#archetypes-fieldname-eventPostponed").hide();
    jq("#archetypes-fieldname-rescheduledEvent").hide();
    
  } else {
    // the title is not blank, we are probably editing, show the check boxes
    jq("#archetypes-fieldname-eventCanceled").show();
    jq("#archetypes-fieldname-eventPostponed").show();
    
    // if postponed is checked, then show the rescheduling option
    if (!jq("#archetypes-fieldname-eventPostponed input").attr('checked')) {
      jq("#archetypes-fieldname-rescheduledEvent").hide();
    }
  }
  
}


jq(document).ready( function () {

  // see if we are on a talk event edit page
  if (jq("#talkevent-base-edit").length > 0) {
    // assign a change event to the postponed checkbox
    jq("#archetypes-fieldname-eventPostponed input").change( function () {
      if (jq("#archetypes-fieldname-eventPostponed input").attr('checked')) {
        jq("#archetypes-fieldname-rescheduledEvent").show();
      } else {
        // make sure the reference has been deleted
        if ((jq("#rescheduledEvent_label").val() != "No reference set. Click the add button to select."
          && jq("#rescheduledEvent_label").val() != "")
          && (jq("#ref_browser_rescheduledEvent_label").val() != "No reference set. Click the add button to select."
          && jq("#ref_browser_rescheduledEvent_label").val() != "")
        ) {
          // tell the user to delete the reference
          alert("If this event is no longer postponed, please clear the rescheduled event field by clicking the Remove Reference button.");
          jq("#archetypes-fieldname-eventPostponed input").attr('checked','checked');
        } else {
          jq("#archetypes-fieldname-rescheduledEvent").hide();
        }
      }
    });
    
    
    // determine which options should be shown
    determineAvailableOptions();
  }
  
});