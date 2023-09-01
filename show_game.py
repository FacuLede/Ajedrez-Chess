from src.objects import board
from src.windows import layout_board
import PySimpleGUI as sg
import os 
import csv

def show_game() :

    chess_board = board.Board()
    squares = chess_board.get_squares()
    board_window = layout_board.build(squares)
    selected_piece = False
    path_file = os.path.join(os.getcwd(),"src","files","games","")
    with open(path_file+"game_26.csv", "r", newline='', encoding="utf-8") as moves:            
        game_movements = list(csv.reader(moves))[0]
    while True :
        event, values = board_window.read(timeout=500)        
        if event in ("-EXIT-", sg.WIN_CLOSED) :
            break
        if len(game_movements) != 0 :
            event = game_movements.pop(0)
        if event.isnumeric() :
            if not selected_piece and squares[int(event)].is_occupied() and chess_board.get_turn(squares[int(event)].get_piece()) :
                board_window[str(event)].update(button_color="#E74C3C")
                last_event = event 
                selected_piece = True
                if squares[int(event)].is_occupied() :
                    movements = squares[int(event)].get_piece().get_legal_movements(squares)
                    chess_board.show_movements(movements, board_window)
            elif selected_piece :                
                chess_board.hide_movements(board_window)
                chess_board.move_piece(int(last_event), int(event), board_window)                
                selected_piece = False  
    board_window.close()

show_game()
