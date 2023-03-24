# try-prefect

try prefect  
use pipenv  
```
$ brew install pipenv
$ mkdir workflow
$ cd workflow
$ pipenv --python 3
Creating a virtualenv for this project...
Pipfile: /Users/user/IdeaProjects/try-prefect/workflow/Pipfile
Using /opt/homebrew/bin/python3 (3.11.2) to create virtualenv...
...
✔ Successfully created virtual environment!
```

install library
```
$ pipenv install prefect
Installing prefect...
Resolving prefect...
Installing...
Adding prefect to Pipfile's [packages] ...
...
Installing dependencies from Pipfile.lock (5f83a7)...
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```

enter venv
```
$ pipenv shell
Launching subshell in virtual environment...
...
(workflow) $ exit
Saving session...
...copying shared history...
...saving history...truncating history files...
...completed.
Deleting expired sessions...       4 completed.
```

start venv script
```
$ pipenv run start 
Pipfile start command
-----------------------------------
Pipfile

[scripts]
start = "python main.py hello"
-----------------------------------
```

start python file
```
$ pipenv run python main.py
```

run prefect script
```
(workflow) $ python3 basic_flow.py 
14:03:39.839 | INFO    | prefect.engine - Created flow run 'organic-bulldog' for flow 'my-favorite-function'
What is your favorite number?
14:03:39.904 | INFO    | Flow run 'organic-bulldog' - Finished in state Completed()
42

```
