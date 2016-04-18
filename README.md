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
Copy the main.py and the VCS directory into the desired project directory.

We are assuming that create_repo has been called before check_in or check_out has been called. Also We are assuming that the user doesn't have additional folders in the desired project directory.

### Usage
In the desired project directory...

To create a repo for your project:
```
python main.py create_repo
```

To create check_in the repo:
```
python main.py check_in.py
```

To check_out a repo:
```
python main.py check_out.py
```

### Extra Features
None

### Bugs
We are still not sure if the script will run on Windows OS.

We are not sure if a if the software will work if a directory contains a directory of files. So I beleive this is another issue.