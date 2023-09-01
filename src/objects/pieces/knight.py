from src.objects.piece import Piece 

class Knight(Piece) :    

    def __init__(self, color, id) :
        Piece.__init__(self, color, id)
        self._image_file_name = self._images_pathfile + "caballo_" + color + ".png"
        self._piece_name = "C"

    def _calculate_row(self) :
        min = 99
        row = int()
        for i in (8 * x for x in range(1,9)) :
            if self._position - i < min and self._position >= i:
                min = self._position - i 
                row = i
        return row   

    def get_possible_movements(self) :
        
        movements = list()
        movements_aux = list()
        row = self._calculate_row()
        i = self._position
        if i - 10 >= row - 8 :
            movements_aux.append(i - 10)
        if i - 17 >= row - 16 :
            movements_aux.append(i - 17)        
        if i + 6 >= row + 8 :
            movements_aux.append(i + 6)
        if i + 15 >= row + 16 :
            movements_aux.append(i + 15)
        if i - 6 <= row - 1 :
            movements_aux.append(i - 6)    
        if i - 15 <= row - 9 :
            movements_aux.append(i - 15)   
        if i + 10 <= row + 15 : 
            movements_aux.append(i + 10)    
        if i + 17 <= row + 23 :       
            movements_aux.append(i + 17)
        for j in movements_aux :
            if j < 64 and j >= 0 :                
                movements.append(j)
        return movements

    def get_legal_movements(self, squares) :
        movements = self.get_possible_movements()
        movements = self.discard_teammates(movements, squares, self)
        return movements