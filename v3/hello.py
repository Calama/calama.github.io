from flask import Flask, Markup, render_template
from markdown import markdown
content = {}


# SITE CONTENT # SITE CONTENT # SITE CONTENT # SITE CONTENT #

title = "Calama Consulting"

content['header'] = """
Calama Consulting
=================

_Never Stop Innovating_
"""


content['main'] = """
blah blah
"""


content['research'] = """
Research
--------

Blah blah blah

1. Point 1
2. Point 2
3. etc.
"""

content['people'] = """
People
------

*   ### Rob Andrews
    
    Rob Andrews, the Principle Investigator and Director of Calama is currently pursing a doctorate in photovoltaic system design and optimization which is unique within the industry. He is published in major academic journals, and is an active member of the international PV modelling collaborative.

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
content = {n: Markup(markdown(c)) for n, c in content.items()}

@app.route('/')
def home():
    return render_template('home.html', title=title, **content)

if __name__ == '__main__':
    app.run(debug=True)
