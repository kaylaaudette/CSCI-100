# Kayla Audette, Kayla Bertholf, William Bodary

# Kayla A- I started with the kilo converter template and formatted it to show the
# the windows seen in this studying game. I then used pillow and tinker to add an image
# and resized it to a window. I then download 20 amino acid photos and edited them to 
# fit the window properly when called. I then added an if statement that recognizes
# the amino acid entry of single amino acid and moves it one another amino acid. However
# I couldn't get it to go through more than two. Then I added descriptions to the code I wrote.  

# Kayla B- Came up with ideas and performed troubleshooting of how to iterate through the
# amino acids. Through this, I found out what did not work to make the functions iterate
# through the hints and amino acid images. I then worked with Will to correct what I
# found that did not work. I then made an amino acid dictionary and implemented its use. 
# The dictionary has a key that is the amino acid image name and a value that is a list of lists. 
# Then I added descriptions to the code I wrote. 

# Will B- I got the submit button to have some functionality, getting it to show a muliplte new
# image when pressed. I also got the game to iterate through all amino acids rather than just one.
# I did this by implementing the index for the current amino acid and accessing the proper dictionary
# entry at that index. I then got the hints and user input to go away when switching to the next amino
# acid.I added describtions to the code I wrote. 

import tkinter
from tkinter import * 
from PIL import Image, ImageTk

# Dictionary of all amino acids and hints (key)
aminoDict = {"Alanine.jpg": ["Alanine", "Ala"],
    "Arginine.jpg": ["Arginine", "Arg"],
    "Asparagine.jpg": ["Asparagine", "Asn"],
    "Aspartic acid.jpg": ["Aspartic acid", "Asp"],
    "Cysteine.jpg": ["Cysteine", "Cys"],
    "Glutamic Acid.jpg": ["Glutamic Acid", "Glu"],
    "Glutamine.jpg": ["Glutamine", "Gln"],
    "Glycine.jpg": ["Glycine", "Gly"],
    "Histidine.jpg": ["Histidine", "His"],
    "Isoleucine.jpg": ["Isoleucine", "Ile"],
    "Leucine.jpg": ["Leucine", "Leu"],
    "Lysine.jpg": ["Lysine", "Lys"],
    "Methionine.jpg": ["Methionine", "Met"],
    "Phenylalanine.jpg": ["Phenylalanine", "Phe"],
    "Proline.jpg": ["Proline", "Pro"],
    "Serine.jpg": ["Serine", "Ser"],
    "Threonine.jpg": ["Threonine", "Thr"],
    "Tryptophan.jpg": ["Tryptophan", "Trp"],
    "Tyrosine.jpg": ["Tyrosine", "Tyr"],
    "Valine.jpg": ["Valine", "Val"],
    "Well Done.jpg": ["", "well done"]
    }

class AminoAcidsGUI:
    
    # constructor
    def __init__(self):

        # creates the main window
        self.main_window = tkinter.Tk() 
        
        # keeps track of the currently displayed amino acid
        self.aaIndex = 0

        # creates the frames to group widgets
        self.title_frame = tkinter.Frame()
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        self.text_frame = tkinter.Frame()
        self.text2_frame = tkinter.Frame()
        
        # calls first amino acid image
        Alanine = Image.open("Alanine.jpg")
        Alanine = Alanine.resize((700, 500), Image.ANTIALIAS)
        photo1 =  ImageTk.PhotoImage(Alanine)
        
        # creates the widget for the top frame
        self.picture = tkinter.Label(self.top_frame, image = photo1) 
        
        # packs top frame widget
        self.picture.pack(side='left')
        
        # calling all of the widget functions 
        self.titleframe()
        self.middleframe()
        self.bottomframe()
        self.textframe1()
        self.textframe2()

        # packs the buttons and frames organizing them into blocks
        self.title_frame.pack()
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        self.text_frame.pack()
        self.text2_frame.pack()
    
        # enter the tkinter main loop
        tkinter.mainloop()
            
    def titleframe(self):
        # creates the widget for the title frame
        self.text_title = tkinter.Label(self.title_frame, text ='Amino Acid Adventure ')
        
        # packs title frame widget
        self.text_title.pack(side='left')
              
        
    def middleframe(self):
        # creates the widgets for the middle frame 
        self.prompt_label = tkinter.Label(self.mid_frame,text='Enter the Amino Acid Name:')
        self.hint = tkinter.StringVar()
        self.acid_entry = tkinter.Entry(self.mid_frame, width=50)
        self.submit_button = tkinter.Button(self.mid_frame,text='Submit',command = self.clickbutton )
        
        # packs the mid frame's widget's  
        self.prompt_label.pack(side='left')
        self.acid_entry.pack(side='left')
        self.submit_button.pack(side='left')
        
    def bottomframe(self):
        # creates the widgets for the bottom frame 
        self.hint_label = tkinter.Label(self.bottom_frame,text = 'Hint:')
        self.hint_description = tkinter.Label(self.bottom_frame, textvariable=self.hint)
        
        # packs the bottom frame widget's
        self.hint_label.pack(side='left')
        self.hint_description.pack(side='left')
        
    def textframe1(self):
        # creates the widgets for the text
        self.text_i = tkinter.Label(self.text_frame, \
                                        text ='When the amino acid name is entered correctly a new one will appear, however if it is incorrect a hint will appear.')
        # packs the texts widget
        self.text_i.pack(side='left')
        
    def textframe2(self):
        # creates the widgets for the text
        self.text_p = tkinter.Label(self.text2_frame, \
                                            text ='After correctly completing all twenty amino acids hit "submit" to restart the game.')
        # packs the texts widget
        self.text_p.pack(side='left')
        
    # callback of the button fuction 
    def clickbutton(self):
        
        # reads user input 
        Entry = str(self.acid_entry.get())
        
        # grabbing list of all keys and values from amino acid dictionary
        aaPictures = list(aminoDict.keys())
        aminoAcids = list(aminoDict.values())
        
        # accessing amino acid name for current entry  
        currentAminoAcid = aminoAcids[self.aaIndex][0]
        
        # checking the user input if correct 
        if Entry == currentAminoAcid or Entry == currentAminoAcid.lower(): 
            
            # checks user input of first 21 dictionary entries 
            if self.aaIndex < 20:
                
                # resets entry and hint to be blank 
                self.acid_entry.delete(0, len(Entry))
                self.hint.set('')
                self.aaIndex += 1
                
                # opens and resizes next amino acid image 
                nextAA = Image.open(aaPictures[self.aaIndex])
                nextAA = nextAA.resize((700, 500), Image.ANTIALIAS)
                photo2 =  ImageTk.PhotoImage(nextAA)
                self.picture.configure(image=photo2)
                self.picture.image=photo2
            
            # resets the game
            else:
                
                # resets entry and hint to be blank
                self.acid_entry.delete(0, len(Entry))
                self.hint.set('')
                self.aaIndex = 0
                
                # accessing amino acid name for current entry 
                currentAminoAcid = aminoAcids[self.aaIndex][0]
                
                # opens and resizes next amino acid image 
                nextAA = Image.open(aaPictures[self.aaIndex])
                nextAA = nextAA.resize((700, 500), Image.ANTIALIAS)
                photo2 = ImageTk.PhotoImage(nextAA)
                self.picture.configure(image=photo2)
                self.picture.image=photo2
                
        # checking the user input if incorrect
        else:
            
            # returns key (hint) 
            return self.hint.set(aminoAcids[self.aaIndex][1])
    
            
# create an instance of the AminoAcidsGUI class 
acids = AminoAcidsGUI()

# Works Cited

# * Authors, Multiple. “TkInter.” TkInter - Python Wiki, Python Software Foundation,
#      17 Feb. 2021, 11:09:08, wiki.python.org/moin/TkInter.

# * M, Remi. “How To Add Images In Tkinter - Using The Python Pillow Package.” ActiveState,
#      21 Apr. 2021, www.activestate.com/resources/quick-reads/how-to-add-images-in-tkinter/. 

# * all photos of amino acids from Wikipedia *
# * started with the kilo converter template *