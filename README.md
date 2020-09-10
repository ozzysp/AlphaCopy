# AlphaCopy
A Raspberry Pi BackUp application in Python GUI Open Source  
A Python/GUI Open Source aplication with free participation to turn a Rasperry Pi on to a Backup Machine from SD Cards to external HD's from USB ports. The idea is to create this application to run with Debian/Linux OS - Raspberry Pi OS and be assembly on a Raspeberry Pi with 3,5" LCD sreen with touchscreen.  


Uma aplicação Python/GUI Open Source com participação aberta para tornar um Raspberry Pi em uma máquina de BackUp de cartões SD para HD's externos. A ideia é criar esse aplicativo que funcione com o sistema Debian/Linux - Raspberry Pi OS e seja montado em um Raspberry Pi com tela de LCD de no mínimo 3,5" com touchscreen.  


# Contributing
Bellow information is intented for developing of the package


## Telegram group
Join our [telegram group](https://t.me/joinchat/K-lrk09EB8N37ygHCxT_Vg)


## First time setup
- Fork AlphaCopy to your GitHub account by clicking the `Fork` button.

- Clone the main repository locally.
```
$ git clone https://github.com/ozzysp/AlphaCopy
$ cd AlphaCopy
```

- Add your fork as a remote to push your work to. Replace {username} with your username. This names the remote "fork", the default AlphaCopy remote is "origin".
```
$ git remote add fork https://github.com/{username}/AlphaCopy
```

- Create and activate a virtualenv.
```
$ python3 -m venv .venv
$ source .venv/bin/activate
```

- Install in editable mode with development dependencies.
```
$ pip install -e . -r requirements-dev.txt
$ pip install PyQt5
$ pip install PySide2
```


## Start coding
- Create a branch to identify the issue you would like to work on. If you're submitting a bug or documentation fix, branch off of the latest ".x" branch.

```
$ git fetch origin
$ git checkout -b your-branch-name origin/1.1.x
```

If you're submitting a feature addition or change, branch off of the "master" branch.
```
$ git fetch origin
$ git checkout -b your-branch-name origin/master
```

- Using your favorite editor, make your changes, committing as you go.

- Include tests that cover any code changes you make. Make sure the test fails without your patch. Run the tests as described below.

- Push your commits to your fork on GitHub and create a pull request. Link to the issue being addressed with fixes #123 in the pull request.
```
$ git push --set-upstream fork your-branch-name
```


## Running the tests
Run the basic test suite with pytest.
```
$ pytest
```
