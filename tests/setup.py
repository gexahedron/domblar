import os
import sys
from pathlib import Path

# add path to domblar development code
sys.path.insert(0, str(Path(os.getcwd()).parent))

from domblar.domblar import Domblar

D = Domblar
