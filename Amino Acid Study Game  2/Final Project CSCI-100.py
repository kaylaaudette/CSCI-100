# CSCI-100: Scientific Computing
# Final Project: Amino Acid Adventure
# Kayla Audette
# 4-20-2021




import tkinter as tk  # Importing tkinter for GUI
from PIL import Image, ImageTk  # Importing Image and ImageTk from PIL library for image handling
import random  # Importing random module for shuffling

class AminoAcidsGUI:
    IMAGE_WIDTH = 700  # Width for displaying images
    IMAGE_HEIGHT = 500  # Height for displaying images

    def __init__(self):
        # Initializing the main window
        self.main_window = tk.Tk() 
        # Creating a list of amino acids and shuffling it
        self.amino_acids = list(aminoDict.keys())
        random.shuffle(self.amino_acids)  # Randomize the order of amino acids
        # Initializing index for current amino acid and counter for wrong attempts
        self.aaIndex = 0
        self.wrong_attempts = 0  

        # Creating different frames for organization
        self.create_frames()
        # Loading initial image
        self.load_image()

        # Running the Tkinter main loop
        self.main_window.mainloop()

    def create_frames(self):
        # Creating frames for organizing widgets
        self.title_frame = tk.Frame(self.main_window)
        self.title_frame.pack()
        self.top_frame = tk.Frame(self.main_window)
        self.top_frame.pack()
        self.mid_frame = tk.Frame(self.main_window)
        self.mid_frame.pack()
        self.bottom_frame = tk.Frame(self.main_window)
        self.bottom_frame.pack()
        self.text_frame = tk.Frame(self.main_window)
        self.text_frame.pack()
        self.text2_frame = tk.Frame(self.main_window)
        self.text2_frame.pack()

        # Creating widgets in the frames
        self.create_widgets()

    def create_widgets(self):
        # Creating labels, entry, and button widgets for user interaction
        self.text_title = tk.Label(self.title_frame, text='Amino Acid Adventure')
        self.text_title.pack()

        self.prompt_label = tk.Label(self.mid_frame, text='Enter the Amino Acid Name:')
        self.acid_entry = tk.Entry(self.mid_frame, width=50)
        self.submit_button = tk.Button(self.mid_frame, text='Submit', command=self.clickbutton)

        self.prompt_label.pack(side='left')
        self.acid_entry.pack(side='left')
        self.submit_button.pack(side='left')

        self.hint_label = tk.Label(self.bottom_frame, text='Hint:')
        self.hint_description = tk.Label(self.bottom_frame, text='')

        self.hint_label.pack(side='left')
        self.hint_description.pack(side='left')

        # Adding text labels for instructions
        self.text_i = tk.Label(self.text_frame, text='When the amino acid name is entered correctly, a new one will appear. If it is incorrect, a hint will appear.')
        self.text_i.pack(side='left')

        self.text_p = tk.Label(self.text2_frame, text='After correctly completing all twenty amino acids, hit "submit" to restart the game.')
        self.text_p.pack(side='left')

    def load_image(self):
        # Loading and displaying the image of the current amino acid
        image_path = aminoDict[self.amino_acids[self.aaIndex]][0]
        amino_image = Image.open(image_path)
        amino_image = amino_image.resize((self.IMAGE_WIDTH, self.IMAGE_HEIGHT), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(amino_image)

        self.picture = tk.Label(self.top_frame, image=self.photo)
        self.picture.pack(side='left')

    def clickbutton(self):
        # Handling button click event
        entry = self.acid_entry.get().lower()
        current_amino_acid = self.amino_acids[self.aaIndex]

        if entry == current_amino_acid.lower():
            # If the entered amino acid is correct, update to the next one
            self.aaIndex += 1
            if self.aaIndex < len(self.amino_acids):
                self.update_image()
                self.wrong_attempts = 0  # Reset wrong attempts counter
            else:
                # If all amino acids are correctly guessed, display congratulations message and restart the game
                self.hint_description.config(text='Congratulations! You completed the game.')
                self.aaIndex = 0
                random.shuffle(self.amino_acids)  # Reshuffle amino acids for the next round
        else:
            # If the entered amino acid is incorrect, provide hints
            self.wrong_attempts += 1  # Increment wrong attempts counter
            if self.wrong_attempts == 1:
                # First wrong attempt hint: 1-letter abbreviation
                hint = f"1-letter abbreviation: {aminoDict[current_amino_acid][2]}"
            elif self.wrong_attempts == 2:
                # Second wrong attempt hint: 3-letter abbreviation
                hint = f"3-letter abbreviation: {aminoDict[current_amino_acid][1]}"
            else:
                # Third wrong attempt hint: Full name
                hint = f"Answer: {self.amino_acids[self.aaIndex]}"
                self.wrong_attempts = 0  # Reset wrong attempts counter
            self.hint_description.config(text=hint)

        self.acid_entry.delete(0, tk.END)

    def update_image(self):
        # Updating image to the next amino acid
        self.hint_description.config(text='')

        image_path = aminoDict[self.amino_acids[self.aaIndex]][0]
        amino_image = Image.open(image_path)
        amino_image = amino_image.resize((self.IMAGE_WIDTH, self.IMAGE_HEIGHT), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(amino_image)
        self.picture.config(image=self.photo)

# Dictionary of all amino acids and hints
aminoDict = {
    "Alanine": ["Alanine.jpg", "Ala", "A"],
    "Arginine": ["Arginine.jpg", "Arg", "R"],
    "Asparagine": ["Asparagine.jpg", "Asn", "N"],
    "Aspartic acid": ["Aspartic acid.jpg", "Asp", "D"],
    "Cysteine": ["Cysteine.jpg", "Cys", "C"],
    "Glutamic acid": ["Glutamic acid.jpg", "Glu", "E"],
    "Glutamine": ["Glutamine.jpg", "Gln", "Q"],
    "Glycine": ["Glycine.jpg", "Gly", "G"],
    "Histidine": ["Histidine.jpg", "His", "H"],
    "Isoleucine": ["Isoleucine.jpg", "Ile", "I"],
    "Leucine": ["Leucine.jpg", "Leu", "L"],
    "Lysine": ["Lysine.jpg", "Lys", "K"],
    "Methionine": ["Methionine.jpg", "Met", "M"],
    "Phenylalanine": ["Phenylalanine.jpg", "Phe", "F"],
    "Proline": ["Proline.jpg", "Pro", "P"],
    "Serine": ["Serine.jpg", "Ser", "S"],
    "Threonine": ["Threonine.jpg", "Thr", "T"],
    "Tryptophan": ["Tryptophan.jpg", "Trp", "W"],
    "Tyrosine": ["Tyrosine.jpg", "Tyr", "Y"],
    "Valine": ["Valine.jpg", "Val", "V"],
}

# Create an instance of the AminoAcidsGUI class 
acids = AminoAcidsGUI()


# Works Cited

# * Authors, Multiple. “TkInter.” TkInter - Python Wiki, Python Software Foundation,
#      17 Feb. 2021, 11:09:08, wiki.python.org/moin/TkInter.

# * M, Remi. “How To Add Images In Tkinter - Using The Python Pillow Package.” ActiveState,
#      21 Apr. 2021, www.activestate.com/resources/quick-reads/how-to-add-images-in-tkinter/. 

# * all photos of amino acids from Wikipedia *
# * started with the kilo converter templ
