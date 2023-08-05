from sys import platform

import os
from time import sleep
from kivy.factory import Factory

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.config import Config
from tools.iconfonts import register
from kivy.core.window import Window
from multiprocessing.dummy import Process
from kivy.clock import Clock


Window.size = (350, 600)
# font_folder = "assets/font/"
# register("icon", f"{font_folder}MaterialIconsRound-Regular.otf", f"{font_folder}googleIconRound.fontd")
Config.set("kivy", "exit_on_escape", "0")
Window.softinput_mode = 'below_target'

class Career_path(MDApp):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Pink"
 

#         # app files
        self.PYTHON_FILES = "UserProfile/libpy/"
        self.KIVY_FILES = "UserProfile/libkv/"
        self.PYTHON_WIDGET_FILES = "UserProfile/widgetpy/"
        self.KIVY_WIDGET_FILES = "UserProfile/widgetkv/"

          

# # Loading kivy files and Widgets
    def build(self):
       
        #Builder loads the '.kv' files   
        return Builder.load_file("manager.kv")
    

    
    def on_start(self):
        Process(target=self.initiate_load_sequence).start()

    def initiate_load_sequence(self):
        sleep(3)
        self.load_screens()
        self.load_widgets()
        Clock.schedule_once(
            lambda x: exec("self.root.ids.manager.add_widget(Factory.Manager())", {"self": self, "Factory": Factory}))
        Clock.schedule_once(
            lambda x: exec("self.root.current = 'manager'", {"self": self}))
        Clock.schedule_once(
            lambda x: exec("self.root.ids.manager.children[0].current = 'login'", {"self": self}), timeout=2)



    def load_screens(self):
        # -------- import python screens -------- #
        libpy = os.listdir(self.PYTHON_FILES)

        for modules in libpy:
            # if modules == "m_cardtextfield":
            #     continue
            exec(f"from UserProfile.libpy import {modules.split('.')[0]}")
        # -------------------------------- #

        # ---------- load kivy screens ---------- #
        libkv = os.listdir(self.KIVY_FILES)
        for kv in libkv:
            Builder.load_file(f"{self.KIVY_FILES}{kv}")
        
    


    def load_widgets(self):
        #import python screens 
        libpy = os.listdir(self.PYTHON_WIDGET_FILES)

        for modules in libpy:
            # if modules == "m_cardtextfield":
            #     continue
            exec(f"from UserProfile.libpy import {modules.split('.')[0]}")
      

        # load kivy screens
        libkv = os.listdir(self.KIVY_WIDGET_FILES)
        for kv in libkv:
            Builder.load_file(f"{self.KIVY_WIDGET_FILES}{kv}")
       
    

    

if __name__ =="__main__":
    Career_path().run()