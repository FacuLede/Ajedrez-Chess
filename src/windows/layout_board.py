import PySimpleGUI as sg
import os 

def build(squares) :
    layout = list()
    lane = list()
    j = 0
    for i in squares :
        if i.is_occupied() :
            lane.append(sg.Button(button_color=i.get_color(),image_subsample=2,size=(12,6),image_size=(102,102),image_filename=i.get_piece().get_image(),key=str(j)))
        else :
            lane.append(sg.Button(button_color=i.get_color(),size=(12,6),key=str(j)))
        j += 1
        
        if len(lane) == 8 :
            layout.append(lane.copy())
            lane.clear()        

    return sg.Window("Chess", layout, background_color="#AED6F1", icon=os.path.join(os.getcwd(),"src","files","icon.ico")).finalize()