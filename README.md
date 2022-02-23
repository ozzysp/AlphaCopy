# AlphaCopy
 
### A Python/GUI Open Source application with free participation to turn a Raspberry Pi on to a Backup Machine from SD Cards to external HDD's from USB ports. The idea is to create this application to run with Debian/Linux OS - Raspberry Pi OS and be assembled on a Raspberry Pi with 3,5" LCD display with touchscreen.  


# Contributing
Bellow information is intended for the development of the package


## Telegram group
Join our [Telegram group](https://t.me/joinchat/K-lrk09EB8N37ygHCxT_Vg)


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
### Linux/Mac
```
$ python3 -m venv .venv
$ source .venv/bin/activate
```
### Windows
```
$ pip3 install virtualenv
$ virtualenv {virtualenv-name}
$ {virtualenv-name}\Scripts\activate
```

- Install in editable mode with development dependencies.
```
$ pip install -r requirements.txt
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

# Thank you for your contribution!
