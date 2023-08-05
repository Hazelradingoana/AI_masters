from sys import platform

import os
from time import sleep
from kivy.factory import Factory

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.config import Config
from UserProfile.libkv import *
from kivy.core.window import Window
from multiprocessing.dummy import Process
from kivy.clock import Clock


# Window.size = (350, 600)
# font_folder = "assets/font/"
# register("icon", f"{font_folder}MaterialIconsRound-Regular.otf", f"{font_folder}googleIconRound.fontd")
# Config.set("kivy", "exit_on_escape", "0")
# Window.softinput_mode = 'below_target'

class Career_path(MDApp):


# # Loading kivy files and Widgets
    def build(self):
       
        #Builder loads the '.kv' files   
        return Builder.load_file("manager.kv")
    


Career_path ().run()