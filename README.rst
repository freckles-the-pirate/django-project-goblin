================
Project Goblin
===============

Overview
========

Project Goblin was created to list and manage projects. Note that the projects
are not stored, but only listed. This is useful if you want to showcase
projects on your blog, come out with new announcements, etc.

Installation
============

The easiest way is to use PIP:

    ::

    pip install django-project-goblin

Add ``'goblin'`` to the list of installed apps.

    ::

    INSTALLED_APPS = (
        # ...
        'goblin',
        #...
    )

Models
======

Once installed, you'll have access to Project Goblin's models:

Project
-------

A project is a software project and can contain many releases. The main
attributes for a software project are (self-explainator):

* name
* description
* README (a longer description)
* homepage (URL link to a project).

Release
-------

The release has a foreign key relation to `Project`_ and to `Change`_. This is
used to make readers aware of the release that has taken place for the project.

The attributes for a release are

* project (FK to `Project`_)
* version (The `Version`_ number)
* download (URL to download the release)

Change
------

A change is a difference of one release over another
