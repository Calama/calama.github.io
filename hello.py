#!/usr/bin/python


from datetime import date
from flask import Flask, url_for, Markup, render_template
from markdown import markdown
content = {}


app = Flask(__name__)
box_bg = lambda filename: lambda: url_for('static', filename=('img/box/' + filename))
dl = lambda filename: lambda: url_for('static', filename=('doc/' + filename))


logo = """
<svg width="144" height="144">
    <path
        d="m 70.684773,140.51809 c 0.51381,-4.4011 -1.40333,-7.4281 -7.25406,-11.4535 -6.76832,-4.6567 -7.60035,-10.0216 -3.14866,-20.3023 1.47738,-3.4119 1.4853,-4.0419 0.0849,-6.75 -0.84952,-1.6428 -1.69508,-2.986904 -1.87902,-2.986904 -0.18394,0 -1.93302,1.507604 -3.88685,3.350304 -2.78708,2.6286 -4.7023,3.4865 -8.88988,3.9823 -6.00518,0.711 -8.27223,2.756 -7.3911,6.6674 2.45371,10.8919 1.70117,15.5467 -3.01276,18.6354 -3.06873,2.0107 -4.36952,1.0562 -2.0514,-1.5053 2.81766,-3.1134 3.09251,-8.2685 0.72607,-13.6182 -3.71596,-8.4006 -2.49084,-12.1205 6.2772,-19.059604 4.0399,-3.1973 5.18234,-4.7472 5.43733,-7.37672 0.31249,-3.2226 0.23261,-3.30257 -2.5,-2.50278 -4.50111,1.3174 -8.49047,0.91544 -13.32281,-1.34237 -5.774781,-2.69816 -7.838861,-1.53992 -10.215631,5.73237 -0.94359,2.8872 -2.29359,5.9464 -3,6.7982 -1.88144,2.268804 -7.1422499,4.219704 -9.6267997,3.569904 -3.0265496,-0.7914 -2.6867096,-1.7576 1.0110098,-2.874104 4.1800999,-1.2623 6.5874999,-4.7567 7.8246399,-11.35764 0.55672,-2.97044 1.54071,-6.03762 2.18666,-6.81594 2.1232,-2.55829 6.67269,-4.29851 12.954121,-4.95505 8.1399,-0.85078 13.0938,-5.2893 7.616,-6.82366 -4.73741,-1.32698 -6.90235,-3.03095 -9.76789,-7.68804 -3.71643,-6.03998 -5.736911,-6.16826 -12.859431,-0.8165 -5.8266,4.37802 -10.0724597,5.12433 -13.9001693,2.4433 -3.3881,-2.37312 -2.67724996,-3.24888 2.19164,-2.70009 4.1301494,0.46553 4.7252694,0.20927 9.2499993,-3.98314 8.47799,-7.85533 10.76816,-8.29038 19.726771,-3.7474 6.50514,3.2988 9.29102,3.67161 12.09817,1.61896 1.81458,-1.32685 1.8084,-1.40205 -0.20369,-2.47889 -2.63854,-1.4121 -4.2854,-6.11789 -4.2854,-12.24526 0,-6.57414 -2.23821,-8.13708 -10.4788,-7.31731 -5.26402,0.52366 -6.461331,0.30009 -9.521201,-1.77789 -2.3815,-1.6173 -3.60598,-3.29574 -3.83163,-5.25216 l -0.33163,-2.87528 3.07624,2.58848 c 4.36329,3.67147 6.303121,4.03696 12.173531,2.29363 8.67107,-2.57503 13.08056,-0.48307 17.85223,8.4695 1.7482,3.27995 3.26762,5.96355 3.3765,5.96355 0.10888,0 1.68138,0.42544 3.49445,0.94542 l 3.29649,0.94542 -0.64688,-4.31371 c -0.65524,-4.3694 0.83828,-8.85691 4.24165,-12.74467 2.23528,-2.55342 1.18774,-6.06225 -2.4829,-8.31672 -8.70432,-5.3461 -9.70046,-6.2154 -10.56114,-9.2164403 -0.49916,-1.74046 -0.57455,-4.43231 -0.16753,-5.98189 l 0.74003,-2.81740999 1.4187,3.99768999 c 1.85529,5.22794 2.79394,6.0644803 9.88727,8.8117503 8.63085,3.34276 10.82623,6.88187 10.04333,16.19056 -0.50319,5.98293 -0.31044,7.32692 1.32657,9.25 2.18054,2.56159 4.09472,2.93826 4.09472,0.80576 0,-2.3965 4.42679,-6.77871 9.61148,-9.51466 6.11053,-3.22453 6.59005,-5.51166 2.46215,-11.74366 -3.40549,-5.14135 -3.84255,-8.9098403 -1.54795,-13.3471003 1.65648,-3.20328 5.26689,-4.30323999 3.93988,-1.20034 -2.06573,4.83022 -1.68149,7.1878903 1.98562,12.1834903 6.541397,8.91118 6.452507,13.5073 -0.42254,21.84793 -2.95195,3.58123 -3.66024,6.40908 -2.41686,9.64927 0.53971,1.40646 1.02023,1.34182 4.07926,-0.54876 2.924664,-1.80754 4.489327,-2.061 9.994817,-1.61907 8.70697,0.69891 10.31414,-0.76501 10.31414,-9.39478 0,-5.73579 0.23071,-6.34951 3.5712,-9.5 1.96416,-1.85245 4.43916,-3.36808 5.5,-3.36808 2.72026,0 2.41208,0.95007 -1.3212,4.07305 -3.21159,2.68657 -3.24702,2.81151 -2.99771,10.57282 0.3383,10.53152 -1.34302,13.36823 -9.73744,16.42899 -5.86811,2.13962 -10.01485,5.68396 -10.01485,8.56 0,0.95929 1.39302,1.36514 4.68564,1.36514 4.03297,0 5.36708,0.57459 9.57776,4.12509 4.28999,3.61737 5.18373,3.99222 7.26146,3.04553 1.30315,-0.59375 3.15124,-2.33754 4.10687,-3.87508 4.32375,-6.95665 8.89712,-9.38356 14.8617,-7.88655 3.48907,0.87571 3.13912,2.59101 -0.52861,2.59101 -4.29969,0 -7.78064,2.62997 -10.1486,7.66759 -1.12329,2.38969 -3.43352,5.51549 -5.13385,6.94622 -3.27696,2.75738 -2.90743,2.74185 -16.9823,0.71406 -2.79606,-0.40284 -4.31511,-0.0812 -5.75,1.21732 -2.59947,2.35248 -2.46851,2.99742 0.89122,4.38907 2.95198,1.22275 5.37022,5.19927 6.61875,10.88377 1.11109,5.0588 4.32474,6.0537 10.83629,3.3548 2.88328,-1.1951 6.28919,-2.1728 7.5687,-2.1728 2.80425,0 7.85777,2.8352 8.62715,4.8402 0.83818,2.184304 0.0976,2.348004 -3.0934,0.683804 -4.12149,-2.149404 -6.22749,-1.888104 -11.89878,1.476 -5.26632,3.1238 -10.1371,3.7797 -13.81574,1.8603 -1.20134,-0.6268 -4.30248,-3.1018 -6.89142,-5.500004 -4.608487,-4.2689 -7.002447,-5.1485 -9.572957,-3.5174 -1.02489,0.6504 -0.97627,1.395 0.24384,3.7347 1.90515,3.653404 1.9181,5.835804 0.0711,11.973104 -1.31694,4.3759 -1.30305,5.0478 0.13729,6.6394 0.88138,0.9739 3.22824,2.0425 5.215234,2.3745 7.247363,1.2112 10.028473,2.563 12.070453,5.867 1.12324,1.8175 2.04225,4.0123 2.04225,4.8774 0,2.7206 -1.9617,2.9219 -2.95724,0.3034 -1.33908,-3.522 -4.65521,-5.2937 -11.042753,-5.8996 -3.025004,-0.287 -6.773594,-1.1035 -8.330214,-1.8144 -3.2877,-1.5015 -6.12306,-6.5552 -7.15572,-12.7542 -0.73973,-4.4406 -3.41655,-8.1442 -5.88626,-8.1442 -0.8196,0 -1.62105,1.5562 -1.99015,3.8645 -0.46241,2.8917 -1.8783,5.0871 -5.62487,8.7216 -5.9031,5.7264 -5.86149,6.9798 0.43182,13.0052 4.67843,4.4792 6.2971,9.3276 4.6023,13.7853 -1.51426,3.9828 -3.73325,3.3767 -3.23586,-0.8839 z m -3.2031,-33.2427 c 2.15127,-2.834 1.59883,-6.7845 -1.68816,-12.072204 -3.56163,-5.72943 -4.6041,-11.40081 -2.88178,-15.67783 l 1.20807,-3 1.15894,5.56403 c 1.489,7.14868 5.01825,11.5791 12.27641,15.4111 3.52422,1.8607 6.3275,4.143004 7.12022,5.796904 1.5912,3.3199 3.19835,3.5463 3.19835,0.4505 0,-3.6065 -2.67805,-6.511604 -8.57371,-9.300704 -5.75473,-2.7224 -10.42629,-8.10914 -10.42629,-12.02239 0,-1.84989 0.5702,-1.56608 4.2533,2.11702 5.12657,5.12657 9.7651,6.59333 18.32349,5.79414 4.92556,-0.45996 6.900344,-0.22799 8.831527,1.03733 3.16782,2.0757 3.98948,0.8291 1.56608,-2.37589 -1.77011,-2.34104 -2.327543,-2.45678 -10.519097,-2.18405 -7.78156,0.25907 -9.09194,0.029 -13.05262,-2.29216 -4.27532,-2.5055 -6.23032,-5.4525 -2.65268,-3.99867 8.39633,3.41197 14.66897,2.34987 22.379524,-3.78936 3.852353,-3.06729 5.989663,-4.07245 8.507663,-4.00108 3.74044,0.10603 4.38081,-1.09153 1.42855,-2.67154 -3.17568,-1.69957 -5.80795,-1.19618 -9.280933,1.77489 -5.693634,4.87076 -10.623254,7.18993 -15.282944,7.18993 -5.82126,0 -6.73406,-1.77933 -1.35413,-2.63961 5.91685,-0.94615 12.37435,-7.01197 14.27377,-13.40802 1.940184,-6.5333 3.221184,-8.70419 5.577437,-9.45203 2.73122,-0.86686 2.52845,-2.50034 -0.31038,-2.50034 -3.478023,0 -6.344867,3.30591 -8.098787,9.33918 -1.74426,6.00006 -7.91401,12.66082 -11.72751,12.66082 -1.983,0 -1.93909,-0.15173 0.62851,-2.1714 3.43348,-2.70078 6.45826,-9.18205 6.48727,-13.90046 0.0121,-1.96453 -0.71245,-5.72723 -1.61005,-8.36156 -1.50414,-4.41438 -1.5054,-5.05521 -0.0162,-8.17814 1.82386,-3.82469 0.68555,-4.4258 -2.4477,-1.29255 -1.72523,1.72523 -1.98159,2.83056 -1.44959,6.25 1.66837,10.72348 1.7031,15.44863 0.1358,18.47944 -2.62607,5.07826 -3.38674,4.50753 -2.85308,-2.14066 0.61704,-7.68707 -1.50229,-12.55978 -7.58853,-17.44728 -2.83617,-2.27756 -4.26035,-4.31552 -4.71705,-6.75 -0.73591,-3.92269 -1.97117,-4.51363 -2.95506,-1.41367 -0.91598,2.88599 1.1069,7.24224 4.54257,9.78233 4.51598,3.33881 8.1725,10.33199 7.75953,14.84027 l -0.34843,3.80368 -2.15969,-4.70357 c -2.51809,-5.4841 -8.73559,-10.46688 -14.13864,-11.33088 -7.19301,-1.15023 -8.33634,-1.58306 -10.58184,-4.00599 -2.71543,-2.93 -3.5501,-3.08238 -3.5501,-0.64812 0,3.2318 3.7034,5.98553 9.71641,7.22482 7.48807,1.5433 10.59779,3.19805 13.7319,7.30708 3.66385,4.80356 3.16742,5.22312 -1.88603,1.594 -3.84419,-2.76068 -5.28198,-3.19205 -10.75,-3.22522 -4.63012,-0.0281 -7.37429,0.53815 -10.29747,2.12479 -4.42348,2.40099 -6.70082,2.66909 -9.58055,1.12791 -1.46343,-0.78321 -1.93426,-0.71018 -1.93426,0.3 0,4.06266 6.22537,4.8951 13.1408,1.75714 5.67029,-2.57296 12.88233,-2.63356 15.96894,-0.13419 l 2.3313,1.88778 -5.04649,-0.0761 c -6.91406,-0.1043 -11.87754,2.70821 -17.45635,9.89151 -3.24333,4.17612 -5.37355,6.00187 -7.2637,6.22549 -3.37092,0.39882 -3.46423,1.94726 -0.16722,2.77476 3.24849,0.81532 6.51862,-1.34721 10.15233,-6.71372 3.8293,-5.65537 7.15903,-7.93224 12.42697,-8.49754 l 4.41342,-0.47361 -3.69633,2.0432 c -4.0138,2.21869 -8.12317,7.08303 -9.33539,11.05049 -0.42011,1.375 -0.83054,5.07328 -0.91206,8.2184 -0.11364,4.3843 -0.66241,6.2657 -2.35222,8.0645 -1.2122,1.2903 -2.204,2.6545 -2.204,3.0316 0,1.633704 3.29627,0.4689 5.54775,-1.9605 2.02556,-2.1856 2.45225,-3.6702 2.45225,-8.53214 0,-6.79254 1.64447,-11.30954 5.36718,-14.74247 3.43954,-3.17181 4.26565,-2.16617 1.69044,2.05783 -3.30389,5.41924 -2.84015,13.26384 1.14785,19.41698 2.37218,3.6601 3.19212,6.050604 3.15411,9.195804 -0.0568,4.6988 0.28815,5.0823 2.24837,2.5 z"
        id="svg-logo"
        />
</svg>
"""

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

<address>

**Calama Consulting**  
(613) 555 - 3.14  
_postal address_  
[email](mailto:email@example.com, "Send us an email!")

</address>
"""
# NOTE: the double-spaces at the end of the lines ^^ force a line-break.


contact = dict(
    destination="roba77@gmail.com",
)

# END SITE CONTENT # END SITE CONTENT # END SITE CONTENT #


content = dict((n, Markup(markdown(c))) for n, c in content.items())


@app.route('/')
def home():
    return render_template('home.html', title=title, boxes=boxes,
                           researches=researches, contact=contact, **content)

if __name__ == '__main__':
    app.run(debug=True)
