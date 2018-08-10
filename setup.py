#!/usr/bin/env python

import os

contents = """# December {}, 2018

\"\"\"

\"\"\"

def method():
    pass

if __name__ == '__main__':
    pass
"""

# this_file = os.path.basename(__file__)

# for filename in os.listdir(os.getcwd()):
#     if filename.startswith('.') or filename == this_file:
#         continue

#     name, _ = tuple(filename.split('.'))
#     if int(name) < 13:
#         continue

for name in range(188, 219):
    filename = str(name) + '.py'
    with open(filename, 'w') as f:
        date = name - 187
        f.write(contents.format(date))
