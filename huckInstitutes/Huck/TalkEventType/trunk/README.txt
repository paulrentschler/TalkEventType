Description

    A Plone product to provide a Plone 3.x compatible content type
      for representing an event where a speaker gives a talk.

Installation

    On the file system:
        - Place the product in the src/Products.TalkEventType directory
           of your Zope instance.
        - Edit your buildout.cfg file and add Products.TalkEventType to
           the eggs= directive and add src/Products.TalkEventType to the
           develop= directive
        - Rerun buildout (suggest: ./bin/buildout -N)
        - Start your Plone instance

    In the Plone Web Interface:
        - As portal manager, go to 'Portal > Site Setup > Add-on Products'.
        - Select 'Talk Event Type' and click the *Install* button.

    Uninstall -- Can be done from the same page.

Written by

    Paul Rentschler <par117@psu.edu>