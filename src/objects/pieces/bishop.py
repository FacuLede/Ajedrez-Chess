from src.objects.piece import Piece 

class Bishop(Piece) :    

    def __init__(self, color, id) :
        Piece.__init__(self, color, id)
        self._image_file_name = self._images_pathfile + "alfil_" + color + ".png"
        self._piece_name = "A"

    def get_possible_movements(self) :
        movements = list()
        i = self._position + 7
        while i < 64 and i not in (-1 + 8 * x for x in range(0,9)) :
            movements.append(i)
            i += 7
        i = self._position + 9
        while i < 64 and i not in (8 * x for x in range(0,9)) :
            movements.append(i)
            i += 9
        i = self._position - 7
        while i >= 0 and i not in (8 * x for x in range(0,9)) :
            movements.append(i)
            i -= 7
        i = self._position - 9
        while i >= 0 and i not in (-1 + 8 * x for x in range(0,9)) :
            movements.append(i)
            i -= 9        
        return movements

    def _evaluate(self, squares, position) :
        r = True
        if squares[position].is_occupied() :
            r = not squares[position].get_piece().is_teammate(self)
        return r

    def get_legal_movements(self, squares) :
        movements = list()
        i = self._position + 7
        while i < 64 and i not in (-1 + 8 * x for x in range(0,9)) and self._evaluate(squares, i) :
            movements.append(i)
            if squares[i].is_occupied() and not squares[i].get_piece().is_teammate(self) :
                break
            i += 7
        i = self._position + 9
        while i < 64 and i not in (8 * x for x in range(0,9)) and self._evaluate(squares, i) :
            movements.append(i)
            if squares[i].is_occupied() and not squares[i].get_piece().is_teammate(self) :
                break
            i += 9
        i = self._position - 7
        while i >= 0 and i not in (8 * x for x in range(0,9)) and self._evaluate(squares, i) :
            movements.append(i)
            if squares[i].is_occupied() and not squares[i].get_piece().is_teammate(self) :
                break
            i -= 7
        i = self._position - 9
        while i >= 0 and i not in (-1 + 8 * x for x in range(0,9)) and self._evaluate(squares, i) :
            movements.append(i)
            if squares[i].is_occupied() and not squares[i].get_piece().is_teammate(self) :
                break
            i -= 9        
        return movements
    
    def get_controled_squares(self, squares) :
        movements = list()
        i = self._position + 7
        while i < 64 and i not in (-1 + 8 * x for x in range(0,9)) :
            movements.append(i)
            if not self._evaluate(squares, i) :
                break
            if squares[i].is_occupied() and not squares[i].get_piece().is_teammate(self) and not "king" in squares[i].get_piece().get_id() :
                break
            i += 7
        i = self._position + 9
        while i < 64 and i not in (8 * x for x in range(0,9)) :
            movements.append(i)
            if not self._evaluate(squares, i) :
                break
            if squares[i].is_occupied() and not squares[i].get_piece().is_teammate(self) and not "king" in squares[i].get_piece().get_id() :
                break
            i += 9
        i = self._position - 7
        while i >= 0 and i not in (8 * x for x in range(0,9)) :
            movements.append(i)
            if not self._evaluate(squares, i) :
                break
            if squares[i].is_occupied() and not squares[i].get_piece().is_teammate(self) and not "king" in squares[i].get_piece().get_id() :
                break
            i -= 7
        i = self._position - 9
        while i >= 0 and i not in (-1 + 8 * x for x in range(0,9)) :
            movements.append(i)
            if not self._evaluate(squares, i) :
                break
            if squares[i].is_occupied() and not squares[i].get_piece().is_teammate(self) and not "king" in squares[i].get_piece().get_id() :
                break
            i -= 9        
        return movements