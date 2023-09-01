from src.objects.piece import Piece 

class Pawn(Piece) :    

    def __init__(self, color, id) :
        Piece.__init__(self, color, id)
        self._image_file_name = self._images_pathfile + "peon_" + color + ".png"
        self._moved = False
        self._just_moved = False
        self._piece_name = "P"

    def get_possible_movements(self) :
        movements = list()
        if not self._moved :            
            if self._color == "negro" :
                movements = [self._position + 8, self._position + 16]                
            else :
                movements = [self._position - 8, self._position - 16]                
        else :
            if self._color == "negro" :
                if self._position + 8 < 64 :
                    movements = [self._position + 8]
            else :
                if self._position - 8 >= 0 :
                    movements = [self._position - 8]   
        if self._color == "negro" :   
            if self._position not in (8 * x for x in range(0,9)) and self._position + 7 < 64 :
                    movements.append(self._position + 7)
            if self._position not in (-1 + 8 * x for x in range(0,9)) and self._position + 9 < 64 :
                movements.append(self._position + 9)     
        else :
            if self._position not in (-1 + 8 * x for x in range(0,9)) and self._position - 7 >= 0 :                    
                    movements.append(self._position - 7)
            if self._position not in (8 * x for x in range(0,9)) and self._position - 9 >= 0 :
                movements.append(self._position - 9)  
        return movements
    
    def _calculate_attacks(self, squares, movements) :
        if self._color == "negro" :   
            if self._position not in (8 * x for x in range(0,9)) and self._position + 7 < 64 and squares[self._position + 7].is_occupied() and not squares[self._position + 7].get_piece().is_teammate(self) :
                movements.append(self._position + 7)
            if self._position not in (-1 + 8 * x for x in range(0,9)) and self._position + 9 < 64 and squares[self._position + 9].is_occupied() and not squares[self._position + 9].get_piece().is_teammate(self) :
                movements.append(self._position + 9)     
        else :
            if self._position not in (-1 + 8 * x for x in range(0,9)) and self._position - 7 >= 0 and squares[self._position - 7].is_occupied() and not squares[self._position - 7].get_piece().is_teammate(self) :                    
                movements.append(self._position - 7)
            if self._position not in (8 * x for x in range(0,9)) and self._position - 9 >= 0 and squares[self._position - 9].is_occupied() and not squares[self._position - 9].get_piece().is_teammate(self) :
                movements.append(self._position - 9)   

    def get_legal_movements(self, squares) :
        movements = list()
        if not self._moved :          
            if self._color == "negro" :   
                if not squares[self._position + 8].is_occupied() :  
                    movements.append(self._position + 8)            
                if not squares[self._position + 8].is_occupied() and not squares[self._position + 16].is_occupied() :  
                    movements.append(self._position + 16)  
            else :
                if not squares[self._position - 8].is_occupied() :  
                    movements.append(self._position - 8)            
                if not squares[self._position - 8].is_occupied() and not squares[self._position - 16].is_occupied() :  
                    movements.append(self._position - 16)  
        else :              
            if self._color == "negro" :
                if self._position + 8 < 64 and not squares[self._position + 8].is_occupied() :
                    movements = [self._position + 8]
            else :
                if self._position - 8 >= 0 and not squares[self._position - 8].is_occupied() :
                    movements = [self._position - 8]      
        self._calculate_attacks(squares, movements)
        self._en_passant_capture(squares, movements)
        return movements

    def _en_passant_capture(self, squares, movements) :
        left = self._position - 1   
        right = self._position + 1 
        if self._color == "blanco" :
            if left not in (-1 + 8 * x for x in range(0,9)) :  
                if squares[left].is_occupied() and not squares[left].get_piece().is_teammate(self) and "pawn" in squares[left].get_piece().get_id() : 
                    if squares[left].get_piece().just_moved() :
                        movements.append(self._position-9)
            if right not in (8 * x for x in range(0,9)) :
                if squares[right].is_occupied() and not squares[right].get_piece().is_teammate(self) and "pawn" in squares[right].get_piece().get_id() :
                    if squares[right].get_piece().just_moved() :
                        movements.append(self._position-7)
        else :
            if left not in (-1 + 8 * x for x in range(0,9)) :  
                if squares[left].is_occupied() and not squares[left].get_piece().is_teammate(self) and "pawn" in squares[left].get_piece().get_id() : 
                    if squares[left].get_piece().just_moved() :
                        movements.append(self._position+7)
            if right not in (8 * x for x in range(0,9)) :
                if squares[right].is_occupied() and not squares[right].get_piece().is_teammate(self) and "pawn" in squares[right].get_piece().get_id() :
                    if squares[right].get_piece().just_moved() :
                        movements.append(self._position+9)

    def moved(self) :
        self._moved = True

    def set_position(self, position) :
          
        if not self._moved and (position == self._position + 16) | (position == self._position - 16) :    
            self._just_moved = True
        self._position = position  

    def just_moved(self) :
        return self._just_moved 
    
    def update_pawn(self) :
        self._just_moved = False

    def get_controled_squares(self, squares):
        movements = list()
        if self._color == "negro" :   
            if self._position not in (8 * x for x in range(0,9)) and self._position + 7 < 64 :
                movements.append(self._position + 7)
            if self._position not in (-1 + 8 * x for x in range(0,9)) and self._position + 9 < 64 :
                movements.append(self._position + 9)     
        else :
            if self._position not in (-1 + 8 * x for x in range(0,9)) and self._position - 7 >= 0 :                    
                movements.append(self._position - 7)
            if self._position not in (8 * x for x in range(0,9)) and self._position - 9 >= 0 :
                movements.append(self._position - 9) 
        return movements