# -*- coding: utf-8 -*-
"""setup -- setuptools setup file for los-cocos.

$Author: eykd $
$Rev: 1016 $
$Date: 2008-04-05 16:22:08 -0500 (Sat, 05 Apr 2008) $
"""

__author__ = "PyAr Team"
__version__ = "0.3.0"
__date__ = "2008-04-10"

try:
    import setuptools
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()

from setuptools import setup, find_packages

__description__ = """Cocos: A framework for building games

Cocos is a framework for building games, demos, and other graphical/interactive applications. It is built over pyglet. It provides some conventions and classes to help you structure a "scene based application".

A cocos application consists of several scenes, and a workflow connecting the different scenes. It provides you with a "director" (a singleton) which handles that workflow between scenes. Each scene is composed of an arbitrary number of layers; layers take care of drawing to the screen (using the pyglet and OpenGL APIs), handling events and in general contain all of the game/application logic.

Cocos simplifies the game development in these areas:

    * Defining a workflow for your game
    * Creating special effects in layers
    * Creating transitions between scenes
    * Managing sprites
    * Basic menus 
"""

setup(
    name = "cocos",
    version = __version__,
    author = "PyAr Team",
    description = __description__,
    url = "http://code.google.com/p/los-cocos/",

    packages = find_packages(),

    install_requires=['pyglet>=1.1alpha2',],
    dependency_links=['http://code.google.com/p/pyglet/downloads/list',],

    include_package_data = True,
    zip_safe = False,
    )