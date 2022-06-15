#!/usr/bin/env python3
import os
import sys
from datetime import date

parent_path = 'src/'
file_template = """#!/usr/bin/env python3
\"\"\"
CREATED AT: {DATE}

URL:

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: {NAME}

Difficulty: 

Desc: 

Tag: 

See: 

\"\"\"


def test():
    pass


if __name__ == '__main__':
    test()

"""
if __name__ == '__main__':
    name = ' '.join(sys.argv[1:])
    # name = "84. Largest Rectangle in Histogram"
    print(name)
    fn = ''.join(x.capitalize() if x.islower() else x for x in name.split()).replace('.', '-')
    path = os.path.join(parent_path, fn + '.py')
    if not os.path.exists(path):
        with open(path, 'w') as f:
            f.write(file_template.format(DATE=date.today(), NAME=fn))
        print(f'generated file at {path}')
    else:
        print('file already exists', path)
