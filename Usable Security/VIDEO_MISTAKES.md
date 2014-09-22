# Week 1
## Tasks 3
Comparing tasks between systems:

  * In the video, the lecturer describe the task as testing the usability of giving write permission to everybody. However, when visually presenting the ways of accomplishing the tasks on the two different tested systems (as well as later, when the lecturer describes the slightly modified task of giving everybody execute permission), it becomes obvious that the task was actually giving *read* permission to everybody.

  * Command line usually has many ways of accomplishing a task, e.g. granting write permission to everybody on a file can be accomplished either by issuing the command

  ```
  #chmod 722 FILE
  ```

  as well as by issuing the following (more user-friendly) command

  ```
  #chmod a+w FILE
  ```

  * Later, when trying to portray the fact that the GUI doesn't allow you give execute permission to everyone, the lecturer states that the command line doesn't have an option to add execute permission.
