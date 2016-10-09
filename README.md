# cTime
JavaScipt has console.time(). Why not implement similiar thing to Python?

## Usage
Place ``cTime.py`` and ``__init__.py`` into your project's folder.

For ex.:
```
myProject/
 __init__.py
 cTime.py
 mySuperScript.py
```

Inside your script (``mySuperScript.py``) you need to import cTime:
``` Python
import cTime
```

If you want to start a new timer:
``` Python
cTime.time(name, _round=2, _print=False)
```
Where:

* ``name`` - timer name, if there's already a timer with that name, ``CollisionError``
Exception will be throw (I have to rethink if I really need custom error)
* ``_round`` - round precision, must be integer, default ``2``
* ``_print`` - make it ``True`` if you want cTime to automatically print results.
If it's false, it will return a floating point number. Default ``False``

See ``example.py`` for, well, you've guessed it, an example ;P

**Note**
It's not delay-free implementation, you have to know that cTime adds a few ms to results.
