# Python Fabric 2.4.0
Implementation of python fabric with SSH example(video). [_website_](https://dextoruz.wordpress.com/2018/10/10/python-fabric-2.4.0/) link.

### Before run any file:
You need some changes in ***send_email.py*** file.
  * Change _sender-email and sender-password_.
  * Change _receiver-email_
  * Before this, you need to sure about your Google account that whether __other device access__
  is _enable_ or not. 


### Note:
If your task has parameters, please set it with DEFAULT VALUES or you must pass arguments to this function. Otherwise, it will throw an error,

   __SyntaxError: non-default argument follows default argument__

 or, if it doesn't throw any error,then it has two scenarios:

   * You executed multiple tasks, and anyone of it had parameters( which were **NOT** set as **DEFAULT VALUES**), so then the coming task will become **STRING** and use as parameter of this task. The results you've seen are not that as you expected.
   * [Jeff Forcier](http://bitprophet.org/) has fixed this bug.
