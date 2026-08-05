---
options:
  end_slide_shorthand: true
  h1_slide_titles: true
  incremental_lists: true
---
<!-- jump_to_middle -->
<!-- column_layout: [1, 1, 1] -->

<!-- column: 1 -->
# Saeyslab Conference 2026: Git and Github

---

# Git core concepts

- **Repository:** A folder where Git tracks your project and its history.
- **Commit:** A snapshot of your repository. Contains:
  - The **changes** with respect to the previous commit.
  - A **hash** that identifies it.
  - A reference to its **parent.**
- **Staging area:** a "waiting area" for your changes.
- **Branch:** A pointer to a specific commit.
- **HEAD:** A pointer to the current commit.
- **Working tree:** The state of the files that you see in your directory.
- Git tracks **changes,** not files.

## Demo
<!--
speaker_note: |
  Demo:
  - vim readme.md
  - git init
  - git status
  - git add readme.md
  - git status
  - git commit
  - git log
  - git log -p
  - vim readme.md: change a line, add a line
  - git status
  - git add readme.md
  - git commit -m "new commit"
  - git log -p
  - Create a few more commits
  - Checkout a previous commit
  - git log --oneline --graph --decorate --all
  - alias "git log --oneline --graph --decorate --all"
-->

---

# Basic Git commands
- `git init`: create a repository
- `git add [FILES]`: add files to the staging area
- `git commit [-m MESSAGE]`: create a commit
- `git checkout [HASH | BRANCH]`: move HEAD to a commit/branch or restore files
  - `git switch [HASH | BRANCH]`: move HEAD to a commit/branch
  - `git restore [FILE]`: restore file in the working tree (remove changes)

---

# Merging branches

- `git merge BRANCH`: merges BRANCH into the current branch.
  - It's best to do this when there are no uncommitted changes in the working tree.
  - This creates a *merge commit:* a commit with **2 parents.**
  - If the 2 parents have conflicting changes, these conflicts need to be resolved.
  - If there are no conflicts, the commit has no contents.

```txt +no_background
      A---B---C feature
     /
D---E---F---G main
               ^
              HEAD
```
<!-- pause -->
```bash +no_background
$ git merge feature
```
<!-- pause -->
```txt +no_background
      A---B---C feature
     /         \
D---E---F---G---H main
                  ^
                  HEAD
```
<!-- pause -->

## Demo

<!--
speaker_note: |
  Demo:
  - Normal branching/merging
    - git switch -c feat/test
    - glog
    - vim test.py
    - git commit
    - git switch main
    - vim readme.md
    - git commit
    - glog
    - git log -p: special merge commit
  - Merge conflicts
    - git switch -c feat/update_readme
    - vim readme.md
    - git commit
    - git switch main
    - vim readme.md
    - git commit
    - git merge feat/update_readme
    - glog
    - git status
    - vim readme.md
    - git commit
    - glog
    - git log -p -c: difference between 2 merge commits
-->

---

# GitHub and git remotes

- A **remote** is a copy of the repository on a server somewhere
- A repository can have multiple remotes
- `git remote add [NAME] [URL]`: adds URL as a remote (typically `origin`)
- `git push`: uploads commits
  - A branch gets assigned an **upstream branch** to track (synchronize)
- `git pull`: downloads commits
  - Will also perform `git merge` if necessary
- GitHub is **just one option** for storing your repositories
  - Alternatives include **GitLab, Bitbucket, Forgejo, Codeberg, ...**
- GitHub adds many bells and whistles to your git repo:
  - **Issues:** a kind of "support ticket" for your repo
  - **Pull requests:** should be called "merge requests"
    - A pull request is a *type* of issue
  - **GitHub Actions:** runs code on certain events
  - Wiki, discussions, releases, ...

## Demo
<!--
speaker_note: |
  Demo:
  - Make a repo on github
  - git remote add origin git@github.com:arnegevaert/git-intro.git
  - git push --set-upstream origin main
  - Show network graph
  - Create a merge conflict
  - Open pull request
  - Show command line instructions: slight difference
    - They tell you to merge in the reverse direction first
    - Then it can be merged back without conflicts
    - Alternatively: if you do it manually, the pull request will close automatically
  - Solve via github
-->


---

# Resources
- `https://learngitbranching.js.org/`
- `https://ohshitgit.com/`
