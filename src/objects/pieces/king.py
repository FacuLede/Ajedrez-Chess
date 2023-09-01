from src.objects.piece import Piece 

class King(Piece) :    

    def __init__(self, color, id) :
        Piece.__init__(self, color, id)
        self._image_file_name = self._images_pathfile + "rey_" + color + ".png"
        self._moved = False
        self._piece_name = "R"

    def _can_left_castles(self, squares) :
        r = True
        i = self._position
        squeares_attacked = self._squares_attacked(squares)
        if i in squeares_attacked :
            r = False
        elif (i - 2 in squeares_attacked) | (i - 1 in squeares_attacked) :
            r = False
        return r
    
    def _can_right_castles(self, squares) :
        r = True
        i = self._position
        squeares_attacked = self._squares_attacked(squares)
        if i in squeares_attacked :
            r = False
        elif (i + 2 in squeares_attacked) | (i + 1 in squeares_attacked) :
            r = False
        return r

    def comprobate_castles(self, squares, movements) :
        if not self._moved :
            if squares[self._position + 3 ].is_occupied() and "rook" in squares[self._position + 3 ].get_piece().get_id() and not squares[self._position + 3 ].get_piece().was_moved() and not squares[self._position + 2 ].is_occupied() and not squares[self._position + 1 ].is_occupied() and self._can_right_castles(squares):
                movements.append(self._position + 2)
            if squares[self._position - 4 ].is_occupied() and "rook" in squares[self._position - 4 ].get_piece().get_id() and not squares[self._position - 4 ].get_piece().was_moved() and not squares[self._position - 3 ].is_occupied() and not squares[self._position - 2 ].is_occupied() and not squares[self._position - 1 ].is_occupied() and self._can_left_castles(squares) :
                movements.append(self._position - 2)
    
    def get_possible_movements(self) :
        movements = list()
        i = self._position 
        if i + 7 < 64 and i + 7 not in (-1 + 8 * x for x in range(0,9)) :
            movements.append(i + 7) #abajo izuquierda
            movements.append(i-1) 
            movements.append(i+8) 
     
        if i + 9 < 64 and i + 9 not in (8 * x for x in range(0,9)) :
            movements.append(i + 9)   #abajo derecha
            movements.append(i+1) 
            movements.append(i+8)        
   
        if i - 7 >= 0 and i - 7 not in (8 * x for x in range(0,9)) :
            movements.append(i - 7)     #arriba derecha
            movements.append(i+1) 
            movements.append(i-8)  
  
        if i - 9 >= 0 and i - 9 not in (-1 + 8 * x for x in range(0,9)) :
            movements.append(i - 9)    #arriba izuqierda
            movements.append(i-1) 
            movements.append(i-8)         
        return list(set(movements))

    def get_legal_movements(self, squares) :
        movements = self.get_possible_movements()
        self.comprobate_castles(squares, movements)
        movements = self.discard_teammates(movements, squares, self)
        movements = self.discard_attacked_squares(movements, squares)
        return movements

    def moved(self):
        self._moved = True 

    def was_moved(self) :
        return self._moved
        
    def _squares_attacked(self, squares) :
        squares_attacked = list()
        for i in squares :
            if i.is_occupied() and not i.get_piece().is_teammate(self) :
                squares_attacked.extend(i.get_piece().get_controled_squares(squares))
        return list(set(squares_attacked))

    def discard_attacked_squares(self, movements, squares) :
        squares_attacked = self._squares_attacked(squares)
        filtered_movements = movements.copy()
        for i in movements :
            if i in squares_attacked :
                filtered_movements.remove(i)
        return filtered_movements

    def is_in_check(self, squares) :
        r = False
        if self._position in self._squares_attacked(squares) :
            r = True
        return r
            
