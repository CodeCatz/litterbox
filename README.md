litterbox
=========

CodeCatz litterbox - pieces of shitty code

### What's this?

Just a litterbox where we can play with Git and Python. Very messy, lots of fun.

### Web development with Flask

[Flask](http://flask.pocoo.org/) is super slim web framework for Python.
To install it just try

    sudo pip install Flask
    
If you don't have `pip` try this also

    sudo easy_install pip
    
Running `flask` web application

    cd Goranche/webServer
    python server.py
    
Now open `http://localhost:5000` with your favorite web browser and see what happens.

### Vagrant environment

First install [VirtualBox](https://www.virtualbox.org/) and then [Vagrant](http://www.vagrantup.com/)

    git clone git://github.com/zigomir/rvdb.git ~/.rvdb --recursive && cd ~/.rvdb && git checkout python
    vagrant up
    vagrant ssh
    cd /vagrant
