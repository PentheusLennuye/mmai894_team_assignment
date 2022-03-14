# mmai894_team_assignment
a.k.a. the Cake Detector

This is the repository for the Jupyter notebooks, models, scripts, spikes, and
deployments for the Team Watts application.

## Clone to a local repository
```
git clone git@github.com:PentheusLennuye/mmai894_team_assignment.git
cd mmai894_team_assignment.git
```

## Workflow

### 1. Create your local working branch

Create your local working branch from the "develop" branch. Do not create it
from the "main" branch.

```
git checkout develop
git pull
git checkout -b lastname/title  # example cummings/lstm_v2
```

### 2. Work on your local working branch

"Commit often and push once"

Have at it! Remember to commit often so if you make a mistake, you can revert
your mistake with a `git checkout -- <filename>`

### 3. Save and push your local working branch to github

You will want to know more about git, but in a nutshell:

```
git fetch && git rebase origin/develop  # In case develop updated while you were working
git add .
git commit -m'This is a good description of what I just did'
git push
```

### 4. Pull Request into Develop

If your branch is the way you want it to be, and you are ready to push to develop:

  1. Go to github.com, PentheusLennuye/mmai894_team_assignment
  2. Ask for a pull request
  3. Once the pull request is approved AND MERGED into develop, purge your
     local branch.
  ```
  git checkout develop
  git branch -d lastname/title  # example cummings/lstm_v2
  ```

### 5. Rinse, and Repeat

Create another branch, and work on it as above.
