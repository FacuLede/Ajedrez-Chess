import os

class Piece() :

    _images_pathfile = os.path.join(os.getcwd(),"src","files","pieces","")

    def __init__(self, color, id) :
        self._position = -1
        self._id = id
        self._color = color
        self._image_file_name = str()
        self._piece_name = str()

    def set_position(self, position) :
        """La idea es que al setear una pieza en una 
        casilla, la casilla le setee la posición a la 
        pieza
        """
        self._position = position
    
    def get_position(self) :
        return self._position

    def get_image(self) :
        return self._image_file_name

    def get_color(self) :
        return self._color

    def get_id(self) :
        return self._id

    def moved(self) :
        pass

    def is_teammate(self, a_piece) :
        is_teammate = False
        if self._color == a_piece.get_color() :
            is_teammate = True
        return is_teammate

    def discard_teammates(self, movements, squares, piece) : #a piece se le envía self
        filtered_movements = movements.copy()
        for i in movements :
            if squares[i].is_occupied() and squares[i].get_piece().is_teammate(piece) :
                filtered_movements.remove(i)     
        return filtered_movements       

    def get_legal_movements(self) :
        pass

    def get_controled_squares(self, squares) :
        return self.get_possible_movements()
    
    def get_piece_name(self) :
        return self._piece_name