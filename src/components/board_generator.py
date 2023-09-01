from src.objects import board
from src.windows import layout_board
import PySimpleGUI as sg

def generate_board() :

    chess_board = board.Board()
    squares = chess_board.get_squares()
    board_window = layout_board.build(squares)
    selected_piece = False
    while True :
        event, values = board_window.read()        
        if event in ("-EXIT-", sg.WIN_CLOSED) :
            break
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
    id = chess_board.get_game_id()  
    chess_board.save_moves(chess_board.get_game_movements(), id)
    chess_board.save_moves(chess_board.get_alphanumeric_movements(), str(id)+"alphanumeric")
    board_window.close()
