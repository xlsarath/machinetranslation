#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module documentation goes here
   and here
   and ...
"""

from googletrans import Translator
import sys
import os
from tkinter import *
from tkinter import messagebox
from functools import partial


def process(text,lang):
	"""
	Processes the user given phrase & language parameters to generate speech output

	parameters
	------------------------------------------------
	text: str
		The input phrase in English given by the user
	lang: int
		The language code into which output must be generated

	Returns
	none
		Plays the final speech output to the user and waits for next instruction.

	"""

	# Languages codes fetched from the GUI (Tkinter)
	langs = {1 : "te", 2 : "ta", 3 : "kn", 4 : "gu", 5 : "hi"}
	# Corresponding voice processing files of flite library 
	voices = {1 : "cmu_indic_tel_ss.flitevox", 2 : "cmu_indic_tam_sdr.flitevox", 3 : "cmu_indic_kan_plv.flitevox", 4 : "cmu_indic_guj_ad.flitevox", 5 : "cmu_indic_hin_ab.flitevox"}
	# lan = str(sys.argv[1])
	# data = str(sys.argv[2])
	# Initiate Translate API
	translator = Translator()
	textt = translator.translate(text, src="en", dest=langs[lang]).text
	f = open("input.txt","w+")
	f.write(str(textt))
	print(textt)
	f.close()
	# Play the final Text to Speech Output to the user 
	os.system("./../flite/bin/flite -voice ../flite/voices/"+voices[lang]+" --setf duration_stretch=1.15 --setf int_f0_target_mean=145 -f input.txt ")

def begin(selected,txt):
	"""
	Initiates English Text processing by gathering inputs from GUI

	parameters
	------------------------------------------------
	selected: Tkinter object
		A Tkinter GUI object with the values for radio buttons
	txt: str
		The input phrase in English given by the user

	Returns
	none
		Retrieves input values from GUI and then passes them on to process function
		
	"""
	lang = selected.get()
	phrase = txt.get()
	process(phrase,lang)


def main():
	"""
	Main function for Ubiquitalk. Initializes GUI Tkinter, activates processing function.

	parameters
	------------------------------------------------
	None

	Returns
	none
		Runs on an infinite loop unless closed by the user. Handles GUI tasks.
		
	"""
	window = Tk()
	window.title("Ubiquitalk Translator")
	window.geometry('255x450')
	lbl = Label(window, text="Ubiquitalk Translator", bg="green", font=("Arial Bold", 15), padx=5, pady=5)
	lbl.grid(column=1, row=0)
	lbl = Label(window, text="", font=("Arial Bold", 20), padx=5, pady=5)
	lbl.grid(column=1, row=1)
	lbl = Label(window, text="Please enter an English phrase to process", bg="yellow", font=("Arial Bold", 8), padx=5, pady=5)
	lbl.grid(column=1, row=2)
	lbl = Label(window, text="", font=("Arial Bold", 20), padx=5, pady=5)
	lbl.grid(column=1, row=3)
	lbl = Label(window, text="Phrase: ")
	lbl.grid(column=1, row=4)
	txt = Entry(window, width=20)
	txt.grid(column=1, row=5)
	selected = IntVar()
	rad1 = Radiobutton(window,text='Telugu', value=1, variable=selected)
	rad2 = Radiobutton(window,text='Tamil', value=2, variable=selected)
	rad3 = Radiobutton(window,text='Kannada', value=3, variable=selected)
	rad4 = Radiobutton(window,text='Gujarati', value=4, variable=selected)
	rad5 = Radiobutton(window,text='Hindi', value=5, variable=selected)
	btn = Button(window, text="Translate!", command=partial(begin,selected,txt))
	rad1.grid(column=1, row=6)
	rad2.grid(column=1, row=7)
	rad3.grid(column=1, row=8)
	rad4.grid(column=1, row=9)
	rad5.grid(column=1, row=10)
	btn.grid(column=1, row=11)
	lbl = Label(window, text="Developed by", font=("Trebuchet Bold", 7), padx=5, pady=5)
	lbl.grid(column=1, row=13)
	lbl = Label(window, text="Chaitanya Krishna Kasaraneni", font=("Arial Bold", 7), padx=5, pady=5)
	lbl.grid(column=1, row=14)
	lbl = Label(window, text="Sarath Chandra Makkena", font=("Arial Bold", 7), padx=5, pady=5)
	lbl.grid(column=1, row=17)
	window.mainloop()



if __name__ == '__main__':
	main()
