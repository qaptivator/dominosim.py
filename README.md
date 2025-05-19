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
from dominosim import Level, Object, OBJ_TYPE, OBJ_ROT
level = Level()
# or level = Level.parse('...')
level.add_object(Object(
    OBJ_TYPE.ORTHOGONAL_DOMINO,
    -2, 5,
    OBJ_ROT.RIGHT
))
print(level.stringify())
# or open('result.txt', 'w').write(level.stringify())
```

this library is so small that it doesnt even need any documentation. but we will go over the principles anyway.

so, this is a domino game, and _you_ want to edit its level through python. the format is really simple, just space separated object arguments, but you still need boilerplate to parse and unify it all. so here we go.

all objects have their type (eg orthogonal, fork and so on), xy integer grid positions, and their rotation (from 0 to 3). you add objects by using the `Object()` class, passing the arguments there, then passing it to `level.add_object()`. levels can be either made empty, or from parsing an already existing level.

_here is a list of useful code snippets when working with domino levels:_

- read level from file
    ```py
    level = Level.parse(open('input.txt', 'r').read())
    ```
- write level to file
    ```py
    open('result.txt', 'w').write(level.stringify())
    ```
- import with short name
    ```py
    import dominosim as d
    level = d.Level() # ...
    ```

# for contributors (future me)

when making a new version, dont forget to update `setup.py` and also `pyproject.toml` (updating the toml file is optional). then, make a new git tag with `git tag vX.Y.Z` and push it to main with `git push origin tag vX.Y.Z`.

# license
MIT license (`LICENSE.txt`)