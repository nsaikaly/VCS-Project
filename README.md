### VCS-Project
* Author: Kumin In and Nick Saikaly
  * Github: @kuminin and @gamer1357
  * Team: NKX
  * Contact Info: kumin.in1@gmail.com
* CECS 343 - 07/08
* Project Part 1

### Introduction
This is the second part of our VCS (Version Control System) project. In this project part, we add the ability to check-in a project tree (mostly already done), and to check-out a project tree to a new location. The check-in ability lets the user checkpoint various intermediate states/versions of a project tree. The check-out ability lets the user, or another user, check-out a specific version of the project tree either to create a branch (e.g., so several users can work in parallel, or to specialize a project for the Android OS) or to rollback to a previous known good project state.


### External Requirements:
None

### Build, Installation, and Setup.
Copy the main.py and the VCS directory into the desired project location.

### Usage
```
python main.py create_repo

python main.py check_in.py

python main.py check_out.py
```

### Extra Features
None

### Bugs
We are still not sure if the script will run on Windows OS.

We are not sure if a if the software will work if a directory contains a directory of files. So I beleive this is another issue.