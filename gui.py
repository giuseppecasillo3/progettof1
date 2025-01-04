import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from funzioni import *


from progetto import *
from cerca import *
from pole_winner import *
from posizioni_guadagnate import *
import pandas as pd

class F1StatsApp:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.root = ctk.CTk()
        self.root.title("Formula 1 Statistics Analyzer")
        self.root.geometry("1400x800")
        
        # Set color scheme
        self.primary_color = "#FF1E1E"  # Bright F1 red
        self.secondary_color = "#1E1E1E"  # Dark gray
        self.accent_color = "#00FF00"  # Bright green for values
        self.text_color = "white"
        self.highlight_color = "#FFD700"  # Gold for highlights
        
        # Create main container
        self.main_container = ctk.CTkFrame(self.root)
        self.main_container.pack(fill="both", expand=True)
        
        # Create sidebar
        self.sidebar = ctk.CTkFrame(self.main_container, fg_color=self.primary_color, width=200)
        self.sidebar.pack(side="left", fill="y", padx=10, pady=20)
        self.sidebar.pack_propagate(False)  # Prevent sidebar from shrinking
        self.create_sidebar()
        
        # Create main content area
        self.main_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.main_frame.pack(side="left", fill="both", expand=True, padx=10, pady=20)
        
        # Create results area (full height, right side)
        self.results_frame = ctk.CTkFrame(self.main_container, fg_color=self.secondary_color, width=600)
        self.results_frame.pack(side="right", fill="both", expand=True, padx=10, pady=20)
        
        # Initialize frames
        self.frames = {}
        self.current_frame = None
        self.setup_circuit_frame()
        self.setup_constructor_frame()
        self.setup_driver_frame()
        self.setup_race_frame()

    def create_sidebar(self):
        # Title
        title = ctk.CTkLabel(
            self.sidebar,
            text="F1 Stats",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=self.text_color
        )
        title.pack(pady=20)
        
        # Navigation buttons
        buttons = [
            ("Circuits", lambda: self.show_frame("circuit")),
            ("Constructors", lambda: self.show_frame("constructor")),
            ("Drivers", lambda: self.show_frame("driver")),
            ("Races", lambda: self.show_frame("race"))
        ]
        
        for text, command in buttons:
            btn = ctk.CTkButton(
                self.sidebar,
                text=text,
                command=command,
                fg_color=self.secondary_color,
                hover_color=self.accent_color
            )
            btn.pack(pady=5, padx=20, fill="x")

    def create_entry_with_label(self, parent, label_text, placeholder_text):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", pady=5, padx=20)
        
        label = ctk.CTkLabel(frame, text=label_text, 
                           font=ctk.CTkFont(size=12),
                           text_color=self.text_color)
        label.pack(anchor="w")
        
        entry = ctk.CTkEntry(frame, 
                           placeholder_text=placeholder_text,
                           fg_color=self.secondary_color,
                           text_color=self.text_color,
                           border_color=self.primary_color)
        entry.pack(fill="x", pady=(5, 0))
        
        return entry

    def create_action_button(self, parent, text, command):
        return ctk.CTkButton(parent,
                           text=text,
                           command=command,
                           fg_color=self.primary_color,
                           hover_color=self.accent_color,
                           text_color=self.text_color,
                           font=ctk.CTkFont(size=12, weight="bold"),
                           corner_radius=10,
                           height=40)

    def create_nav_button(self, parent, text, command):
        return ctk.CTkButton(parent,
                           text=text,
                           command=command,
                           fg_color="transparent",
                           hover_color=self.accent_color,
                           text_color=self.text_color,
                           font=ctk.CTkFont(size=14))

    def show_frame(self, frame_name):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = self.frames[frame_name]
        self.current_frame.pack(fill="both", expand=True)

    def setup_circuit_frame(self):
        frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        
        # Title
        title = ctk.CTkLabel(frame,
                           text="Circuit Analysis",
                           font=ctk.CTkFont(size=20, weight="bold"),
                           text_color=self.text_color)
        title.pack(pady=20)
        
        # Entry
        self.circuit_entry = self.create_entry_with_label(frame,
                                                      "Circuit Name",
                                                      "Enter circuit name...")
        
        # Buttons frame
        buttons_frame = ctk.CTkFrame(frame, fg_color="transparent")
        buttons_frame.pack(fill="x", pady=20)
        
        # Action buttons
        self.create_action_button(buttons_frame,
                               "Show Circuit Hall of Fame",
                               self.show_circuit_hall_of_fame).pack(pady=10, fill="x")
        
        self.frames["circuit"] = frame

    def setup_constructor_frame(self):
        frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        
        # Title
        title = ctk.CTkLabel(frame,
                           text="Constructor Analysis",
                           font=ctk.CTkFont(size=20, weight="bold"),
                           text_color=self.text_color)
        title.pack(pady=20)
        
        # Entries
        self.constructor_entry = self.create_entry_with_label(frame,
                                                         "Constructor Name",
                                                         "Enter constructor name...")
        
        self.circuit_entry_constructor = self.create_entry_with_label(frame,
                                                                  "Circuit Name",
                                                                  "Enter circuit name...")
        
        # Buttons frame
        buttons_frame = ctk.CTkFrame(frame, fg_color="transparent")
        buttons_frame.pack(fill="x", pady=20)
        
        # Action buttons
        self.create_action_button(buttons_frame,
                               "Show Constructor Drivers",
                               self.show_constructor_drivers).pack(pady=10, fill="x")
        
        self.create_action_button(buttons_frame,
                               "Show Points at Circuit",
                               self.show_constructor_circuit_points).pack(pady=10, fill="x")
        
        self.create_action_button(buttons_frame,
                               "Show Season Points Trend",
                               self.show_constructor_season_points).pack(pady=10, fill="x")
        
        self.frames["constructor"] = frame

    def setup_driver_frame(self):
        frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        
        # Title
        title = ctk.CTkLabel(frame,
                           text="Driver Analysis",
                           font=ctk.CTkFont(size=20, weight="bold"),
                           text_color=self.text_color)
        title.pack(pady=20)
        
        # Entries
        self.driver_name_entry = self.create_entry_with_label(frame,
                                                          "Driver Name",
                                                          "Enter driver first name...")
        
        self.driver_surname_entry = self.create_entry_with_label(frame,
                                                             "Driver Surname",
                                                             "Enter driver surname...")
        
        self.circuit_entry_driver = self.create_entry_with_label(frame,
                                                              "Circuit Name",
                                                              "Enter circuit name...")
        
        # Buttons frame
        buttons_frame = ctk.CTkFrame(frame, fg_color="transparent")
        buttons_frame.pack(fill="x", pady=20)
        
        # Action buttons
        self.create_action_button(buttons_frame,
                               "Show Win Percentage and Podiums",
                               self.show_win_percentage).pack(pady=10, fill="x")
        
        self.create_action_button(buttons_frame,
                               "Show Race Duration Trend",
                               self.show_race_duration).pack(pady=10, fill="x")
        
        self.create_action_button(buttons_frame,
                               "Show Pit Stop Trend",
                               self.show_pitstop_trend).pack(pady=10, fill="x")
        
        self.create_action_button(buttons_frame,
                               "Show Position Trend at Circuit",
                               self.show_position_trend).pack(pady=10, fill="x")
        
        self.create_action_button(buttons_frame,
                               "Show Average Position Trend",
                               self.show_avg_position).pack(pady=10, fill="x")
        
        self.frames["driver"] = frame

    def setup_race_frame(self):
        frame = ctk.CTkFrame(self.main_frame)
        
        # Title
        title = ctk.CTkLabel(
            frame,
            text="Race Analysis",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=20)
        
        # Year input
        year_label = ctk.CTkLabel(frame, text="Year:")
        year_label.pack()
        self.year_entry = ctk.CTkEntry(frame)
        self.year_entry.pack(pady=(0, 10))
        
        # Circuit input
        circuit_label = ctk.CTkLabel(frame, text="Circuit:")
        circuit_label.pack()
        self.circuit_entry_race = ctk.CTkEntry(frame)
        self.circuit_entry_race.pack(pady=(0, 10))
        
        # Driver name input for position changes
        driver_name_label = ctk.CTkLabel(frame, text="Driver Name:")
        driver_name_label.pack()
        self.driver_name_entry_race = ctk.CTkEntry(frame)
        self.driver_name_entry_race.pack(pady=(0, 10))
        
        # Driver surname input for position changes
        driver_surname_label = ctk.CTkLabel(frame, text="Driver Surname:")
        driver_surname_label.pack()
        self.driver_surname_entry_race = ctk.CTkEntry(frame)
        self.driver_surname_entry_race.pack(pady=(0, 20))
        
        # Buttons
        pole_button = ctk.CTkButton(
            frame,
            text="Show Pole Winner",
            command=self.show_pole_winner,
            fg_color=self.primary_color,
            hover_color=self.accent_color
        )
        pole_button.pack(pady=5)
        
        position_button = ctk.CTkButton(
            frame,
            text="Show Position Changes",
            command=self.show_position_changes,
            fg_color=self.primary_color,
            hover_color=self.accent_color
        )
        position_button.pack(pady=5)
        
        winner_button = ctk.CTkButton(
            frame,
            text="Show Race Winner",
            command=self.show_race_winner,
            fg_color=self.primary_color,
            hover_color=self.accent_color
        )
        winner_button.pack(pady=5)
        
        self.frames["race"] = frame

    def show_pole_winner(self):
        year = self.year_entry.get().strip()
        circuit = self.circuit_entry_race.get().strip()
        
        if year and circuit:
            try:
                # Clear previous results
                for widget in self.results_frame.winfo_children():
                    widget.destroy()
                
                # Create scrollable frame for results
                scroll_frame = ctk.CTkScrollableFrame(
                    self.results_frame,
                    fg_color=self.secondary_color
                )
                scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)
                
                # Header
                header_frame = ctk.CTkFrame(scroll_frame, fg_color=self.primary_color, height=100)
                header_frame.pack(fill="x", padx=5, pady=10)
                header_frame.pack_propagate(False)
                
                ctk.CTkLabel(
                    header_frame,
                    text="🏁 Pole Position",
                    font=ctk.CTkFont(size=32, weight="bold"),
                    text_color=self.text_color
                ).pack(pady=(5,0))
                
                ctk.CTkLabel(
                    header_frame,
                    text=f"{circuit} {year}",
                    font=ctk.CTkFont(size=24),
                    text_color=self.text_color
                ).pack(pady=(0,5))
                
                # Get pole winner
                get_pole_winner = pole_winner(int(year), circuit)
                
                if get_pole_winner:
                    # Winner box
                    winner_box = ctk.CTkFrame(scroll_frame, fg_color=self.primary_color)
                    winner_box.pack(fill="x", pady=5, padx=5)
                    
                    ctk.CTkLabel(
                        winner_box,
                        text=get_pole_winner,
                        font=ctk.CTkFont(size=28, weight="bold"),
                        text_color=self.accent_color
                    ).pack(pady=20)
                else:
                    ctk.CTkLabel(
                        scroll_frame,
                        text="No data found for this race",
                        font=ctk.CTkFont(size=16),
                        text_color=self.accent_color
                    ).pack(pady=10)
                
            except ValueError:
                messagebox.showerror("Error", "Year must be a valid number")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Required", "Please enter both year and circuit name")

    def show_race_winner(self):
        year = self.year_entry.get().strip()
        circuit = self.circuit_entry_race.get().strip()
        
        if year and circuit:
            try:
                import sys
                import io
                # Capture print output
                old_stdout = sys.stdout
                result_stream = io.StringIO()
                sys.stdout = result_stream
                
                # Call the function
                vincitore_gara(int(year), circuit)
                
                # Get the output and parse it
                result = result_stream.getvalue()
                sys.stdout = old_stdout
                
                # Parse the results into a dictionary
                lines = result.strip().split("\n")
                stats = {
                    "Race": f"{circuit} {year}",
                    "Winner": lines[-1] if lines else "Not found"
                }
                
                # Show in GUI format
                self.show_list_result("Race Winner", [stats["Winner"]])
            except ValueError:
                messagebox.showerror("Error", "Year must be a valid number")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Required", "Please enter both year and circuit name")

    def show_list_result(self, title, items):
        # Clear previous results
        for widget in self.results_frame.winfo_children():
            widget.destroy()
        
        # Create scrollable frame for results
        scroll_frame = ctk.CTkScrollableFrame(
            self.results_frame,
            fg_color=self.secondary_color
        )
        scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Header
        header_frame = ctk.CTkFrame(scroll_frame, fg_color=self.primary_color, height=100)
        header_frame.pack(fill="x", padx=5, pady=10)
        header_frame.pack_propagate(False)
        
        ctk.CTkLabel(
            header_frame,
            text=title,
            font=ctk.CTkFont(size=32, weight="bold"),
            text_color=self.text_color
        ).pack(pady=20)
        
        # Results box
        if items:
            results_box = ctk.CTkFrame(scroll_frame, fg_color=self.primary_color)
            results_box.pack(fill="x", pady=5, padx=5)
            
            for item in items:
                ctk.CTkLabel(
                    results_box,
                    text=item,
                    font=ctk.CTkFont(size=16),
                    text_color=self.accent_color
                ).pack(pady=5)
        else:
            ctk.CTkLabel(
                scroll_frame,
                text="No data found",
                font=ctk.CTkFont(size=16),
                text_color=self.accent_color
            ).pack(pady=10)

    def show_win_percentage(self):
        name = self.driver_name_entry.get().strip()
        surname = self.driver_surname_entry.get().strip()
        if name and surname:
            try:
                # Get driver ID and stats
                id_pilota = Cerca_ID_pilota(name, surname)
                gare_vinte = Conta_vittorie_pilota(id_pilota)
                numero_podi = Conta_Podi(id_pilota)
                
                # Clear previous widgets
                for widget in self.results_frame.winfo_children():
                    widget.destroy()
                
                # Create title
                title = ctk.CTkLabel(
                    self.results_frame,
                    text=f"Statistics for {name} {surname}",
                    font=ctk.CTkFont(size=24, weight="bold"),
                    text_color=self.text_color
                )
                title.pack(pady=20)
                
                # Create stats frame
                stats_frame = ctk.CTkFrame(self.results_frame)
                stats_frame.pack(fill="both", expand=True, padx=20, pady=20)
                
                # Total races
                races_frame = ctk.CTkFrame(stats_frame, fg_color=self.primary_color)
                races_frame.pack(fill="x", padx=10, pady=5)
                ctk.CTkLabel(
                    races_frame,
                    text="Total Races:",
                    font=ctk.CTkFont(size=16, weight="bold"),
                    text_color=self.text_color
                ).pack(side="left", padx=10)
                ctk.CTkLabel(
                    races_frame,
                    text=str(gare_vinte[0]),
                    font=ctk.CTkFont(size=16),
                    text_color=self.accent_color
                ).pack(side="right", padx=10)
                
                # Podiums
                podiums_frame = ctk.CTkFrame(stats_frame, fg_color=self.primary_color)
                podiums_frame.pack(fill="x", padx=10, pady=5)
                ctk.CTkLabel(
                    podiums_frame,
                    text="Total Podiums:",
                    font=ctk.CTkFont(size=16, weight="bold"),
                    text_color=self.text_color
                ).pack(side="left", padx=10)
                ctk.CTkLabel(
                    podiums_frame,
                    text=str(numero_podi),
                    font=ctk.CTkFont(size=16),
                    text_color=self.accent_color
                ).pack(side="right", padx=10)
                
                # Wins
                wins_frame = ctk.CTkFrame(stats_frame, fg_color=self.primary_color)
                wins_frame.pack(fill="x", padx=10, pady=5)
                ctk.CTkLabel(
                    wins_frame,
                    text="Race Wins:",
                    font=ctk.CTkFont(size=16, weight="bold"),
                    text_color=self.text_color
                ).pack(side="left", padx=10)
                ctk.CTkLabel(
                    wins_frame,
                    text=str(gare_vinte[1]),
                    font=ctk.CTkFont(size=16),
                    text_color=self.accent_color
                ).pack(side="right", padx=10)
                
                # Win percentage
                if gare_vinte[1] > 0:  # Only show if they have wins
                    percent_frame = ctk.CTkFrame(stats_frame, fg_color=self.primary_color)
                    percent_frame.pack(fill="x", padx=10, pady=5)
                    ctk.CTkLabel(
                        percent_frame,
                        text="Win Percentage:",
                        font=ctk.CTkFont(size=16, weight="bold"),
                        text_color=self.text_color
                    ).pack(side="left", padx=10)
                    ctk.CTkLabel(
                        percent_frame,
                        text=f"{gare_vinte[2]}%",
                        font=ctk.CTkFont(size=16),
                        text_color=self.accent_color
                    ).pack(side="right", padx=10)
                
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Required", "Please enter both driver name and surname")

    def show_position_changes(self):
        year = self.year_entry.get().strip()
        circuit = self.circuit_entry_race.get().strip()
        name = self.driver_name_entry_race.get().strip()
        surname = self.driver_surname_entry_race.get().strip()
        
        if year and circuit and name and surname:
            try:
                # Clear previous results
                for widget in self.results_frame.winfo_children():
                    widget.destroy()
                
                # Create scrollable frame for results
                scroll_frame = ctk.CTkScrollableFrame(
                    self.results_frame,
                    fg_color=self.secondary_color
                )
                scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)
                
                # Header with circuit and driver name
                header_frame = ctk.CTkFrame(scroll_frame, fg_color=self.primary_color, height=100)
                header_frame.pack(fill="x", padx=5, pady=10)
                header_frame.pack_propagate(False)
                
                ctk.CTkLabel(
                    header_frame,
                    text=f"🏎️ {name} {surname}",
                    font=ctk.CTkFont(size=32, weight="bold"),
                    text_color=self.text_color
                ).pack(pady=(5,0))
                
                ctk.CTkLabel(
                    header_frame,
                    text=f"at {circuit} {year}",
                    font=ctk.CTkFont(size=24),
                    text_color=self.text_color
                ).pack(pady=(0,5))
                
                # Stats container
                stats_container = ctk.CTkFrame(scroll_frame, fg_color="transparent")
                stats_container.pack(fill="x", padx=5, pady=5)
                
                # Position Changes Box
                position_changes_box = ctk.CTkFrame(stats_container, fg_color=self.primary_color)
                position_changes_box.pack(fill="x", pady=5)
                
                position_changes_title = ctk.CTkLabel(
                    position_changes_box,
                    text="Position Changes",
                    font=ctk.CTkFont(size=20, weight="bold"),
                    text_color=self.text_color
                )
                position_changes_title.pack(pady=(10,0))
                
                # Get position changes
                changes = differenza_posizioni(int(year), circuit, name, surname)
                
                if isinstance(changes, dict) and 'start' in changes and 'finish' in changes:
                    # Starting position
                    start_frame = ctk.CTkFrame(position_changes_box, fg_color="transparent")
                    start_frame.pack(fill="x", pady=5, padx=20)
                    
                    ctk.CTkLabel(
                        start_frame,
                        text="Started:",
                        font=ctk.CTkFont(size=16, weight="bold"),
                        text_color=self.text_color
                    ).pack(side="left", padx=5)
                    
                    ctk.CTkLabel(
                        start_frame,
                        text=f"P{changes['start']}",
                        font=ctk.CTkFont(size=16),
                        text_color=self.accent_color
                    ).pack(side="right", padx=5)
                    
                    # Finish position
                    finish_frame = ctk.CTkFrame(position_changes_box, fg_color="transparent")
                    finish_frame.pack(fill="x", pady=5, padx=20)
                    
                    ctk.CTkLabel(
                        finish_frame,
                        text="Finished:",
                        font=ctk.CTkFont(size=16, weight="bold"),
                        text_color=self.text_color
                    ).pack(side="left", padx=5)
                    
                    ctk.CTkLabel(
                        finish_frame,
                        text=f"P{changes['finish']}",
                        font=ctk.CTkFont(size=16),
                        text_color=self.accent_color
                    ).pack(side="right", padx=5)
                    
                    # Positions gained/lost
                    diff = changes['start'] - changes['finish']
                    diff_text = f"Gained {abs(diff)}" if diff > 0 else f"Lost {abs(diff)}" if diff < 0 else "Maintained position"
                    diff_color = "#00FF00" if diff > 0 else "#FF0000" if diff < 0 else self.accent_color
                    
                    positions_frame = ctk.CTkFrame(position_changes_box, fg_color="transparent")
                    positions_frame.pack(fill="x", pady=10, padx=20)
                    
                    ctk.CTkLabel(
                        positions_frame,
                        text=diff_text,
                        font=ctk.CTkFont(size=24, weight="bold"),
                        text_color=diff_color
                    ).pack()
                    
                    if diff != 0:
                        ctk.CTkLabel(
                            positions_frame,
                            text="positions",
                            font=ctk.CTkFont(size=16),
                            text_color=self.text_color
                        ).pack()
                else:
                    ctk.CTkLabel(
                        position_changes_box,
                        text="No data found for this race",
                        font=ctk.CTkFont(size=16),
                        text_color=self.accent_color
                    ).pack(pady=10)
                
            except ValueError:
                messagebox.showerror("Error", "Year must be a valid number")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Required", "Please enter year, circuit, driver name and surname")

    def show_race_winner(self):
        year = self.year_entry.get().strip()
        circuit = self.circuit_entry_race.get().strip()
        if year and circuit:
            try:
                import sys
                import io
                # Capture print output
                old_stdout = sys.stdout
                result_stream = io.StringIO()
                sys.stdout = result_stream
                
                # Call the function
                vincitore_gara(int(year), circuit)
                
                # Get the output and parse it
                result = result_stream.getvalue()
                sys.stdout = old_stdout
                
                # Parse the results into a dictionary
                lines = result.strip().split("\n")
                stats = {
                    "Race": f"{circuit} {year}",
                    "Winner": lines[-1] if lines else "Not found"
                }
                
                # Show in GUI format
                self.show_list_result("Race Winner", [stats["Winner"]])
            except ValueError:
                messagebox.showerror("Error", "Year must be a valid number")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Required", "Please enter both year and circuit name")

    def show_constructor_drivers(self):
        constructor = self.constructor_entry.get().strip()
        if constructor:
            try:
                import sys
                import io
                # Capture print output
                old_stdout = sys.stdout
                result_stream = io.StringIO()
                sys.stdout = result_stream
                
                # Call the function
                Piloti_per_scuderia(constructor)
                
                # Get the output
                result = result_stream.getvalue()
                sys.stdout = old_stdout
                
                # Show the result in the text display
                self.show_list_result("Drivers for " + constructor, result.strip().split("\n"))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Required", "Please enter a constructor name")

    def show_constructor_circuit_points(self):
        constructor = self.constructor_entry.get().strip()
        circuit = self.circuit_entry_constructor.get().strip()
        if constructor and circuit:
            try:
                plt.clf()  # Clear any existing plots
                circuit_id = Cerca_ID_circuito(circuit)[0]  # Get only the ID
                constructor_id = Cerca_ID_scuderia(constructor)
                if constructor_id is not None and circuit_id is not None:
                    grafico_punti_scuderia(constructor_id, circuit_id)
                    self.show_plot(plt.gcf())
                else:
                    messagebox.showwarning("Not Found", "Constructor or circuit not found")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Required", "Please enter both constructor and circuit names")

    def show_constructor_season_points(self):
        constructor = self.constructor_entry.get().strip()
        if constructor:
            try:
                plt.clf()  # Clear any existing plots
                constructor_id = Cerca_ID_scuderia(constructor)
                if constructor_id is not None:
                    grafico_punti_totali_scuderia(constructor_id)
                    self.show_plot(plt.gcf())
                else:
                    messagebox.showwarning("Not Found", "Constructor not found")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Required", "Please enter a constructor name")

    def show_race_duration(self):
        name = self.driver_name_entry.get().strip()
        surname = self.driver_surname_entry.get().strip()
        circuit = self.circuit_entry_driver.get().strip()
        if name and surname and circuit:
            try:
                plt.clf()  # Clear any existing plots
                driver_id = Cerca_ID_pilota(name, surname)
                circuit_id = Cerca_ID_circuito(circuit)[0]
                if driver_id is not None and circuit_id is not None:
                    grafico_durata_gara(driver_id, circuit_id)
                    self.show_plot(plt.gcf())
                else:
                    messagebox.showwarning("Not Found", "Driver or circuit not found")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Required", "Please enter driver name, surname and circuit name")

    def show_pitstop_trend(self):
        name = self.driver_name_entry.get().strip()
        surname = self.driver_surname_entry.get().strip()
        if name and surname:
            try:
                plt.clf()  # Clear any existing plots
                driver_id = Cerca_ID_pilota(name, surname)
                if driver_id is not None:
                    grafico_media_pit_stop(driver_id)
                    self.show_plot(plt.gcf())
                else:
                    messagebox.showwarning("Not Found", "Driver not found")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Required", "Please enter both driver name and surname")

    def show_position_trend(self):
        name = self.driver_name_entry.get().strip()
        surname = self.driver_surname_entry.get().strip()
        circuit = self.circuit_entry_driver.get().strip()
        if name and surname and circuit:
            try:
                plt.clf()  # Clear any existing plots
                driver_id = Cerca_ID_pilota(name, surname)
                circuit_id = Cerca_ID_circuito(circuit)[0]
                if driver_id is not None and circuit_id is not None:
                    grafico_andamento_posizione_circuito(driver_id, circuit_id)
                    self.show_plot(plt.gcf())
                else:
                    messagebox.showwarning("Not Found", "Driver or circuit not found")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Required", "Please enter driver name, surname and circuit name")

    def show_avg_position(self):
        name = self.driver_name_entry.get().strip()
        surname = self.driver_surname_entry.get().strip()
        if name and surname:
            try:
                plt.clf()  # Clear any existing plots
                driver_id = Cerca_ID_pilota(name, surname)
                if driver_id is not None:
                    grafico_posizione_media(driver_id)
                    self.show_plot(plt.gcf())
                else:
                    messagebox.showwarning("Not Found", "Driver not found")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Required", "Please enter both driver name and surname")

    def show_circuit_hall_of_fame(self):
        circuit = self.circuit_entry.get().strip()
        if circuit:
            try:
                import sys
                import io
                # Capture print output
                old_stdout = sys.stdout
                result_stream = io.StringIO()
                sys.stdout = result_stream
                
                # Call the function
                Albo_oro_circuito(circuit)
                
                # Get the output
                result = result_stream.getvalue()
                sys.stdout = old_stdout
                
                # Show the result in the text display
                self.show_list_result("Hall of Fame for " + circuit, result.strip().split("\n"))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Required", "Please enter a circuit name")

    def show_plot(self, figure):
        # Hide text display
        #self.text_display.pack_forget()
        
        # Clear any existing widgets in results frame
        for widget in self.results_frame.winfo_children():
            if isinstance(widget, ctk.CTkCanvas):
                widget.destroy()
        
        # Style the plot
        figure.patch.set_facecolor(self.secondary_color)
        for ax in figure.get_axes():
            ax.set_facecolor(self.secondary_color)
            ax.spines['bottom'].set_color(self.text_color)
            ax.spines['top'].set_color(self.text_color)
            ax.spines['left'].set_color(self.text_color)
            ax.spines['right'].set_color(self.text_color)
            ax.tick_params(colors=self.text_color)
            ax.xaxis.label.set_color(self.text_color)
            ax.yaxis.label.set_color(self.text_color)
            ax.title.set_color(self.text_color)
        
        # Create canvas and show new plot
        canvas = FigureCanvasTkAgg(figure, self.results_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

def main():
    app = F1StatsApp()
    app.root.mainloop()

if __name__ == "__main__":
    main()
