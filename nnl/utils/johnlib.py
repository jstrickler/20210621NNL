"""
Demo module for NNL

Contains silly worthless functions and data.
"""
COLORS = ['red', 'blue', 'green']

def spam():
    """
    Spiced fatty pig meat.

    :return: None
    """
    print("Hello from spam()")

def _ham(): # "private"
    print("   and _ham()")

def toast():
    """
    Grilled slices of bread, just waiting for butter and jam.

    :return: None
    """
    print("Hello from toast()")
    _ham()

# use the following if you want to also run your module
# as a script. Otherwise it is not needed (but doesn't
# hurt anything).
if __name__ == "__main__":  # only execute if this file is
    # directly run with python, not imported
    print(f"Hello from the {__name__} module!")
    spam()
    toast()
