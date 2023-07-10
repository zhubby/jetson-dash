# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from jtop import jtop



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with jtop() as jetson:
    # jetson.ok() will provide the proper update frequency
        while jetson.ok():
        # Read tegra stats
            print(jetson.cpu)
