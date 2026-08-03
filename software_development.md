# Software development topics

## Technical concepts
- Version control
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

## Useful skills
- Power editing
- Mastering the shell, piping
- Big O notation
