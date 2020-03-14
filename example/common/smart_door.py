
class SmartDoor:
    """Classe simple pour représenter une porte"""

    closing_message = ' se ferme.'  # Attribut de ma classe
    opening_message = " s'ouvre."  # Attribut de ma classe

    def __init__(self, name):
        """
        Constructeur de ma classe
        :param name: Nom de la porte
        """
        self.name = name.capitalize()

    def close(self):
        msg = self.name + self.closing_message
        print(msg)
        return msg

    def open(self):
        msg = self.name + self.opening_message
        print(msg)
        return msg
