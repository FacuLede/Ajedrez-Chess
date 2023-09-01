import PySimpleGUI as sg
import os 

def build(color) :
    path_file = os.path.join(os.getcwd(),"src","files","pieces","") 
    layout =[
        [sg.Button(button_color="white",image_subsample=2,size=(12,6),image_size=(102,102),image_filename=path_file + "reina_" + color + ".png",key="-QUEEN-"),
        sg.Button(button_color="#2874A6",image_subsample=2,size=(12,6),image_size=(102,102),image_filename=path_file + "torre_" + color + ".png",key="-ROOK-"),
        sg.Button(button_color="white",image_subsample=2,size=(12,6),image_size=(102,102),image_filename=path_file + "caballo_" + color + ".png",key="-KNIGHT-"),
        sg.Button(button_color="#2874A6",image_subsample=2,size=(12,6),image_size=(102,102),image_filename=path_file + "alfil_" + color + ".png",key="-BISHOP-")
        ]
    ]
    return sg.Window("Promotion", layout, background_color="#AED6F1", keep_on_top=True).finalize()