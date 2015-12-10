# AttrDict
A dict class that allows object-like values access syntax

# Dependencies

* python >= 2.6.x

# Basic example

``` python
from attrdict import AttrDict

my_dict = {'my_homepage': 'http://twitter.com/bbrodriges'}
my_attrdict = AttrDict(my_dict)
print(my_attrdict.my_homepage)
```
