# Saeyslab Conference 2026: Software Development

<!-- column_layout: [1, 1] -->
<!-- column: 0 -->
## Version control
- Introduction to git
- Github features
- Github action, CI/CD

## Dependency management
- Virtual environments
- Lockfiles

## Structuring projects
- In Python
- In R

## Automated testing
- Unit testing
- Property testing

<!-- column: 1 -->
## Containers

## Reproducible research

## Principles of software development

## Design patterns

<!-- end_slide -->

<!-- jump_to_middle -->

# Introduction to version control

<!-- end_slide -->

# Key Git concepts
<!-- incremental_lists: true -->
- **Repository:** A folder where Git tracks your project and its history.
- **Commit:** A snapshot of your repository.
  - A commit contains the **changes with respect to the previous commit.**
- **Staging area:** a "waiting area" for your changes.
- **Branch:** A pointer to a specific commit.
- **HEAD:** A pointer to the current commit.
- Git tracks **changes,** not files.

## Demo
<!--
speaker_note: |
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
-->

