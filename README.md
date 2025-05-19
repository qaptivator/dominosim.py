# dominosim.py
Python level editing library for Kyowob's Domino Simulator  
**_made by qaptivator (captivator)_**

# installation
```bash
pip install git+https://github.com/qaptivator/dominosim.py.git#egg=dominosim
```
it will act as a regular PyPi package, but wont be actually hosted there (there are many issues regarding actually publishing a package there).

# usage
```py
from dominosim import Level
level = Level()
# or level = Level.parse('...')
level.add_object()
print(level.stringify())
```

# license
MIT license (`LICENSE.txt`)