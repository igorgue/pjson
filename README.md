pjson
=====

Like `python -mjson.tool` but with moar colors (and less conf)

###Usage

    ⚡ echo '{"json":"obj"}' | pjson
    {
      "json": "obj"
    }

###Looks Like This

Image for the haters:

![image](http://f.cl.ly/items/3R1M3b2j2o2v1z0z2U0E/Screen%20Shot%202012-07-19%20at%206.58.54%20PM.png)

Small retina display images are fucking huge.

###Example With Curl

    ⚡ curl https://github.com/igorgue.json | pjson

###Install

Install `pygments`:

    pip install pygments

or, if you run as root:

    sudo pip install pygments

And copy and paste this:

    curl https://raw.github.com/igorgue/pjson/master/pjson > ~/bin/pjson

If it doesn't work run this:

    ⚡ echo 'export PATH=$HOME/bin:$PATH' >> ~/.bashrc

For zsh bros, though, they might already know this:

    ⚡ echo 'export PATH=$HOME/bin:$PATH' >> ~/.zshrc

###MFW I did This Project

![image](http://alltheragefaces.com/img/faces/large/surprised-omg-l.png)

