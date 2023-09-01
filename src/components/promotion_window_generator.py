from src.windows import layout_promotion
import PySimpleGUI as sg
from src.objects.pieces import queen, rook, knight, bishop

def generate_promotion(a_piece) :
    color = a_piece.get_color()
    promotion_window = layout_promotion.build(color)
    while True :
        event, values = promotion_window.read()
        if event == sg.WIN_CLOSED :
            break
        elif event == "-QUEEN-" :
            piece = queen.Queen(color, color+"_"+"queen")
            break
        elif event == "-ROOK-" :
            piece = rook.Rook(color, color+"_"+"rook")
            break
        elif event == "-KNIGHT-" :
            piece = knight.Knight(color, color+"_"+"knight")
            break
        elif event == "-BISHOP-" :
            piece = bishop.Bishop(color, color+"_"+"bishop")   
            break
    promotion_window.close()
    return piece