from src.objects.piece import Piece 
from src.objects.pieces import rook, bishop

# mi idea inicial era que la reina heredase de torre y alfil ya que su comportamiento
# es justamente la suma de estos dos, pero no puede porque ya hereda de piece, clase de 
# la cual, también heredan las dos clases previamente mencionadas 
class Queen(Piece) :    

    def __init__(self, color, id) :
        Piece.__init__(self, color, id)
        self._image_file_name = self._images_pathfile + "reina_" + color + ".png"
        self._piece_name = "D"

    def get_possible_movements(self) :
        movements = list()
        self._get_possible_lineal_movements(movements)
        self._get_possible_diagonal_movements(movements)
        return movements

    def _get_possible_lineal_movements(self, movements) :
        i = self._position + 8
        while i < 64 :
            movements.append(i)
            i += 8
        i = self._position - 8
        while i >= 0 :
            movements.append(i)
            i -= 8
        i = self._position + 1
        while i < 64 and i not in (8 * x for x in range(1,9)) : 
            movements.append(i)
            i += 1
        i = self._position - 1
        while i >= 0 and i not in (-1 + 8 * x for x in range(1,9)) : 
            movements.append(i)
            i -= 1
    
    def _get_possible_diagonal_movements(self, movements) :
        i = self._position + 7
        while i < 64 and i not in (-1 + 8 * x for x in range(1,9)) :
            movements.append(i)
            i += 7
        i = self._position + 9
        while i < 64 and i not in (8 * x for x in range(1,9)) :
            movements.append(i)
            i += 9
        i = self._position - 7
        while i >= 0 and i not in (8 * x for x in range(1,9)) :
            movements.append(i)
            i -= 7
        i = self._position - 9
        while i >= 0 and i not in (-1 + 8 * x for x in range(1,9)) :
            movements.append(i)
            i -= 9        

    def get_legal_movements(self, squares) :
        movements = list()
        self._get_lineal_legal_movements(squares, movements)
        self._get_diagonal_legal_movements(squares, movements)
        return movements 

    def _evaluate(self, squares, position) :
        r = True
        if squares[position].is_occupied() :
            r = not squares[position].get_piece().is_teammate(self)
        return r

    def _get_diagonal_legal_movements(self, squares, movements) :
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
    
    def _get_lineal_legal_movements(self, squares, movements) :
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

    def get_controled_squares(self, squares) :
        controled_squares = self._get_controled_squares_diagonal(squares)
        controled_squares.extend(self._get_controled_squares_lineal(squares))
        return controled_squares

    def _get_controled_squares_diagonal(self, squares) :
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
    
    def _get_controled_squares_lineal(self, squares) :
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