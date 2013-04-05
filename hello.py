#!/usr/bin/python


from datetime import date
from flask import Flask, url_for, Markup, render_template
from markdown import markdown
content = {}


app = Flask(__name__)
box_bg = lambda filename: lambda: url_for('static', filename=('img/box/' + filename))
dl = lambda filename: lambda: url_for('static', filename=('doc/' + filename))


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

Some quick blurb here about products. blah blah blah


"""

boxes = (
    dict(
        name='Frames',
        id='frames',
        description='Frames is a cool program!',
        background=box_bg('frames.png'),
    ),
    dict(
        name='Helicopters',
        id='helicopters',
        description='Fly around and bubblegum and rainbows',
        background=box_bg('helicopters.png'),
    ),
    dict(
        name='Solar Concentrator',
        id='concentrator',
        description='Sunlight yeah yeah yeah',
        background=box_bg('concentrator.png'),
    ),
)


content['research'] = """
Research
--------

"""

researches = (
    dict(
        title='A brilliant piece of research pertaining to Photovoltaics',
        date=date(2012, 1, 1),
        id='photovoltaics-research',
        description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a diam lectus. Sed sit amet ipsum mauris. Maecenas congue ligula ac quam viverra nec consectetur ante hendrerit. Donec et mollis dolor.',
        background=box_bg('photovoltaics.png'),
        download=dl('blah1.pdf'),
    ),
    dict(
        title='Advanced analysis of unobtainable theories yeilding knowledge',
        date=date(2012, 1, 2),
        id='yield-analysis',
        description='Donec viverra mi quis quam pulvinar at malesuada arcu rhoncus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. In rutrum accumsan ultricies.',
        background=box_bg('yeild.png'),
        download=dl('blah2.pdf'),
    ),
    dict(
        title='Systematic synergistically salvageable slippery sloughs',
        date=date(2012, 1, 3),
        id='esses',
        description='Vivamus fermentum semper porta. Nunc diam velit, adipiscing ut tristique vitae, sagittis vel odio. Maecenas convallis ullamcorper ultricies.',
        background=box_bg('sss.png'),
        download=dl('blah3.pdf'),
    ),
    dict(
        title='Advanced analysis of unobtainable theories yeilding knowledge 2',
        date=date(2012, 1, 4),
        id='yield-analysis-2',
        description='blah blah blah blah blah blah blah blah blah blah',
        background=box_bg('yeild.png'),
        download=dl('blah4.pdf'),
    ),
    dict(
        title='Advanced analysis of unobtainable theories yeilding knowledge 3',
        date=date(2012, 1, 5),
        id='yield-analysis-3',
        description='blah blah blah blah blah blah blah blah blah blah',
        background=box_bg('yeild.png'),
        download=dl('blah5.pdf'),
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
        display=Markup("""<address>
                            Somewhere only we know<br/>
                            Toronto M5W 1E6, Canada
                        </address>"""),
        id='address',
        icon='c',
    ),
    dict(
        display=Markup(markdown('[(613) 555-2076](tel:+1-613-555-2076)')),
        id='telephone',
        icon='t',
    ),
    dict(
        display=Markup(markdown('[hello@calamaconsulting.ca](mailto:hello@calamaconsulting.ca)')),
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
    app.run(debug=True)
