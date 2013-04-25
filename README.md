Calama Consulting Website
=========================

The content should all be in [hello.py](hello.py). It's possible that some did
leak into the [template](templates/home.html) though.

Running hello.py will launch a development server:

    $ python hello.py

(site will be live at [localhost:5000](http://localhost:5000))


The site is hosted on github. To update the live page, pass "export" to
`hello.py`:

    $ python hello.py export

This should update `index.html` with the new content. Push to github and it'll
be live!
