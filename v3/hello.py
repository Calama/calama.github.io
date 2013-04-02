from flask import Flask, Markup, render_template
from markdown import markdown
content = {}


# SITE CONTENT # SITE CONTENT # SITE CONTENT # SITE CONTENT #

title = "Calama Consulting"


content['header'] = """
Calama Consulting
=================

_Never Stop Innovating!_
"""

content['nav'] = """

* [Calama](#calama "Calama Consulting -- Go to top of page")

"""


content['leader'] = """
The solar photovoltaic industry thrives on innovation. The potential for PV in
the world is huge, but so are the challenges. In the race to integrate solar as
a major player of our sustainable energy mix those companies who do not
innovate will be left behind; as long as the industry relies on unsustainable
government subsidies, there can be no status-quo.

Calama Consulting is a solar systems consulting firm committed to continual
innovation, and specializes in developing customized solutions for its clients.
"""


content['research'] = """
Research
--------

Blah blah blah

horizontal (3-panel?) slider thing here

1.  Point 1
2.  Point 2
3.  etc.
"""

content['people'] = """
People
------

two panels here

*   ### Rob Andrews

    Rob Andrews, the Principle Investigator and Director of Calama is currently
    pursing a doctorate in photovoltaic system design and optimization which is
    unique within the industry. He is published in major academic journals, and
    is an active member of the international PV modelling collaborative.

*   ### Philip Schleihauf

    blah blah blah
"""


content['footer'] = """
Contact
-------

`hello`

"""

# END SITE CONTENT # END SITE CONTENT # END SITE CONTENT #


app = Flask(__name__)
content = dict((n, Markup(markdown(c))) for n, c in content.items())


@app.route('/')
def home():
    return render_template('home.html', title=title, **content)

if __name__ == '__main__':
    app.run(debug=True)
