# This is to test coda environment

import torch
import pandas as pd
import numpy
import tqdm


print("Torch version:", torch.__version__)

print("Is CUDA enabled?", torch.cuda.is_available())


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
