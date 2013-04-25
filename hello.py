#!/usr/bin/python


from datetime import date
from flask import Flask, url_for, Markup, render_template
from markdown import markdown
content = {}


app = Flask(__name__)
box_bg = lambda filename: lambda: url_for('static', filename=('img/box/' + filename))
dl = lambda filename: lambda: url_for('static', filename=('pdfs/' + filename))


# SITE CONTENT # SITE CONTENT # SITE CONTENT # SITE CONTENT #

title = "Calama Consulting"


content['calama'] = """
Calama Consulting
=================

_Never Stop Innovating_

"""


content['who_we_are'] = """
The solar photovoltaic industry thrives on innovation. The potential for PV in
the world is huge, but so are the challenges. In the race to integrate solar as
a major player of our sustainable energy mix those companies who do not
innovate will be left behind; as long as the industry relies on unsustainable
government subsidies, there can be no status-quo.

Calama Consulting is a solar systems consulting firm committed to continual
innovation, and specializes in developing customized solutions for its clients.

"""


content['products'] = """
Products
--------
Calama specializes in monitoring and maintaining PV systems. All of our services are focussed ensuring the maximum output from a PV system.


"""

boxes = (
    dict(
        name='Consulting',
        id='consulting',
        description=Markup(markdown('''
Calma consulting services pring the latest knowledge from industry and academia to bear on your PV project. We focus on:

 *  Resoursce evaluation campaingn design, and design and maintenance of custom data aquisition
 *  PV resource data evaluation and selection of appropriate metrological data
 *  PV system design and optimization
 *  PV system evaluation and performance monitoring
 *  Sytem troubleshooting and loss analysis

        ''')),
        background=box_bg('frames.png'),
    ),
    dict(
        name='Frames',
        id='frames',
        description='''The frames program centralilzes performance evaluation, maintenance control and PV portfolio management into a powerful, intuative interface
        This program is currently under development, and we are actively seeking beta testers for this package.''',
        background=box_bg('frames.png'),
    ),
    dict(
        name='Aerial Inspection',
        id='helicopters',
        description='''Calama Aerial inspection services allow for efficeint identification of unerperforming panels in large scale PV arrays.
        This innovative inspection technique is a  low cost solution for identifying underperforming PV panels in large scale PV arrays.  ''',
        background=box_bg('helicopters.png'),
    ),
    
)


content['research'] = """
Research
--------

"""

researches = (
    dict(
        title='Improved parametric empirical determination of module short circuit current for modelling and optimization of solar photovoltaic systems',
        authors='R. W. Andrews, A. Pollard, and J. M. Pearce' ,
        journal='Solar Energy',
        date=date(2012, 10, 1),
        id='short-circuit-current',
        download=dl('I_sc_Prediction_arxiv.pdf'),
    ),
    dict(
        title='The effects of snowfall on solar photovoltaic performance',
        authors='R. W. Andrews, A. Pollard, and J. M. Pearce',
        date=date(2013, 2, 1),
        id='snowfall',
        download=dl('Snow_Paper_Submission_open_access.pdf'),
    ),
    dict(
        title='Prediction of energy effects on photovoltaic systems due to snowfall events',
        authors='R. W. Andrews and J. M. Pearce',
        date=date(2012, 7, 1),
        id='snowfall-prediction',
        download=None,
    ),
    dict(
        title='The effect of spectral albedo on amorphous silicon and crystalline silicon solar photovoltaic device performance',
        authors='R. W. Andrews and J. M. Pearce',
        date=date(2013, 3, 1),
        id='spec-albedo',
        download=dl('Snow_albedo_open_access.pdf'),
    ),
    dict(
        title='A new method to determine the effects of hydrodynamic surface coatings on the snow shedding effectiveness of solar photovoltaic modules',
        authors='R. W. Andrews, A. Pollard, and J. M. Pearce',
        date=date(2013, 6, 1),
        id='hydrodynamic',
        download=None,
    ),
    dict(
        title='Model of Loss Mechanisms for Low Optical Concentration on Solar Photovoltaic Arrays with Planar Reflectors',
        authors='R. W. Andrews, N. Alazzam, and J. M. Pearce',
        date=date(2011, 6, 1),
        id='loss-mechanisms',
        download=None,
    ),
    dict(
        title='Environmental and economic assessment of a greenhouse waste heat exchange',
        authors='R. W. Andrews, and J. M. Pearce',
        date=date(2011, 9, 1),
        id='waste-heat-exchange-assessment',
        download=None,
    ),
)


content['people'] = """
People
------

*   ### Rob Andrews

    Rob Andrews, the Principle Investigator and Director of Calama is currently
    pursing a doctorate in photovoltaic system design and optimization which is
    unique within the industry. He is published in major academic journals, and
    is an active member of the international PV modelling collaborative.

*   ### Philip Schleihauf

    Philip Schleihauf builds websites, administers servers and databases,
    designs graphics, rides unicycles, and sometimes sleeps. Phil joined Calama
    in 2013 to develop and launch [Frames](#frames
    "Frames is an exciting new product being developed at Calama Consulting").

"""


content['footer'] = """
Contact
-------

"""

contact = (
    dict(
        display=Markup("""<address>Toronto ON, Canada</address>"""),
        id='address',
        icon='c',
    ),
    dict(
        display=Markup(markdown('[(613) 530-0323](tel:+1-613-530-0323)')),
        id='telephone',
        icon='t',
    ),
    dict(
        display=Markup(markdown('[rob.andrews@calamaconsulting.ca](mailto:ob.andrews@calamaconsulting.ca)')),
        id='email',
        icon='@',
    ),
)

# END SITE CONTENT # END SITE CONTENT # END SITE CONTENT #


content = dict((n, Markup(markdown(c))) for n, c in content.items())


@app.route('/')
def home():
    return render_template('home.html', title=title, boxes=boxes,
                           researches=researches, contact=contact, **content)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'export':
        open('index.html', 'w').write(app.test_client().get('/').data)
    else:
        app.run(debug=True)
