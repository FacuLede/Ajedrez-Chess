from src.functions import functions
from src.objects import square
from src.objects.pieces import pawn, rook, knight, queen, king, bishop 
from src.components import promotion_window_generator as pwg
import os
import csv

class Board() :
    _colors = ("white","#2874A6")
    _path_file = os.path.join(os.getcwd(),"src","files","pieces","")
    def __init__(self) :
        j = 0
        self._board = list()
        for i in range(64) :
            self._board.append(square.Square(self._colors[j], i))
            j = functions.change_values(j,i)
        self.set_pieces()
        self._turn = "blanco" 
        self._game_movements = list()
        self._alphanumeirc_movements = list()

    def is_occupied(self,position) :
        """Retorna True si la casilla correspondiente a 
        la posición recibida como parámetro está ocupada
        por una pieza, false en caso contrario.
        """
        return self._board[position].is_occupied()

    def _create_pieces(self, color, pieces) :
        pieces.append(rook.Rook(color,color+"_"+"left_rook"))  
        pieces.append(knight.Knight(color,color+"_"+"left_knight"))
        pieces.append(bishop.Bishop(color,color+"_"+"left_bishop"))        
        pieces.append(queen.Queen(color,color+"_"+"queen"))
        pieces.append(king.King(color,color+"_"+"king"))
        pieces.append(bishop.Bishop(color,color+"_"+"right_bishop"))        
        pieces.append(knight.Knight(color,color+"_"+"right_knight"))              
        pieces.append(rook.Rook(color,color+"_"+"right_rook"))     

    def _create_pawns(self, color, pieces) :
        for i in range(1,9) :            
            pieces.append(pawn.Pawn(color,color+"_"+"pawn"+str(i)))

    def _set_pieces(self, pieces, position) :
        j = position
        for i in pieces :
            self._board[j].set_piece(i,j)
            j +=  1

    def set_pieces(self) :
        black_pieces = list()
        self._create_pieces("negro", black_pieces)
        self._create_pawns("negro", black_pieces)
        white_pieces = list()
        self._create_pawns("blanco", white_pieces)
        self._create_pieces("blanco", white_pieces)        
        self._set_pieces(black_pieces,0)
        self._set_pieces(white_pieces,48)

    def get_squares(self) :
        return self._board

    def move_piece(self, position_1, position_2, board_window) :
        piece = self._board[position_1].get_piece()
        piece_2 = "None"
        if self._board[position_2].is_occupied() :
            piece_2 = self._board[position_2].get_piece()
        id = piece.get_id()
        movements = piece.get_legal_movements(self._board)         
        if position_2 in movements :                         
            self._update_pawns()  
            self._game_movements.extend([position_1,position_2])         
            if "king" in id and position_2 in (position_1+2, position_1-2):
                self.castles(piece, position_1, position_2, board_window) 
                self.change_turn()  
                self._game_movements.pop()
                self._game_movements.pop()
            if "pawn" in id :  
                self.en_passant_capture(piece, position_1, position_2, board_window)             
            self._board[position_2].set_piece(piece, position_2)  
            self._board[position_1].dispose_piece() 
            if self.check_for_check(piece) :
                self.undo_move([piece, piece_2], position_1, position_2)
            else :
                print(piece.get_piece_name(),self.get_alphanumeric_coords(int(position_1)),self.get_alphanumeric_coords(int(position_2)))
                self._alphanumeirc_movements.append(piece.get_piece_name()+"-"+self.get_alphanumeric_coords(int(position_1))+">"+self.get_alphanumeric_coords(int(position_2)))
                piece.moved()                   
                board_window[str(position_1)].update(image_filename=self._path_file+"no_pieza.png",image_subsample=2,image_size=(102,102))
                board_window[str(position_2)].update(image_filename=piece.get_image(),image_subsample=2,image_size=(102,102))
                        
                if "pawn" in id and self.promotionable(piece, position_2) :
                    self.promote_pawn(piece, position_2, board_window)
                self.change_turn()  

    def castles(self, piece, position, new_position, board_window) :
        castled = False
        if not piece.was_moved() :
            if new_position == position + 2 :
                self.move_piece(position + 3, position + 1, board_window)
                castled = True
            elif new_position == position - 2 :
                self.move_piece(position - 4, position - 1, board_window)
                castled = True
        return castled

    def en_passant_capture(self, piece, position_1, position_2, board_window) :
        if piece.get_color() == "negro" :
            if position_2 == position_1 + 7 and not self._board[position_2].is_occupied() : #abajo izquierda
                board_window[str(position_1 - 1)].update(image_filename=self._path_file+"no_pieza.png",image_subsample=2,image_size=(102,102))
                self._board[position_1 - 1].dispose_piece()
            elif position_2 == position_1 + 9 and not self._board[position_2].is_occupied() : #abajo derecha
                board_window[str(position_1 + 1)].update(image_filename=self._path_file+"no_pieza.png",image_subsample=2,image_size=(102,102))
                self._board[position_1 + 1].dispose_piece()
        else :
            if position_2 == position_1 - 9 and not self._board[position_2].is_occupied() : #arriba izquierda
                board_window[str(position_1 - 1)].update(image_filename=self._path_file+"no_pieza.png",image_subsample=2,image_size=(102,102))
                self._board[position_1 - 1].dispose_piece()
            elif position_2 == position_1 - 7 and not self._board[position_2].is_occupied() : #arriba derecha
                board_window[str(position_1 + 1)].update(image_filename=self._path_file+"no_pieza.png",image_subsample=2,image_size=(102,102))
                self._board[position_1 + 1].dispose_piece()
        

    def _update_pawns(self) :
        for i in self._board :
            if i.is_occupied() and "pawn" in i.get_piece().get_id() :
                i.get_piece().update_pawn()

    def promotionable(self, piece, position) :
        r = False
        if piece.get_color() == "blanco" and position in (x for x in range(0,8)):
            r = True
        elif piece.get_color() == "negro" and position in (x for x in range(56,64)):
            r = True
        return r

    def promote_pawn(self, piece, position, board_window) :
        new_piece = pwg.generate_promotion(piece)
        self._board[position].set_piece(new_piece, position)
        board_window[str(position)].update(image_filename=new_piece.get_image(),image_subsample=2,image_size=(102,102))

    def show_movements(self, movements, board_window) :
        for i in movements :
            board_window[str(i)].update(button_color="#58D68D")
    
    def hide_movements(self, board_window) :
        j = 0
        for i in self._board :
            board_window[str(j)].update(button_color=i.get_color())
            j += 1

    def change_turn(self) :
        if self._turn == "blanco" :
            self._turn = "negro"
        else :
            self._turn = "blanco" 
    
    def get_turn(self, piece) :
        return self._turn == piece.get_color()

    def check_for_check(self, piece) :
        king = None
        for i in self._board :
            if i.is_occupied() and i.get_piece().is_teammate(piece) and "king" in i.get_piece().get_id() :
                king = i.get_piece()
        return king.is_in_check(self._board)

    def undo_move(self, pieces, position_1, position_2) :
        if pieces[1] != "None" :
            self._board[position_1].set_piece(pieces[0],position_1)
            self._board[position_2].set_piece(pieces[1],position_2)
        else : 
            self._board[position_1].set_piece(pieces[0],position_1)
            self._board[position_2].dispose_piece()
        self._game_movements.pop()

    def get_alphanumeric_coords(self, an_int) :
        rows = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h"}
        row = ( an_int % 8 ) + 1
        column = ( 63 - an_int ) // 8 + 1
        return rows[row] + str(column)

    
    def get_game_id(self) :
        path_file = os.path.join(os.getcwd(),"src","files","")
        with open(path_file+"game_id.csv", "r", newline='', encoding="utf-8") as moves:            
            id = int(list(csv.reader(moves)).pop()[0]) 
        with open(path_file+"game_id.csv", "w", newline='', encoding="utf-8") as moves:
            writer = csv.writer(moves,delimiter=',')
            writer.writerow([id+1])
        return id

    def save_moves(self, movements, id) :
            path_file = os.path.join(os.getcwd(),"src","files","games","")

            if os.path.exists(path_file+"game_"+str(id)+".csv") :           
            
                with open(path_file+"game_"+str(id)+".csv", "a", newline='', encoding="utf-8") as moves:
                    writer = csv.writer(moves,delimiter=',')
                    writer.writerow(movements)
            else : 
                with open(path_file+"game_"+str(id)+".csv", "w", newline='', encoding="utf-8") as moves:
                    writer = csv.writer(moves,delimiter=',')
                    writer.writerow(movements)

    def get_game_movements(self) :
        return self._game_movements
    
    def get_alphanumeric_movements(self) :
        return self._alphanumeirc_movements