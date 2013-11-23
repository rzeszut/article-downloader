article-downloader
==================

A web scraper for downloading article metadata (title, journal, authors, year, etc.)

Prerequisites
-------------
Install pip and virtualenv:

    sudo apt-get install python-pip python-virtualenv

Create virtualenv and install requirements:

    virtualenv venv
    . venv/bin/acticate
    pip install -r requirements.txt

Set up SSH proxy tunnel:

    ssh -D 12345 <user>@student.agh.edu.pl

You can now run the application:

    ./bot.py
