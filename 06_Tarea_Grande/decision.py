class Manager:

    def __init__(self):
        self.current_decision = None
        self.commands = {'3': 'Mover robot derecha',
                         '4': 'Mover robot izquierda',
                         '5': 'Mover robot arriba',
                         '6': 'Mover robot abajo',}
    
    def decide_what_to_do(self, shape):
        shape = str(shape)
        if shape not in self.commands:
            return None, "no sé qué hacer :c"            
        
        return shape, self.commands[shape]
