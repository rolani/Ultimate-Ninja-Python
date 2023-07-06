message = """(1) Punch of Fury
(2) Kick of Punishment
(3) Sword of Justice
(4) Shuriken of Vengeance
(5) Nunchucks of Anger
(6) Knife of Freedom"""

instructions = """Welcome to Ultimate Ninja Battle Combat!!! 
You will be fighting against the computer, 
and the winner gets bragging rights. 
For each turn you will be asked to use one of the 6 attacks below:"""

newline = '\n'

def is_int(val) -> bool:

    """
    check if the value is an integer.
    """
    try:
        if type(val) == int:
            return True
        else:
            return False
    except ValueError:
        return False
