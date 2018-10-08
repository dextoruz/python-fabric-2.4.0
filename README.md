# Python Fabric 2.4.0
Implementation of python fabric with SSH example(video). [_website_](https://linxnerd.wordpress.com/2018/10/10/python-fabric-2.4.0/) link.

## Installation

_`   sudo apt install fabric`_

_`   sudo apt install update`_

or the best way;

_`   pip install fabric`_

_`   pip install -U fabric`_   /// for update


### Note:
If your task has parameters, please set it with DEFAULT VALUES or you must pass arguments to this function. Otherwise, it throws an error,

   __SyntaxError: non-default argument follows default argument__

 or, if it doesn't throw any error, it has two scenarios:

   * You executed multiple tasks, and anyone of it had parameters( which were NOT set as DEFAULT VALUES), so then the coming task will become STRING and use as parameter of this task. The results you've seen are not that as you expected.
   * [Jeff Forcier](http://bitprophet.org/) has fixed this bug. 
