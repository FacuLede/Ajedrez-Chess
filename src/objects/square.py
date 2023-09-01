class Square() :
    
    def __init__(self,color,position) :
        self._is_occupied = False
        self._color = color
        self._position = position
        self._piece = None

    def get_color(self) :
        return self._color
        
    def set_color(self, color) :
        self._color = color 

    def get_position(self) :
        return self._position

    def is_occupied(self) :
        return self._is_occupied

    def dispose_piece(self) :
        self._piece = None
        self._is_occupied = False


    def set_piece(self, piece, position) :
        self._piece = piece
        self._is_occupied = True
        piece.set_position(position)

    def get_piece(self) :
        return self._piece