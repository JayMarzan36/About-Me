from get_image_meta import get_all_image_metadata
import sys, os
from utils import bcolors



if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(bcolors.WARNING + "Please specify a directory" + bcolors.ENDC)
        sys.exit(1)

    inpt = sys.argv[1]
    
    if  os.path.isdir(inpt):
        get_all_image_metadata(inpt)
    elif "/" not in inpt:
        print(bcolors.WARNING + "Please replace '\\' with '/'" + bcolors.ENDC)
    else:
        print(bcolors.WARNING + "Not a directory" + bcolors.ENDC)