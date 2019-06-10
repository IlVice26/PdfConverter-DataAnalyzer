"""
    PdfConverter-DataAnalyzer by Vicentini Elia

    layout = [[sg.Text('All graphic widgets in one window!', size=(30, 1), font=("Helvetica", 25), text_color='blue')],      
    [sg.Text('Here is some text.... and a place to enter text')],      
    [sg.InputText()],      
    [sg.Checkbox('My first checkbox!'), sg.Checkbox('My second checkbox!', default=True)],      
    [sg.Radio('My first Radio!     ', "RADIO1", default=True), sg.Radio('My second Radio!', "RADIO1")],      
    [sg.Multiline(default_text='This is the default Text shoulsd you decide not to type anything',)],      
    [sg.InputCombo(['Combobox 1', 'Combobox 2'], size=(20, 3)),      
    sg.Slider(range=(1, 100), orientation='h', size=(35, 20), default_value=85)],      
    [sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'], size=(30, 6)),      
    sg.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=25),      
    sg.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=75),      
    sg.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=10)],      
    [sg.Text('_'  * 100, size=(70, 1))],      
    [sg.Text('Choose Source and Destination Folders', size=(35, 1))],      
    [sg.Text('Source Folder', size=(15, 1), auto_size_text=False, justification='right'), sg.InputText('Source'),      
    sg.FolderBrowse()],      
    [sg.Text('Destination Folder', size=(15, 1), auto_size_text=False, justification='right'), sg.InputText('Dest'),      
    sg.FolderBrowse()],      
    [sg.Submit(), sg.Cancel(), sg.Button('Customized', button_color=('white', 'green'))]]      


"""

__author__ = 'Vicentini Elia'
__version__ = '0.0.1'


import PySimpleGUI as sg
import exportData
import dataCollect
import pdfConverter
import os


def setupapp():
    
    layout = [
        [sg.Output((80, 20), key = 'out')],
        [sg.ProgressBar(1000, 'h', (20, 20), key='progbar'), sg.Cancel()]
    ]

    window = sg.Window('PdfConverter-DataAnalyzer - build 0.0.1', layout)

    # Event Loop
    for i in range(1000):
        event, values = window.Read(timeout=10)
        if event is None or event is 'Cancel':
            break
        sg.Element('out')
            


if __name__ == "__main__":
    setupapp()
