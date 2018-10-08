# Python Fabric 2.4.0
Implementation of python fabric with SSH example(video).
Brief introduction; [_website_](https://linxnerd.wordpress.com/2018/10/10/python-fabric-2.4.0/) link.

## Installation

_`   sudo apt install fabric`_

_`   sudo apt install update`_

or the best way;

_`   pip install fabric`_

_`   pip install -U fabric`_   /// for update


## Note:
If your task has __Parameters__, please set it by **DEFAULT VALUES**, Because when you'll execute
multiple tasks, and anyone of it has parameters( which is __NOT__ set as DEFAULT VALUES), then the
coming task will become __STRING__ and use as parameter of this task. The results will not show as you
expected.
