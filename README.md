# Python Fabric 2.4.0
Implementation of python fabric with SSH example.
Brief introduction [__here__](https://linxnerd.wordpress.com/2018/10/10/python-fabric-2.4.0/)

# Installation

    __sudo apt install fabric__

    __sudo apt install update__

or the best way;

    __pip install fabric__

    __pip install -U fabric__    /// for update

For checking the version and on-line reference manual;

    __fab --version__

    __man fab__

After installation, create __*fabfile.py__* in your current directory and write your jobs/tasks there, and for execution:

    fab -l                           *///shows list of available tasks*

    __fab task1__                  *///task1 = name of your task*

    __fab task1 admin__      */// admin = parameter of task1*

    __fab task1 task2 ...__    */// multiple tasks execution*


##    Note:
*       If your task has parameters, please set it by __DEFAULT VALUES__, Because when you'll execute multiple   tasks, and anyone of it has parameters( which is *__NOT__* set as DEFAULT VALUES), then the coming task will become __STRING__ and use as parameter of this task. The results will not show as you expected.*
