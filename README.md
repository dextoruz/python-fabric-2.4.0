# Python Fabric 2.4.0
Implementation of python fabric with SSH example.
Brief introduction [**here**](https://linxnerd.wordpress.com/2018/10/10/python-fabric-2.4.0/)

# Installation

    **sudo** apt install fabric

    **sudo apt install update**

or the best way;

    **pip install fabric**

    **pip install -U fabric**    /// for update

For checking the version and on-line reference manual;

    **fab --version**

    **man fab**

After installation, create ***fabfile.py*** in your current directory and write your jobs/tasks there, and for execution:

    fab -l                           *///shows list of available tasks*

    **fab task1**                  *///task1 = name of your task*

    **fab task1 admin**      */// admin = parameter of task1*

    **fab task1 task2 ...**    */// multiple tasks execution*


##    Note:
*####        If your task has parameters, please set it by DEFAULT VALUES, Because when you'll execute multiple   tasks, and anyone of it has parameters( which is NOT set as DEFAULT VALUES), then the coming task will become STRING and use as parameter of this task. The results will not show as you expected.*
