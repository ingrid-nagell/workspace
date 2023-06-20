from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))  
# the number of parents tells python how far upwards to navigate in order to look for 
# the path of the what_to_import file

from child_folder.child_child_folder import what_to_import

print(what_to_import)