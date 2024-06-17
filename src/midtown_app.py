# -*- coding: utf-8 -*-
"""
Project: MidTown IT Training Solutions App
Description: Provides a gui hub to switch between three algorithmic solutions:
                - Rock Paper Scissors
                - Multiplication Table
                - Caesar Cipher
Version: 2.0.1
Author: Luke Wait
Date: October 30, 2023
License: MIT License

Dependencies (requirements.txt):
CTkToolTip==0.8
customtkinter==5.2.1
darkdetect==0.8.0
packaging==23.2
Pillow==10.1.0

Icons: Designed by Freepik - www.freepik.com

GitHub Repository: https://github.com/LukeWait/gui-app-switcher-midtownapp
"""

import os
import pkg_resources
import customtkinter as ctk
from tkinter import *
from CTkToolTip import *
from PIL import Image

base_path = pkg_resources.resource_filename(__name__, "")


class Gui(ctk.CTk):
    """Represents the graphical user interface.

    Utilizes the customtkinter library (ctk) for appearance settings and interactions.

    Attributes:
        images_path (str): Path to the directory containing images used in the GUI.
        
    Methods:
        __init__(): Initializes the Gui object, sets up the main window, loads images, and creates frames.
        load_images(): Loads images used in the GUI from specified directories.
        load_fonts(): Loads fonts used in the GUI from specified directories.
        create_menu_frame(): Creates and configures the menu frame where users can select solutions and exit.
        create_main_frame(): Creates and configures the main frame where application details are displayed.
        create_title_frame(): Creates and configures the title frame where solution name is displayed.
        create_rps_frame(): Creates and configures the Rock Paper Scissors frame.
        create_mt_frame(): Creates and configures the Multiplication Table frame.
        create_cc_frame(): Creates and configures the Caesar Cipher frame.
        show_solution(): Shows frames according to selected solution.
        switch_rps_frame(): Shows and hides frames within the Rock Paper Scissor screen.
        update_msg(): Updates the msg section of any solution screen.
        update_rps_image(): Updates the image section of the Rock Paper Scissors screen.
        update_rps_name(): Updates the player name labels of the Rock Paper Scissors screen.
        update_rps_score(): Updates the player score labels of the Rock Paper Scissors screen.
        update_rps_segbutton(): Updates the segmented buttons of the Rock Paper Scissors screen.
        update_mt_textbox(): Updates the textbox of the Multiplication Table screen.
        update_cc_textbox(): Updates the textboxes of the Caesar Cipher screen.
        update_mt_slider(): Updates the displayed tooltip value of the Multiplication Table range slider.
    """

    def __init__(self):
        """Initializes the Gui object, sets up the main window, loads images, and creates frames.

        Configures various settings and elements for the game interface.
        """
        super().__init__()
        
        # Constants for colors
        self.DARKNESS = "#202020"
        self.MIDNESS = "#303030"
        self.LIGHTNESS = "#404040"
        self.DARK_BLUE = "#?"
        self.BLUE = "#1f538d"
        self.LIGHT_BLUE = "#3a7ebf"
        self.GREEN = "#4e9a06"
        self.RED = "#cc0000"
        
        # customtkinter appearance settings
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Configure window
        self.title("MidTown IT Training Solutions App")
        self.minsize(901, 600)
        self.geometry("1101x831")
        self.resizable(True, True)
        self.configure(fg_color=self.DARKNESS)

        # Configure grid layout (1x2)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Define paths to various resource directories
        self.images_path = os.path.join(base_path, "..", "assets", "images")
        self.fonts_path = os.path.join(base_path, "..", "assets", "fonts")

        # Dictionaries of solution icons, buttons, and rps images
        self.icons = {}
        self.menu_buttons = {}
        self.rps_images = {}

        # Load images and fonts
        self.load_images()
        self.load_fonts()

        # Create and show frames
        self.create_menu_frame()
        self.create_main_frame()
        self.create_title_frame()
        self.create_rps_frame()
        self.create_mt_frame()
        self.create_cc_frame()
       
    def load_fonts(self):
        """Loads fonts used in the GUI from specified directories.
        """
        try:
            ctk.FontManager.load_font(os.path.join(self.fonts_path, "Fascinate-Regular.ttf"))
            ctk.FontManager.load_font(os.path.join(self.fonts_path, "BRITANIC.ttf"))
            ctk.FontManager.load_font(os.path.join(self.fonts_path, "CaesarDressing-Regular.ttf"))
            ctk.FontManager.load_font(os.path.join(self.fonts_path, "Rubik-Italic-VariableFont_wght.ttf"))
            ctk.FontManager.load_font(os.path.join(self.fonts_path, "Rubik-VariableFont_wght.ttf"))
            ctk.FontManager.load_font(os.path.join(self.fonts_path, "Silkscreen-Bold.ttf"))
            ctk.FontManager.load_font(os.path.join(self.fonts_path, "Silkscreen-Regular.ttf"))
            
        except Exception as e:
            print(f"Error:\n{str(e)}")
     
    def load_images(self):
        """Loads images used in the GUI from specified directories.
        """
        try:
            # Define the solution names and their corresponding file names
            solutions = {
                "Rock Paper Scissors": "rock_paper_scissors.png",
                "Multiplication Table": "multiply_table.png",
                "Caesar Cipher": "caesar_coin.png"
            }
            
            # Define the icon sizes you need
            icon_sizes = [(30, 30), (50, 50)]
            
            # Loop through the solutions and icon sizes to populate the nested dictionary
            for solution, file_name in solutions.items():
                solution_icons = {}
                for size in icon_sizes:
                    icon = ctk.CTkImage(Image.open(os.path.join(self.images_path, file_name)), 
                                        size=size)
                    solution_icons[size] = icon
                self.icons[solution] = solution_icons

            # Define the player names (left and right) and their corresponding file names
            player_names = ["p1", "p2"]
            gesture_names = ["Rock", "Paper", "Scissors"]

            # Loop through the player and gesture names to populate the dictionary
            for player in player_names:
                self.rps_images[player] = {}
                for gesture in gesture_names:
                    image = ctk.CTkImage(Image.open(os.path.join(self.images_path, 
                                         f"{gesture.lower()}-{player}.png")), size=(180, 180))
                    self.rps_images[player][gesture] = image

            self.image_blank = ctk.CTkImage(Image.open(os.path.join(self.images_path, "blank.png")), 
                                            size=(180, 180))

        except Exception as e:
            print(f"Error:\n{str(e)}")
    
    def create_menu_frame(self):
        """Creates and configures the menu frame.

        Users can select from the 3 algorithmic solutions and exit application.
        """
        # Configure menu frame
        self.menu_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.menu_frame.grid_rowconfigure((1, 5), weight=1)
        self.menu_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")
        # Configure menu frame widgets
        self.menu_label_main = ctk.CTkLabel(self.menu_frame, text="MidTown IT", 
                                            font=ctk.CTkFont(size=34, family="Fascinate"))
        self.menu_label_main.grid(row=0, column=0, padx=0, pady=(30, 0))
        self.menu_label_sub = ctk.CTkLabel(self.menu_frame, text="Training Solutions App", 
                                           font=ctk.CTkFont(size=18, family="Rubik"))
        self.menu_label_sub.grid(row=1, column=0, padx=0, pady=0, sticky="n")
        
        # Create buttons for each entry in the menu_icons dictionary
        for menu_text, icon_sizes in self.icons.items():
            menu_icon = icon_sizes[(30, 30)]
            menu_button = ctk.CTkButton(self.menu_frame, corner_radius=10, height=50,
                                        text=menu_text, fg_color=self.DARKNESS,
                                        image=menu_icon, anchor="w",
                                        font=ctk.CTkFont(family="Rubik", size=15))
            menu_button.grid(row=len(self.menu_buttons) + 2, column=0, padx=30, sticky="ew")
            
            # Add the button to the menu_buttons dictionary
            self.menu_buttons[menu_text] = menu_button
        
        self.menu_button_exit = ctk.CTkButton(self.menu_frame, text="Exit Application", width=220, 
                                              height=50, corner_radius=30,
                                              font=ctk.CTkFont(size=15, family="Rubik", weight="bold"))
        self.menu_button_exit.grid(row=5, column=0, padx=30, pady=30, sticky="s")

    def create_main_frame(self):
        """Creates and configures the main frame.

        Displays application information on startup and exit.
        """
        self.main_frame = ctk.CTkFrame(self, corner_radius=10, fg_color=self.MIDNESS)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid(row=0, column=1, padx=(0, 15), pady=15, sticky="nsew")
        
    def create_title_frame(self):
        """Creates and configures the title frame.

        Displays selected solution title bar.
        """
        # Configure title frame
        self.title_frame = ctk.CTkFrame(self.main_frame, corner_radius=10, 
                                        fg_color=self.BLUE, bg_color=self.DARKNESS)
        self.title_frame.grid_columnconfigure((0, 1), weight=1)
        # Configure title frame widgets
        self.title_image = ctk.CTkLabel(self.title_frame, text="", anchor="e")
        self.title_image.grid(row=0, column=0, padx=(0, 10), pady=(10, 0), sticky="new")
        self.title_label = ctk.CTkLabel(self.title_frame, text="", anchor="w")
        self.title_label.grid(row=0, column=1, padx=(10, 0), pady=(0, 5), sticky="sew")    
        self.title_filler = ctk.CTkLabel(self.title_frame, text="", font=ctk.CTkFont(size=1), 
                                         height=10)
        self.title_filler.grid(row=1, column=0, columnspan=2, padx=0, pady=0, sticky="nsew")

    def create_rps_frame(self):
        """Creates and configures the Rock Paper Scissors frame.

        Contains two main inner frames - login and game.
        Contains three sub inner frames for displaying messages and game options.
        """
        # Configure rps frame
        self.rps_frame = ctk.CTkFrame(self.main_frame, corner_radius=10, 
                                      fg_color=self.MIDNESS, bg_color=self.DARKNESS)
        self.rps_frame.grid_columnconfigure(0, weight=1)
        self.rps_frame.grid_rowconfigure(1, weight=1)
        self.rps_filler = ctk.CTkLabel(self.rps_frame, text="", font=ctk.CTkFont(size=1), 
                                       height=5, fg_color=self.DARKNESS)
        self.rps_filler.grid(row=0, column=0, padx=0, pady=0, sticky="new")
        
        # Configure login frame
        self.rps_frame_login = ctk.CTkFrame(self.rps_frame, corner_radius=0, fg_color=self.MIDNESS)
        self.rps_frame_login.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.rps_frame_login.grid_columnconfigure((0, 1), weight=1)
        self.rps_frame_login.grid_rowconfigure((0, 1), weight=1)
        # Configure login frame widgets
        self.rps_label_player1 = ctk.CTkLabel(self.rps_frame_login, text="PLAYER 1", 
                                              font=ctk.CTkFont(size=22, family="Silkscreen", weight="bold"))
        self.rps_label_player1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="s")
        self.rps_label_player2 = ctk.CTkLabel(self.rps_frame_login, text="PLAYER 2", 
                                              font=ctk.CTkFont(size=22, family="Silkscreen", weight="bold"))
        self.rps_label_player2.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="s")
        self.rps_entry_p1name = ctk.CTkEntry(self.rps_frame_login, fg_color=self.DARKNESS, width=180, 
                                             justify="center", text_color=self.GREEN, 
                                             font=ctk.CTkFont(size=14, family="Silkscreen"), 
                                             placeholder_text="P1 Name here", validate="key", 
                                             validatecommand=(self.register(lambda P: len(P) <= 12), "%P"))
        self.rps_entry_p1name.grid(row=1, column=0, padx=10, pady=10, sticky="n")
        self.rps_entry_p2name = ctk.CTkEntry(self.rps_frame_login, fg_color=self.DARKNESS, width=180, 
                                             justify="center", text_color=self.GREEN,
                                             font=ctk.CTkFont(size=14, family="Silkscreen"),
                                             placeholder_text="P2 Name here", validate="key", 
                                             validatecommand=(self.register(lambda P: len(P) <= 12), "%P"))
        self.rps_entry_p2name.grid(row=1, column=1, padx=10, pady=10, sticky="n")
        
        # Configure login msg frame
        self.rps_frame_login_msg = ctk.CTkFrame(self.rps_frame_login, corner_radius=10, height=160,
                                                fg_color=self.DARKNESS)
        self.rps_frame_login_msg.grid(row=2, column=0, columnspan=2, padx=0, pady=(10, 0), sticky="nsew") 
        self.rps_frame_login_msg.grid_columnconfigure(0, weight=1)
        self.rps_frame_login_msg.grid_rowconfigure(1, weight=1)
        # Configure login msg frame widgets
        self.rps_msg_login = ctk.CTkLabel(self.rps_frame_login_msg, text_color=self.GREEN,
                                          font=ctk.CTkFont(size=14, family="Silkscreen"),
                                          text="Welcome to the Rock Paper Scissors game\n" +
                                               "Please enter a name for P1 and P2")
        self.rps_msg_login.grid(row=0, column=0, padx=10, pady=(20, 10), sticky="")
        self.rps_button_start = ctk.CTkButton(self.rps_frame_login_msg, corner_radius=10, height=50, 
                                              text="Start Game", fg_color=self.LIGHTNESS,
                                              hover_color=self.GREEN, 
                                              font=ctk.CTkFont(size=14, family="Silkscreen"))
        self.rps_button_start.grid(row=1, column=0, padx=10, pady=(10, 20))
        
        # Configure game frame
        self.rps_frame_game = ctk.CTkFrame(self.rps_frame, corner_radius=0, fg_color=self.MIDNESS)
        self.rps_frame_game.grid_columnconfigure((0, 2), weight=1)
        self.rps_frame_game.grid_rowconfigure((0, 3), weight=1)
        # Configure game frame widgets
        self.rps_label_p1name = ctk.CTkLabel(self.rps_frame_game, text="", 
                                             font=ctk.CTkFont(size=22, family="Silkscreen", weight="bold"))
        self.rps_label_p1name.grid(row=0, column=0, padx=0, pady=(10, 0), sticky="s")
        self.rps_label_p1score = ctk.CTkLabel(self.rps_frame_game, text="Score: 0", width=200,
                                              font=ctk.CTkFont(size=14, family="Silkscreen"))
        self.rps_label_p1score.grid(row=1, column=0, padx=0, pady=0, sticky="")
        self.rps_label_p2name = ctk.CTkLabel(self.rps_frame_game, text="", 
                                             font=ctk.CTkFont(size=22, family="Silkscreen", weight="bold"))
        self.rps_label_p2name.grid(row=0, column=2, padx=0, pady=(10, 0), sticky="s")
        self.rps_label_p2score = ctk.CTkLabel(self.rps_frame_game, text="Score: 0", width=200,
                                              font=ctk.CTkFont(size=14, family="Silkscreen"))
        self.rps_label_p2score.grid(row=1, column=2, padx=0, pady=0, sticky="")   
        self.rps_frame_p1choice = ctk.CTkFrame(self.rps_frame_game, corner_radius=10)
        self.rps_frame_p1choice.grid(row=2, column=0, padx=10, pady=(5, 10))
        self.rps_image_p1choice = ctk.CTkLabel(self.rps_frame_p1choice, text="",
                                               text_color=self.GREEN, image=self.image_blank)
        self.rps_image_p1choice.grid(row=0, column=0, padx=10, pady=10)
        self.rps_label_vs = ctk.CTkLabel(self.rps_frame_game, text="Vs", 
                                         font=ctk.CTkFont(size=33, family="Silkscreen", weight="bold"))
        self.rps_label_vs.grid(row=2, column=1, padx=0, pady=10)
        self.rps_frame_p2choice = ctk.CTkFrame(self.rps_frame_game, corner_radius=10)
        self.rps_frame_p2choice.grid(row=2, column=2, padx=10, pady=(5, 10))
        self.rps_image_p2choice = ctk.CTkLabel(self.rps_frame_p2choice, text="",
                                               text_color=self.GREEN, image=self.image_blank)
        self.rps_image_p2choice.grid(row=0, column=0, padx=10, pady=10)
        self.rps_segbutton_p1 = ctk.CTkSegmentedButton(self.rps_frame_game, width=200,
                                                       font=ctk.CTkFont(size=14, family="Silkscreen"),
                                                       unselected_hover_color=self.GREEN,
                                                       values=["Rock", "Paper", "Scissors"])
        self.rps_segbutton_p1.grid(row=3, column=0, padx=0, pady=(0, 10), sticky="n")
        self.rps_segbutton_p2 = ctk.CTkSegmentedButton(self.rps_frame_game, width=200,
                                                       font=ctk.CTkFont(size=14, family="Silkscreen"),
                                                       unselected_hover_color=self.GREEN,
                                                       values=["Rock", "Paper", "Scissors"])
        self.rps_segbutton_p2.grid(row=3, column=2, padx=0, pady=(0, 10), sticky="n")
        
        # Configure game msg frame
        self.rps_frame_game_msg = ctk.CTkFrame(self.rps_frame_game, corner_radius=10, 
                                               fg_color=self.DARKNESS, height=160)
        self.rps_frame_game_msg.grid_columnconfigure(0, weight=1)
        self.rps_frame_game_msg.grid_rowconfigure(1, weight=1)
        # Configure game msg frame widgets
        self.rps_msg_game = ctk.CTkLabel(self.rps_frame_game_msg, text_color=self.GREEN,
                                         text="P1 and P2 make your selection\nNo Peaking!",
                                         font=ctk.CTkFont(size=14, family="Silkscreen"))
        self.rps_msg_game.grid(row=0, column=0, padx=10, pady=(20, 10), sticky="")
        self.rps_button_quit1 = ctk.CTkButton(self.rps_frame_game_msg, corner_radius=10, height=50, 
                                              fg_color=self.LIGHTNESS, 
                                              hover_color=self.RED, text="Quit Game",
                                              font=ctk.CTkFont(size=14, family="Silkscreen"))
        self.rps_button_quit1.grid(row=1, column=0, padx=10, pady=(10, 20), sticky="")
        
        # Configure postgame msg frame
        self.rps_frame_postgame_msg = ctk.CTkFrame(self.rps_frame_game, corner_radius=10, 
                                                   fg_color=self.DARKNESS, height=160)
        self.rps_frame_postgame_msg.grid_columnconfigure((0, 1), weight=1)
        self.rps_frame_postgame_msg.grid_rowconfigure(1, weight=1)
        # Configure postgame msg frame widgets
        self.rps_msg_postgame = ctk.CTkLabel(self.rps_frame_postgame_msg, text_color=self.GREEN,
                                             font=ctk.CTkFont(size=14, family="Silkscreen"))
        self.rps_msg_postgame.grid(row=0, column=0, columnspan=2, padx=10, pady=(20, 10), sticky="")
        self.rps_button_quit2 = ctk.CTkButton(self.rps_frame_postgame_msg, corner_radius=10,
                                              height=50, fg_color=self.LIGHTNESS, 
                                              hover_color=self.RED, text="Quit Game", 
                                              font=ctk.CTkFont(size=14, family="Silkscreen"))
        self.rps_button_quit2.grid(row=1, column=0, padx=10, pady=(10, 20), sticky="e")
        self.rps_button_replay = ctk.CTkButton(self.rps_frame_postgame_msg, corner_radius=10, 
                                               height=50, fg_color=self.LIGHTNESS, 
                                               hover_color=self.GREEN, text="Play Again", 
                                               font=ctk.CTkFont(size=14, family="Silkscreen"))
        self.rps_button_replay.grid(row=1, column=1, padx=10, pady=(10, 20), sticky="w")
        
    def create_mt_frame(self):
        """Creates and configures the Multiplication Table frame.
        
        Contains one main inner frame and a sub frame for messages.
        """
        # Configure mt frame
        self.mt_frame = ctk.CTkFrame(self.main_frame, corner_radius=10, 
                                     fg_color=self.MIDNESS, bg_color=self.DARKNESS)
        self.mt_frame.grid_columnconfigure(0, weight=1)
        self.mt_frame.grid_rowconfigure(1, weight=1)
        self.mt_filler = ctk.CTkLabel(self.mt_frame, text="", font=ctk.CTkFont(size=1), 
                                      height=5, fg_color=self.DARKNESS)
        self.mt_filler.grid(row=0, column=0, padx=0, pady=0, sticky="new")
        
        # Configure main frame
        self.mt_frame_main = ctk.CTkFrame(self.mt_frame, corner_radius=0, fg_color=self.MIDNESS)
        self.mt_frame_main.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.mt_frame_main.grid_columnconfigure((0, 1), weight=1, uniform="col_uniform")
        self.mt_frame_main.grid_rowconfigure((0, 2, 4, 6), weight=1)
        # Configure main frame widgets
        self.mt_label_user = ctk.CTkLabel(self.mt_frame_main, text="Username", 
                                          font=ctk.CTkFont(size=24, family="Britannic Bold"))
        self.mt_label_user.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="s")
        self.mt_entry_user = ctk.CTkEntry(self.mt_frame_main, fg_color=self.DARKNESS, width=180, 
                                          justify="center", text_color=self.GREEN, 
                                          font=ctk.CTkFont(size=14, family="Silkscreen"), 
                                          placeholder_text="Enter name", validate="key", 
                                          validatecommand=(self.register(lambda P: len(P) <= 12), "%P"))
        self.mt_entry_user.grid(row=1, column=0, padx=10, pady=10) 
        self.mt_label_multiplier = ctk.CTkLabel(self.mt_frame_main, text="Multiplier", 
                                                font=ctk.CTkFont(size=24, family="Britannic Bold"))
        self.mt_label_multiplier.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="s")
        self.mt_entry_multiplier = ctk.CTkEntry(self.mt_frame_main, fg_color=self.DARKNESS, width=180, 
                                                justify="center", text_color=self.GREEN, 
                                                font=ctk.CTkFont(size=14, family="Silkscreen"), 
                                                placeholder_text="Enter number", validate="key", 
                                                validatecommand=(self.register(lambda P: len(P) <= 12), "%P"))
        self.mt_entry_multiplier.grid(row=3, column=0, padx=10, pady=10)
        self.mt_label_multiplicand = ctk.CTkLabel(self.mt_frame_main, text="Multiplicand Range", 
                                           font=ctk.CTkFont(size=24, family="Britannic Bold"))
        self.mt_label_multiplicand.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="s")
        self.mt_slider_multiplicand = ctk.CTkSlider(self.mt_frame_main, from_=1, to=24, number_of_steps=24, 
                                                    width=180, command=self.update_mt_slider)
        self.mt_slider_multiplicand.grid(row=5, column=0, padx=10, pady=(10, 5))
        self.mt_slider_tooltip = CTkToolTip(self.mt_slider_multiplicand, message="12",
                                            font=ctk.CTkFont(size=10, family="Silkscreen"))
        self.mt_label_multiplicand = ctk.CTkLabel(self.mt_frame_main, width=180, 
                                           text="1              12            24", 
                                           font=ctk.CTkFont(size=10, family="Silkscreen"))
        self.mt_label_multiplicand.grid(row=6, column=0, padx=10, pady=(0, 10), sticky="n")
        self.mt_textbox = ctk.CTkTextbox(self.mt_frame_main, state="disabled", wrap=NONE, width=500,
                                         fg_color=self.DARKNESS, text_color=self.GREEN, 
                                         font=ctk.CTkFont(size=14, family="Silkscreen"))
        self.mt_textbox.grid(row=0, column=1, rowspan=7, padx=(0, 10), pady=10, sticky="nsw")
        
        # Configure msg frame
        self.mt_frame_msg = ctk.CTkFrame(self.mt_frame_main, corner_radius=10, 
                                         fg_color=self.DARKNESS, height=160)
        self.mt_frame_msg.grid(row=7, column=0, columnspan=3, padx=0, pady=(10, 0), sticky="nsew")
        self.mt_frame_msg.grid_columnconfigure(0, weight=1)
        self.mt_frame_msg.grid_rowconfigure(1, weight=1)
        # Configure msg frame widgets
        self.mt_msg = ctk.CTkLabel(self.mt_frame_msg, text_color=self.GREEN,
                                   text="Welcome to the Multiplication Table generator\n" +
                                        "Enter the details to be used",
                                   font=ctk.CTkFont(size=14, family="Silkscreen"))
        self.mt_msg.grid(row=0, column=0, padx=10, pady=(20, 10), sticky="")
        self.mt_button_generate = ctk.CTkButton(self.mt_frame_msg, corner_radius=10, height=50, 
                                                text="Generate", fg_color=self.LIGHTNESS,
                                                hover_color=self.GREEN, 
                                                font=ctk.CTkFont(size=14, family="Silkscreen"))
        self.mt_button_generate.grid(row=1, column=0, padx=10, pady=(10, 20))
          
    def create_cc_frame(self):
        """Creates and configures the Caesar Cipher frame.
        """
        # Configure cc frame
        self.cc_frame = ctk.CTkFrame(self.main_frame, corner_radius=10, 
                                     fg_color=self.MIDNESS, bg_color=self.DARKNESS)
        self.cc_frame.grid_columnconfigure(0, weight=1)
        self.cc_frame.grid_rowconfigure(1, weight=1)
        self.cc_filler = ctk.CTkLabel(self.cc_frame, text="", font=ctk.CTkFont(size=1), 
                                      height=5, fg_color=self.DARKNESS)
        self.cc_filler.grid(row=0, column=0, padx=0, pady=0, sticky="new")
        
        # Configure main frame
        self.cc_frame_main = ctk.CTkFrame(self.cc_frame, corner_radius=0, fg_color=self.MIDNESS)
        self.cc_frame_main.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.cc_frame_main.grid_columnconfigure((0, 1), weight=1, uniform="col_uniform")
        self.cc_frame_main.grid_rowconfigure(1, weight=1)
        # Configure main frame widgets
        self.cc_label_ptext = ctk.CTkLabel(self.cc_frame_main, text="Plaintext", width=500,
                                           font=ctk.CTkFont(size=23, family="Caesar Dressing"))
        self.cc_label_ptext.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="e")
        self.cc_label_ctext = ctk.CTkLabel(self.cc_frame_main, text="Ciphertext", width=500,
                                           font=ctk.CTkFont(size=23, family="Caesar Dressing"))
        self.cc_label_ctext.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="w")
        self.cc_textbox_ptext = ctk.CTkTextbox(self.cc_frame_main, wrap=WORD, width=500,
                                               fg_color=self.DARKNESS, text_color=self.GREEN, 
                                               font=ctk.CTkFont(size=14, family="Silkscreen"))
        self.cc_textbox_ptext.grid(row=1, column=0, padx=10, pady=10, sticky="nse")
        self.cc_textbox_ctext = ctk.CTkTextbox(self.cc_frame_main, wrap=WORD, width=500,
                                               fg_color=self.DARKNESS, text_color=self.GREEN, 
                                               font=ctk.CTkFont(size=14, family="Silkscreen"))
        self.cc_textbox_ctext.grid(row=1, column=1, padx=10, pady=10, sticky="nsw")
        self.cc_label_key = ctk.CTkLabel(self.cc_frame_main, text="Cipher Key:", 
                                         font=ctk.CTkFont(size=23, family="Caesar Dressing"))
        self.cc_label_key.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.cc_entry_key = ctk.CTkEntry(self.cc_frame_main, fg_color=self.DARKNESS, width=180, 
                                         justify="center", text_color=self.GREEN, 
                                         font=ctk.CTkFont(size=14, family="Silkscreen"), 
                                         placeholder_text="Enter key", validate="key", 
                                         validatecommand=(self.register(lambda P: len(P) <= 12), "%P"))
        self.cc_entry_key.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        
        # Configure msg frame
        self.cc_frame_msg = ctk.CTkFrame(self.cc_frame_main, corner_radius=10, 
                                         fg_color=self.DARKNESS, height=160)
        self.cc_frame_msg.grid(row=3, column=0, columnspan=2, padx=0, pady=(10, 0), sticky="nsew")    
        self.cc_frame_msg.grid_columnconfigure((0, 1), weight=1)
        self.cc_frame_msg.grid_rowconfigure(1, weight=1)
        # Configure msg frame widgets
        self.cc_msg = ctk.CTkLabel(self.cc_frame_msg, text_color=self.GREEN,
                                   text="Welcome to the Caesar Cipher encryption service\n" +
                                        "Enter text and cipher key to be used",
                                   font=ctk.CTkFont(size=14, family="Silkscreen"))
        self.cc_msg.grid(row=0, column=0, columnspan=2, padx=10, pady=(20, 10), sticky="")
        self.cc_button_encode = ctk.CTkButton(self.cc_frame_msg, corner_radius=10,
                                              height=50, fg_color=self.LIGHTNESS, 
                                              hover_color=self.GREEN, text="Encrypt", 
                                              font=ctk.CTkFont(size=14, family="Silkscreen"))
        self.cc_button_encode.grid(row=1, column=0, padx=10, pady=(10, 20), sticky="e")
        self.cc_button_decode = ctk.CTkButton(self.cc_frame_msg, corner_radius=10, 
                                               height=50, fg_color=self.LIGHTNESS, 
                                               hover_color=self.GREEN, text="Decrypt", 
                                               font=ctk.CTkFont(size=14, family="Silkscreen"))
        self.cc_button_decode.grid(row=1, column=1, padx=10, pady=(10, 20), sticky="w")
    
    def show_solution(self, title):
        """Shows frames according to selected solution.
        
        Configures the title frame to display selected solution name, icon and font.
        
        Args:
            title (str): The selected solution ("Rock Paper Scissors", "Multiplication Table",
                         or "Caesar Cipher").
        """
        # Forget title frame and reconfigure
        self.title_frame.grid_forget()
        self.title_label.configure(text=title)
        self.title_image.configure(image=self.icons[title][(50, 50)])
        
        # Display frames according to solution
        if title == "Rock Paper Scissors":
            self.title_label.configure(font=ctk.CTkFont(size=33, family="Silkscreen", weight="bold"))
            self.mt_frame.grid_forget()
            self.cc_frame.grid_forget()
            self.rps_frame.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")
        elif title == "Multiplication Table":
            self.title_label.configure(font=ctk.CTkFont(size=38, family="Britannic Bold"))
            self.rps_frame.grid_forget()
            self.cc_frame.grid_forget()
            self.mt_frame.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")
        elif title == "Caesar Cipher":
            self.title_label.configure(font=ctk.CTkFont(size=36, family="Caesar Dressing"))
            self.rps_frame.grid_forget()
            self.mt_frame.grid_forget()
            self.cc_frame.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")
        
        # Display configured title frame 
        self.title_frame.grid(row=0, column=0, padx=0, pady=0, sticky="new")

    def switch_rps_frame(self, screen):
        """Shows and hides frames within the Rock Paper Scissor screen.
        
        Configures Gui widgets to default states.
        
        Args:
            screen (str): The screen configuration to be displayed ("login", "game", or "postgame").
        """
        if screen == "login":
            # Clear entry fields
            self.rps_entry_p1name.delete(0, END)
            self.rps_entry_p2name.delete(0, END)
            # Forget game frame and show login frame
            self.rps_frame_game.grid_forget()
            self.rps_frame_login.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nsew")
        elif screen == "game":
            # Reset widgets for new round
            self.update_rps_segbutton("p1", "enabled")
            self.update_rps_segbutton("p2", "enabled")
            self.update_rps_image("p1", "Waiting")
            self.update_rps_image("p2", "Waiting")
            # Forget login frame and postgame msg frame in case of replay rounds
            self.rps_frame_login.grid_forget()
            self.rps_frame_postgame_msg.grid_forget()
            # Show game frame and game msg frame
            self.rps_frame_game_msg.grid(row=4, column=0, columnspan=3, padx=0, pady=(10, 0), sticky="nsew")
            self.rps_frame_game.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nsew")
        elif screen == "postgame":
            # Switch from game msg frame to postgame msg frame
            self.rps_frame_game_msg.grid_forget()
            self.rps_frame_postgame_msg.grid(row=4, column=0, columnspan=3, padx=0, pady=(10, 0), sticky="nsew")            

    def update_msg(self, msg, frame, type):
        """Updates the msg section of the Rock Paper Scissors screen.

        Args:
            msg (str): The message to be displayed.
            frame (str): The msg frame to display the message in ("login", "game", or "postgame").
            type (str): The type of message, determining text color ("error", or "system")
        """
        # Color text by type of msg
        if type == "error":
            color = self.RED
        elif type == "system":
            color = self.GREEN
        
        # Choice of msg frame to update    
        if frame == "rps_login":
            self.rps_msg_login.configure(text=msg, text_color=color)         
        elif frame == "rps_game":
            self.rps_msg_game.configure(text=msg, text_color=color)  
        elif frame == "rps_postgame":
            self.rps_msg_postgame.configure(text=msg, text_color=color)
        elif frame == "mt":
            self.mt_msg.configure(text=msg, text_color=color)
        elif frame == "cc":
            self.cc_msg.configure(text=msg, text_color=color)          

    def update_rps_image(self, player, output):
        """Updates the image section of the Rock Paper Scissors screen.

        Args:
            player (str): The players' image to update ("p1", or "p2").
            output (str): The image to be output ("Waiting", "?", "Rock", "Paper", or "Scissors").
        """
        if player == "p1":
            if output == "Waiting":
                self.rps_image_p1choice.configure(text="Waiting for input...", image=self.image_blank,
                                                  font=ctk.CTkFont(size=14, family="Silkscreen"))
            elif output == "?":
                self.rps_image_p1choice.configure(text="?", 
                         font=ctk.CTkFont(size=50, family="Silkscreen", weight="bold"))
            elif output == "Rock" or "Paper" or "Scissors":
                self.rps_image_p1choice.configure(text="", image=self.rps_images[player][output])
        elif player == "p2":
            if output == "Waiting":
                self.rps_image_p2choice.configure(text="Waiting for input...", image=self.image_blank,
                                                  font=ctk.CTkFont(size=14, family="Silkscreen"))
            elif output == "?":
                self.rps_image_p2choice.configure(text="?", 
                         font=ctk.CTkFont(size=50, family="Silkscreen", weight="bold"))
            elif output == "Rock" or "Paper" or "Scissors":
                self.rps_image_p2choice.configure(text="", image=self.rps_images[player][output])

    def update_rps_name(self, player, name):
        """Updates the player name labels of the Rock Paper Scissors screen.

        Args:
            player (str): The players' name to update ("p1", or "p2").
            name (str): The name to be output.
        """
        if player == "p1":
            self.rps_label_p1name.configure(text=name)
        elif player == "p2":
            self.rps_label_p2name.configure(text=name)

    def update_rps_score(self, player, score):
        """Updates the player score labels of the Rock Paper Scissors screen.

        Args:
            player (str): The players' score to update ("p1", or "p2").
            score (str): The score to be output.
        """
        if player == "p1":
            self.rps_label_p1score.configure(text=f"Score: {score}")
        elif player == "p2":
            self.rps_label_p2score.configure(text=f"Score: {score}")

    def update_rps_segbutton(self, player, state):
        """Updates the segmented buttons of the Rock Paper Scissors screen.

        Args:
            player (str): The players' button state to update ("p1", or "p2").
            state (str): The state of the button to change to ("enabled", or "disabled")
        """
        if player == "p1":
            if state == "enabled":
                self.rps_segbutton_p1.configure(state="normal")
            elif state == "disabled":
                self.rps_segbutton_p1.set("deselect")
                self.rps_segbutton_p1.configure(state="disabled")
        elif player == "p2":
            if state == "enabled":
                self.rps_segbutton_p2.configure(state="normal")
            elif state == "disabled":
                self.rps_segbutton_p2.set("deselect")
                self.rps_segbutton_p2.configure(state="disabled")
        
    def update_mt_textbox(self, text):
        """Updates the textbox of the Multiplication Table screen.

        Args:
            text (str): The text to be displayed.
        """
        # Enable textbox and clear out contents
        self.mt_textbox.configure(state="normal")
        self.mt_textbox.delete("0.0", END)
        # If text is provided, insert into textbox
        if text:
            self.mt_textbox.insert(END, text)
        self.mt_textbox.configure(state="disabled")
    
    def update_cc_textbox(self, text, output):
        """Updates the textboxes of the Caesar Cipher screen.

        Args:
            text (str): The text to be displayed.
            output (str): The type of text to be displayed ("ptext", or "ctext").
        """
        if output == "ptext":
            self.cc_textbox_ptext.delete(0.0, END)
            self.cc_textbox_ptext.insert(END, text)
        elif output == "ctext":
            self.cc_textbox_ctext.delete(0.0, END)
            self.cc_textbox_ctext.insert(END, text)  
        
    def update_mt_slider(self, value):
        """Updates the displayed tooltip value of the Multiplication Table range slider.

        Args:
            value (int): The value to display on the slider.
        """
        self.mt_slider_tooltip.configure(message=int(value))          


class RockPaperScissors:
    """Manages Rock Paper Scissors functionality.

    Attributes:
        gui (Gui): Reference to the shared Gui instance.
        p1name (str): Player one username.
        p2name (str): Player two username.
        p1choice (str): Player one rock, paper, scissors choice.
        p2choice (str): Player two rock, paper, scissors choice.
        p1score (int): Player one number of rounds won.
        p2score (int): Player two number of rounds won.

    Methods:
        start(): Starts a new game of Rock Paper Scissors.
        replay(): Starts a new round of Rock Paper Scissors.
        quit(): Exits Rock Paper Scissors mid-game or upon completion.
        select(): Handles player choice during game of Rock Paper Scissors.
        results(): Calculates and displays results of a round of Rock Paper Scissors.
    """

    def __init__(self, gui):
        """Initializes the RockPaperScissors instance.
        
        Args:
            gui (Gui): Reference to the shared Gui instance.
        """
        self.gui = gui
        self.p1name = None
        self.p2name = None
        self.p1choice = None
        self.p2choice = None
        self.p1score = 0
        self.p2score = 0
                
    def start(self):
        """Starts a new game of Rock Paper Scissors.

        Gets usernames from entry fields. 
        If both players have entered names, switches to the game screen.
        """
        # Get usernames from entry fields
        self.p1name = self.gui.rps_entry_p1name.get()
        self.p2name = self.gui.rps_entry_p2name.get()
        
        # Store invalid fields for accurate error message
        invalid_fields = []
        if not self.p1name:
            invalid_fields.append("Player 1 empty")
        if not self.p2name:
            invalid_fields.append("Player 2 empty")
        
        # Validate entry fields and switch to game screen
        if invalid_fields:
            error_message = " & ".join(invalid_fields)
            self.gui.update_msg(f"Input Error: Please ensure all fields have correct input\n"
                                f"Fields: {error_message}", 
                                "rps_login", "error")
        else:
            self.gui.update_rps_name("p1", self.p1name)
            self.gui.update_rps_name("p2", self.p2name)
            self.gui.switch_rps_frame("game")

    def replay(self):
        """Starts a new round of Rock Paper Scissors.
        """
        self.gui.switch_rps_frame("game")

    def quit(self):
        """Quits the current Rock Paper Scissors game and returns to the login screen.

        Displays a thank you message and resets variables.
        """
        # Return to login screen and display thank you message
        self.gui.switch_rps_frame("login")
        self.gui.update_msg("Thank you for playing!\nPlease enter a name for P1 and P2", 
                                "rps_login", "system")
        
        # Reset game variables
        self.p1name = None
        self.p2name = None
        self.p1score = 0
        self.p2score = 0
        self.gui.update_rps_score("p1", self.p1score)
        self.gui.update_rps_score("p2", self.p2score)
           
    def select(self, value, player):
        """Handles a player's choice in the Rock Paper Scissors game.

        Sets the chosen value for the specified player and handles game logic when both players have chosen.

        Args:
            value (str): The choice made by the player (e.g., "Rock", "Paper", "Scissors").
            player (str): The player making the choice ("p1" or "p2").
        """
        # Sets player choice and disables selection button
        self.gui.update_rps_segbutton(player, "disabled")
        if player == "p1":
            self.p1choice = value
        elif player == "p2":
            self.p2choice = value
        
        # If both players have chosen, calculates the results
        if self.p1choice and self.p2choice:
            self.results()
        # Otherwise, change the image from waiting to ?
        else:
            self.gui.update_rps_image(player, "?")

    def results(self):
        """Calculates and displays the results of a round of Rock Paper Scissors.

        Calculates the winner based on the players' choices and increments scores. 
        Displays player choices and post-game options.
        """
        # Calculate result using modulus method
        choices = {"Rock": 0, "Paper": 1, "Scissors": 2}
        result = (choices[self.p1choice] - choices[self.p2choice]) % 3

        # Determine winner, increment score, and display results message
        if result == 0:
            self.gui.update_msg("It's a tie!\nPlay again?", "rps_postgame", "system")
        elif result == 1:
            self.p1score += 1
            self.gui.update_rps_score("p1", self.p1score)
            self.gui.update_msg(f"{self.p1name} is the victor!\nPlay again?", "rps_postgame", "system")
        else:
            self.p2score += 1
            self.gui.update_rps_score("p2", self.p2score)
            self.gui.update_msg(f"{self.p2name} is the victor!\nPlay again?", "rps_postgame", "system")
        
        # Display player choices and postgame options
        self.gui.update_rps_image("p1", self.p1choice)
        self.gui.update_rps_image("p2", self.p2choice)
        self.gui.switch_rps_frame("postgame")

        # Reset choices
        self.p1choice = None
        self.p2choice = None
               
         
class MultiplicationTable:
    """Manages Multiplication Table functionality.

    Attributes:
        gui (Gui): Reference to the shared Gui instance.
        username (str): Person generating table.
        multiplier (int): Multiplier to be used in Multiplication Table.
        multiplicand (int): Upper multipicand value.

    Methods:
        generate(): Generates Multiplication Table based on user input.
        is_number(): Checks if a variable is an integer and returns bool.
    """

    def __init__(self, gui):
        """Initializes the MultiplicationTable instance.
        
        Args:
            gui (Gui): Reference to the shared Gui instance.
        """
        self.gui = gui
        self.username = None
        self.multiplier = None
        self.multiplicand = 12
        
    def generate(self):
        """Generates Multiplication Table based on user input.
        
        Checks for valid user input and updates output fields with generated table and msgs.
        """
        # Get input variables from entry fields
        self.username = self.gui.mt_entry_user.get()
        self.multiplier = self.gui.mt_entry_multiplier.get()
        self.multiplicand = int(self.gui.mt_slider_multiplicand.get())
        
        text = ""
        
        # Store invalid fields for accurate error message
        invalid_fields = []
        if not self.username:
            invalid_fields.append("Username empty")
        if not self.multiplier:
            invalid_fields.append("Multiplier empty")
        elif not self.is_number(self.multiplier):
            invalid_fields.append("Multiplier not an integer")
        
        # Validate user input and update output fields
        if invalid_fields:
            error_message = " & ".join(invalid_fields)
            self.gui.update_msg(f"Input Error: Please ensure all fields have correct input\n"
                                f"Fields: {error_message}", 
                                "mt", "error")
        else:
            self.multiplier = int(self.multiplier)
                
            # Generate the multiplication table for every multiplicand in the chosen range
            text += f"{self.username}'s Table:\n\n"
            for multiplicand in range(1, self.multiplicand + 1):
                product = multiplicand * self.multiplier
                text += f"{multiplicand} x {self.multiplier} = {product}\n"
                
            # Display the success msg
            self.gui.update_msg("Multiplication Table has been generated\n" +
                                "Thank you for choosing MidTown IT", "mt", "system")
            
        # Display generated table, or clear out textbox if invalid input   
        self.gui.update_mt_textbox(text)
     
    def is_number(self, value):
        """Checks if a variable is an integer.

        Args:
            value (int): The value to check if is integer.
            
        Returns:
            return (bool): True or false, is value an integer.
        """
        try:
            int(value)
            return True
        except ValueError:
            return False
        
        
class CaesarCipher:
    """Manages Caesar Cipher functionality.

    Attributes:
        gui (Gui): Reference to the shared Gui instance.
        cipherkey (str): Key that will determine the alpha shift.
        plaintext (str): Message to be encrypted, or decrypted message.
        ciphertext (str): Encrypted message, or message to be decrypted.

    Methods:
        encrypt(): Handles retrieval of plaintext and cipher key for encryption.
        decrypt(): Handles retrieval of ciphertext and cipher key for decryption.
        caesar_cipher(): Uses a cipher key to encrypt and decrypt plaintext and ciphertext.
        validate_key(): Ensures cipher key is an integer.
    """

    def __init__(self, gui):
        """Initializes the Caesar Cipher instance.
        
        Args:
            gui (Gui): Reference to the shared Gui instance.
        """
        self.gui = gui
        self.cipherkey = None
        self.plaintext = None
        self.ciphertext = None
        
    def encrypt(self):
        """Handles retrieval of plaintext and cipher key for encryption.
        
        Validates input fields and outputs the encypted plaintext.
        """
        # Get input variables from entry fields
        self.cipherkey = self.gui.cc_entry_key.get()
        self.plaintext = self.gui.cc_textbox_ptext.get(0.0, END).strip().upper()
              
        self.ciphertext = ""      
              
        # Store invalid fields for accurate error message
        invalid_fields = []
        if not self.cipherkey:
            invalid_fields.append("Cipher key empty")
        if not self.plaintext:
            invalid_fields.append("Plaintext empty")
        
        # Validate user input and update output fields
        if invalid_fields:
            error_message = " & ".join(invalid_fields)
            self.gui.update_msg(f"Input Error: Please ensure all fields have correct input\n"
                                f"Fields: {error_message}", 
                                "cc", "error")
        else:    
            # Encrypt the plaintext into cyphertext
            self.ciphertext = self.caesar_cipher(self.plaintext, "encrypt")
            
            # Display the success msg / result of using a multiple of 26 as a key
            if self.cipherkey % 26 == 0:
                self.gui.update_msg("Using a cipher key divisible by 26 results in no change!\n" +
                                    "Alpha characters remain unchanged", "cc", "error")
            else:
                self.gui.update_msg("Plaintext has been encrypted with the cipher key\n" +
                                    "Thank you for choosing MidTown IT", "cc", "system")
        
        # Display generated ciphertext, or clear out output textbox if invalid input 
        self.gui.update_cc_textbox(self.ciphertext, "ctext")
    
    def decrypt(self):
        """Handles retrieval of ciphertext and cipher key for decryption.
        
        Validates input fields and outputs the decrypted ciphertext.
        """
        # Get input variables from entry fields
        self.cipherkey = self.gui.cc_entry_key.get()
        self.ciphertext = self.gui.cc_textbox_ctext.get(0.0, END).strip().upper()
        
        self.plaintext = ""
        
        # Store invalid fields for accurate error message
        invalid_fields = []
        if not self.cipherkey:
            invalid_fields.append("Cipher key empty")
        if not self.ciphertext:
            invalid_fields.append("Ciphertext empty")
        if not self.ciphertext.isalpha():
            invalid_fields.append("Ciphertext contains non-alpha")
        
        # Validate user input and update output fields
        if invalid_fields:
            error_message = " & ".join(invalid_fields)
            self.gui.update_msg(f"Input Error: Please ensure all fields have correct input\n"
                                f"Fields: {error_message}", 
                                "cc", "error")
        else:
            # Decrypt the cyphertext into plaintext
            self.plaintext = self.caesar_cipher(self.ciphertext, "decrypt")
            
            # Display the success msg / result of using a multiple of 26 as a key
            if self.cipherkey % 26 == 0:
                self.gui.update_msg("Using a cipher key divisible by 26 results in no change!\n" +
                                    "Alpha characters remain unchanged", "cc", "error")
            else:
                self.gui.update_msg("Ciphertext has been decrypted with the cipher key\n" +
                                    "Thank you for choosing MidTown IT", "cc", "system")
            
        # Display generated ciphertext, or clear out output textbox if invalid input 
        self.gui.update_cc_textbox(self.plaintext, "ptext")
    
    def caesar_cipher(self, text, dir):
        """Uses a cipher key to encrypt and decrypt plaintext and ciphertext.
        
        Converts only letters using ASCII values and modulus.
        Removes all non-alpha characters and replaces "." with "X"
        
        Args:
            text (str): The text to be encrypted/decrypted..
            dir (str): The direction of the cipher ("encrypt" or "decrypt")
            
        Returns:
            result (str): The encrypted/decrypted text.
        """
        result = ""
        
        self.cipherkey = self.validate_key(self.cipherkey)
        
        for char in text.upper():
            # Only encrypt/decrypt letters and full stop, removing non-alpha characters
            if char.isalpha() or char ==".":
                # Change full stop to "X"
                if char == ".":
                    char = "X"
                # Gets ASCII value of "A" to use as baseline
                base = ord("A")
                # Substracts base from char and adds the cipherkey, giving alpha<->numeric representation
                # of modified char. Using % 26 ensures the cipher loops the alphabetic range.       
                # Adding the base aligns alpha<->numeric representation (1-26) with ASCII values of A-Z
                if dir == "encrypt":
                    modified_char = chr(((ord(char) - base + self.cipherkey) % 26) + base)
                elif dir == "decrypt":
                    modified_char = chr(((ord(char) - base - self.cipherkey) % 26) + base)  
                
                result += modified_char
                
        return result
    
    def validate_key(self, key):
        """Ensures caesar cipher key is valid.
        
        If key provided is not an integer, uses ascii value of characters to create integer.

        Args:
            key (str): The cipher key to be validated/converted.
            
        Returns:
            int_key (int): True or false, is value an integer.
        """
        int_key = 0 
        try:
            int_key = int(key)
        except:
            # For every character in key string, adds ASCII value to int_key
            for char in key:
                int_key += ord(char)
        return int_key
   
     
class App:
    """Manages the MidTown IT Training Solutions application.

    Attributes:
        gui (Gui): Reference to the Gui instance.
        rps (RockPaperScissors): Reference to the RockPaperScissors instance.
        mt (MultiplicationTable): Reference to the MultiplicationTable instance.
        cc (CaesarCipher): Reference to the CaesarCipher instance.
        selected_solution (str): The selected solution name.

    Methods:
        select_solution(): Handles menu item selection.
        on_exit(): Handles application exit.
    """

    def __init__(self):
        """Initializes the App class.

        Configures various settings and defines button commands.
        """
        # Instances of classes
        self.gui = Gui()
        self.rps = RockPaperScissors(self.gui)
        self.mt = MultiplicationTable(self.gui)
        self.cc = CaesarCipher(self.gui)
        
        # Indicates the solution selected from menu sidebar
        self.selected_solution = None
        
        # Gui widget commands and bindings
        for solution_name, menu_button in self.gui.menu_buttons.items():
            menu_button.configure(command=lambda name=solution_name: (self.select_solution(name), 
                                                                      menu_button.focus_set()))
        self.gui.menu_button_exit.configure(command=self.on_exit)
        # Rock Paper Scissors
        self.gui.rps_button_start.configure(command=lambda: (self.gui.rps_button_start.focus_set(),
                                                             self.rps.start()))
        self.gui.rps_entry_p1name.bind("<Return>", lambda event: (self.gui.rps_button_start.focus_set(),
                                                                  self.rps.start()))
        self.gui.rps_entry_p2name.bind("<Return>", lambda event: (self.gui.rps_button_start.focus_set(),
                                                                  self.rps.start()))
        self.gui.rps_button_quit1.configure(command=lambda: (self.gui.rps_button_quit1.focus_set(),
                                                             self.rps.quit()))
        self.gui.rps_button_quit2.configure(command=lambda: (self.gui.rps_button_quit2.focus_set(),
                                                             self.rps.quit()))
        self.gui.rps_button_replay.configure(command=lambda: (self.gui.rps_button_replay.focus_set(),
                                                              self.rps.replay()))
        self.gui.rps_segbutton_p1.configure(command=lambda value, 
                                            player="p1": (self.gui.rps_segbutton_p1.focus_set(),
                                                          self.rps.select(value, player)))
        self.gui.rps_segbutton_p2.configure(command=lambda value, 
                                            player="p2": (self.gui.rps_segbutton_p2.focus_set(),
                                                          self.rps.select(value, player)))
        # Multiplication Table
        self.gui.mt_button_generate.configure(command=lambda: (self.gui.mt_button_generate.focus_set(),
                                                               self.mt.generate()))
        self.gui.mt_entry_user.bind("<Return>", lambda event: (self.gui.mt_button_generate.focus_set(),
                                                               self.mt.generate()))
        self.gui.mt_entry_multiplier.bind("<Return>", lambda event: (self.gui.mt_button_generate.focus_set(),
                                                                     self.mt.generate()))
        # Caesar Cipher
        self.gui.cc_button_encode.configure(command=lambda: (self.gui.cc_button_encode.focus_set(),
                                                             self.cc.encrypt()))
        self.gui.cc_button_decode.configure(command=lambda: (self.gui.cc_button_decode.focus_set(),
                                                             self.cc.decrypt()))
        
        # Enables function on exit and safely close threads
        self.gui.protocol("WM_DELETE_WINDOW", self.on_exit)

    def select_solution(self, solution_name):
        """Event handler for the menu buttons on the menu frame.

        Highlights the selected menu item and changes the screen to selected solution.

        Args:
            solution_name (str): The name of the selected solution.
        """
        # If there is a previously selected solution, set color to default
        if self.selected_solution is not None:
            self.gui.menu_buttons.get(self.selected_solution).configure(fg_color=self.gui.DARKNESS)
            
        # Set color to highlighted and show the selected solution screen
        self.gui.menu_buttons.get(solution_name).configure(fg_color=self.gui.BLUE)
        self.selected_solution = solution_name
        self.gui.show_solution(self.selected_solution)

    def on_exit(self):
        """Called when the program is exited.
        """
        self.gui.destroy()


if __name__ == "__main__":
    app = App()
    app.gui.mainloop()
