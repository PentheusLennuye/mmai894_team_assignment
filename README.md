# mmai894_team_assignment
a.k.a. the Cake Detector

This is the repository for the Jupyter notebooks, models, scripts, spikes, and
deployments for the Team Watts application.

## Clone to a local repository
```
git clone git@github.com:PentheusLennuye/mmai894_team_assignment.git
cd mmai894_team_assignment.git
```

## Style

I recommend we keep lines to 80 characters. This will make cowriting and code
review easier. See Robert C. Martin. *Clean Code*, Pearson, 2008.

## Workflow

### 1. Create your local working branch

Create your local working branch from the "develop" branch. Do not create it
from the "main" branch.

```
git checkout develop
git pull
git checkout -b lastname/title  # example cummings/lstm_v2
git push -u origin lastname/title
```

### 2. Work on your local working branch

"Commit often and push once"

  - Have at it!
  - Remember to commit often so if you make a mistake, you can revert it
    ```
    git add .  # This basically adds everything into a change set
    git commit -m'This is a descriptive message.'
    ```
  - If you love your team, use a good commit message each commit! *A commit
    message shows whether a developer is a good collaborator* - Peter Hutterer.
  - If you messed up and need to go back to your last save point, revert with:
    ```
    git checkout -- <filename>
    ```

We will figure out a decent commit message as we go along, but for starters, here are some example:

  - "feature: Add new lstm model after first cnn"
  - "fix: Changed bidirectional lstm input params. Resolved training crash."
  - "docs: Inserted example commit messages to README"
  - "refactor: Moved hyperparameter exploration into a loop. Changed function names."
  - "style: Fixed lines 210 - 259 to stay within 80 characters."

See https://dev.to/wordssaysalot/art-of-writing-a-good-commit-message-56o7

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
