# Software development topics

## Technical concepts
- Version control
  - https://www.w3schools.com/git/git_staging_environment.asp?remote=github
  - Git: commit, branch, merge
  - Github: push, pull, issue, pull request
  - CI/CD: github actions introduction
- Dependency management
  - Pin versions of dependencies
  - The point of lockfiles
    - Why you shouldn't use conda/mamba
  - Minimize the number of dependencies
    - More dependencies => more maintenance
    - Supply chain attacks
- Automated testing
  - Unit testing
  - Property testing
- Containers: basics


## Software development principles
- Core principles
  - ETC: Easier to Change
  - DRY: Don't Repeat Yourself
  - Orthogonality
  - Reversibility
  - Design by contract
  - Assertive programming
  - Decoupling
  - Don't outrun your headlights
  - Technical debt
- Programming by coincidence vs deliberate programming
- Refactoring
- Tools
  - Tracer bullets
  - Prototypes
  - Plain text
  - External configuration
- Debugging
- Testing
  - Design for testability
  - Test to help you think
- Commenting: documentation vs code comments
  - You shouldn't need many code comments, write readable code!

## Design patterns
...

## Reproducibility
- Full automation: have a single command to produce figures/results/papers
- Notebooks are for drafting/experimenting
  - Nonlinear execution
  - Encourages code duplication
  - Not ideal for version control
  - An exception: tutorials (but then you're basically just using notebooks as a website building tool)
- Containers: not as reproducible as you might think
- Don't hardcode things (especially not paths!)
  - Use a .env file for environment variables if you really need some global path
- Externalize your configs

## Useful skills
- Power editing
- Mastering the shell, piping
- Big O notation

## Project structuring
- Python: `uv`, `pixi`, `src/` etc
- R: `renv`, `Rproj`, avoid `setwd`, `here` etc
  - https://www.r-bloggers.com/2018/08/structuring-r-projects/
  - https://intro2r.com/dir_struct.html
  - https://tmieno2.github.io/WritingJournalArticleRmarkdown/C1_1_ProjectOrganization.html
  - https://r-statistics.co/R-Project-Structure.html

