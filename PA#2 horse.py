# Michael Carr
# Programing Assignment 2
# MIS 301
# 02/21/2024

from DrawingPanel import *
# finds DrawingPanel.py and its associated class

# This program draws a horse on a field
def main():
    # Creates the Panel & Sky
    panel = DrawingPanel(600,600,background="cyan")
    # Creates the Grass & Sun
    panel.fill_rect(0,300,600,390,"darkgreen")
    panel.fill_oval(500,100,100,100, "Yellow")
    # Creates the head of horse
    panel.fill_oval(130,130,125,50,"Brown")
    panel.fill_oval(210,150,50,125,"Brown")
    panel.fill_oval(200,145,10,10,"Black")
    panel.fill_oval(200,145,5,5,"White")
    # Creates the maine of horse
    panel.fill_oval(227,126,15,10,"Black")
    panel.fill_oval(240,132,15,10,"Black")
    panel.fill_oval(250,140,15,10,"Black")
    for i in range(0,6):
        panel.fill_oval(250+(2*i),150+(10*i),15,10,"Black")
    # Creates the body of horse
    panel.fill_oval(210,200,250,100,"Brown")
    # Creates the legs of horse
    panel.fill_rect(400,250,20,125,"Brown")
    panel.fill_rect(370,250,20,125,"Brown")
    panel.fill_rect(260,250,20,125,"Brown")
    panel.fill_rect(230,250,20,125,"Brown")
    # Creates the hooves of horse
    panel.fill_rect(400,370,20,10,"Black")
    panel.fill_rect(370,370,20,10,"Black")
    panel.fill_rect(260,370,20,10,"Black")
    panel.fill_rect(230,370,20,10,"Black")
    # Creates the tail of horse
    for i in range(0,7):
        panel.fill_oval(450+(3*i),240+(i*10),15,10,"Black")
# Starts the program
main()

