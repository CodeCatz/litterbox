litterbox
=========

CodeCatz litterbox - pieces of shitty code

### What's this?

Just a litterbox where we can play with Git and Python. Very messy, lots of fun.

### Web development with Flask

#### Install Flask

[Flask](http://flask.pocoo.org/) is a super slim web framework for Python.
To install it just try running:

    sudo pip install Flask
    
If you don't have `pip`, you can also try:

    sudo easy_install pip
    

That's it. You're ready to run and make Flash apps.

#### An example Flask app

In your local copy of the litterbox repo, move into the folder Goranche/webServer and run the Python script that start a simple web server.

    cd Goranche/webServer
    python server.py
    
Now open `http://localhost:5000` with your favorite web browser and see what happens.

#### Make your own!

Just copy the files from Goranche's webServer folder into your own folder of choice. Make necessary changes to scripts. Run the server & have fun!

### Vagrant environment

First install [VirtualBox](https://www.virtualbox.org/) and then [Vagrant](http://www.vagrantup.com/)

    git clone git://github.com/zigomir/rvdb.git ~/.rvdb --recursive && cd ~/.rvdb && git checkout python
    vagrant up
    vagrant ssh
    cd /vagrant
