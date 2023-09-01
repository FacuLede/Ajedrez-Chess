from src.objects.piece import Piece 

class Rook(Piece) :    

    def __init__(self, color, id) :
        Piece.__init__(self, color, id)
        self._image_file_name = self._images_pathfile + "torre_" + color + ".png"
        self._moved = False 
        self._piece_name = "T"

    def get_possible_movements(self) :
        movements = list()
        i = self._position + 8
        while i < 64 :
            movements.append(i)
            i += 8
        i = self._position - 8
        while i >= 0 :
            movements.append(i)
            i -= 8
        i = self._position + 1
        while i < 64 and i not in (8 * x for x in range(0,9)) : 
            movements.append(i)
            i += 1
        i = self._position - 1
        while i >= 0 and i not in (-1 + 8 * x for x in range(0,9)) : 
            movements.append(i)
            i -= 1
        return movements

    def _evaluate(self, squares, position) :
        r = True
        if squares[position].is_occupied() :
            r = not squares[position].get_piece().is_teammate(self)
        return r

    def get_legal_movements(self, squares) :
        movements = list()
        i = self._position + 8
        while i < 64 and self._evaluate(squares, i) :
            movements.append(i)
            if squares[i].is_occupied() and not squares[i].get_piece().is_teammate(self) :
                break
            i += 8
        i = self._position - 8
        while i >= 0 and self._evaluate(squares, i) :
            movements.append(i)
            if squares[i].is_occupied() and not squares[i].get_piece().is_teammate(self) :
                break
            i -= 8
        i = self._position + 1
        while i < 64 and i not in (8 * x for x in range(0,9)) and self._evaluate(squares, i) : 
            movements.append(i)
            if squares[i].is_occupied() and not squares[i].get_piece().is_teammate(self) :
                break
            i += 1
        i = self._position - 1
        while i >= 0 and i not in (-1 + 8 * x for x in range(0,9)) and self._evaluate(squares, i) : 
            movements.append(i)
            if squares[i].is_occupied() and not squares[i].get_piece().is_teammate(self) :
                break
            i -= 1
        return movements        

    def get_controled_squares(self, squares) :
        movements = list()
        i = self._position + 8
        while i < 64 :
            movements.append(i)
            if not self._evaluate(squares, i) :
                break
            if squares[i].is_occupied() and not squares[i].get_piece().is_teammate(self) and not "king" in squares[i].get_piece().get_id() :
                break
            i += 8
        i = self._position - 8
        while i >= 0 :            
            movements.append(i)
            if not self._evaluate(squares, i) :
                break
            if squares[i].is_occupied() and not squares[i].get_piece().is_teammate(self) and not "king" in squares[i].get_piece().get_id() :
                break
            i -= 8
        i = self._position + 1
        while i < 64 and i not in (8 * x for x in range(0,9)) : 
            movements.append(i)
            if not self._evaluate(squares, i) :
                break
            if squares[i].is_occupied() and not squares[i].get_piece().is_teammate(self) and not "king" in squares[i].get_piece().get_id() :
                break
            i += 1
        i = self._position - 1
        while i >= 0 and i not in (-1 + 8 * x for x in range(0,9)) : 
            movements.append(i)
            if not self._evaluate(squares, i) :
                break
            if squares[i].is_occupied() and not squares[i].get_piece().is_teammate(self) and not "king" in squares[i].get_piece().get_id() :
                break
            i -= 1
        return movements    

    def moved(self):
        self._moved = True 

    def was_moved(self) :
        return self._moved
    