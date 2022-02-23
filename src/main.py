# This file integrates the other modules and runs the program.
from src import alphacopy
from src import Stacked_AlphaCopy_app

def integration():
    pass
    """
    This function integrates the other modules and runs the program.
    """
    alphacopy.alpha_copy()
    Stacked_AlphaCopy_app.stacked_alphacopy_app()

if __name__ == "__main__":
    integration()
