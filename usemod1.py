import sys
# from pkg.pkg import module
from nnl.utils import johnlib
from nnl.physics.emma import emma_id

# johnlib.py
johnlib.spam()
johnlib.toast()

print(johnlib.COLORS)

# module search
#  sys.path

# made from:
# 1. current directory
# 2. directories in PYTHONPATH
# 3. builtin  directories under sys.prefix
for path in sys.path:
    print(path)
print()
print(sys.prefix)

emma_id()