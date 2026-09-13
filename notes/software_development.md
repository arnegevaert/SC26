# Software development topics

## DevOps & Reproducibility
- Version control
  - https://www.w3schools.com/git/git_staging_environment.asp?remote=github
  - Git: commit, branch, merge
  - Github: push, pull, issue, pull request
  - CI/CD: github actions introduction (continuous integration/delivery)

- Dependency management
  - Paths in linux, Python and R
  - Pin versions of dependencies
  - The point of lockfiles
    - Why you shouldn't use conda/mamba
  - Minimize the number of dependencies
    - More dependencies => more maintenance
    - Supply chain attacks

- Project structuring
  - Python: `uv`, `pixi`, `src/` etc
  - R: `renv`, `Rproj`, avoid `setwd`, `here` etc
    - https://www.r-bloggers.com/2018/08/structuring-r-projects/
    - https://intro2r.com/dir_struct.html
    - https://tmieno2.github.io/WritingJournalArticleRmarkdown/C1_1_ProjectOrganization.html
    - https://r-statistics.co/R-Project-Structure.html

- Containers
  - Virtualization: VM vs Container
    - Intro to VMs
    - Hypervisors (e.g. VMWare, Virtualbox)
    - Difference to container
  - Demo 1: hello world
  - Basic dockerfile example
  - Docker build => creates an *image*
  - Docker run => *runs* that image, which results in a *container*
  - An image is like a class, a container is like an object
  - Demo 2: simple python script
  - Demo 3: simple bash script with dependency
  - Advanced concepts
    - Persistent storage: Volumes
    - Using docker for development: Development containers, bind mounts
    - Orchestrating multiple containers: Docker compose
  - Challenges
    - Go through diamol or [docker workshop](https://docs.docker.com/get-started/workshop/)
    - Wrap your current project in a docker image
    - Use a development container to develop your current or next project
    - Learn about Github Actions and set up automated tests on Github

- Reproducibility
  - Full automation: have a single command to produce figures/results/papers
  - Notebooks are for drafting/experimenting
    - Nonlinear execution
    - Encourages code duplication
    - Not ideal for version control
    - An exception: tutorials (but then you're basically just using notebooks as a website building tool)
  - Containers: not as reproducible as you might think
    - Show this with a demo?
  - Don't hardcode things (especially not paths!)
    - Use a .env file for environment variables if you really need some global path
  - Externalize your configs

## Software Development & Design Patterns
- Introduction
  - Sources: pragmatic programmer, a philosophy of software design
    - Challenge: read these books and implement their principles in your daily programming work
  - Why do we need "good code"?
    - Improves collaboration: with others, with your future self, with agents
      - What's confusing to people is generally also confusing to agents
    - Improves reproducibility
    - Makes it easier to discover and fix bugs
    - Makes it easier to make changes (which you will have to do at revision time)
  - What is "good code"?
    - Bad code: complexity
      - Complexity is anything related to the structure of a software system that makes it hard to understand and modify the system
      - "complex" does not mean lots of features
      - Symptoms of complexity
        - Change amplification: a seemingly simple change requires modifications in many places
        - Cognitive load: a developer needs to know a lot in order to complete a task
          - Use web page example Figure 2.1 p18
        - Unknown unknowns: it is not obvious which pieces of code must be modified to complete a task
      - Causes of complexity
        - Dependencies: web site example
        - Obscurity: bad naming, documentation, hidden dependencies
        - Complexity is incremental: use bangkok picture
          - This is why it's also called "technical debt"
    - Properties of good code
      - Good code is obvious
      - Good code is easier to change (ETC: easier to change)
      - Good code doesn't repeat itself (DRY: don't repeat yourself)
      - Orthogonality
      - Reversibility (?)

- Strategic vs tactical programming
  - PP calls this programming by coincidence vs deliberate programming
  - ...

- Modules should be deep
  - Modules have an interface and an implementation
  - Interface: what a developer needs to know in order to use the module
  - Abstraction: a simplified view of an entity, which omits unimportant details
    - Modules provide abstractions of their interfaces
    - An abstraction that omits important details is a false (or leaky) abstraction
    - Abstractions typically form layers
      - Red flag: pass-through method (use figure 7.1)
  - Deep modules (use figure 4.1 and unix file system example)
  - Shallow modules (use example in section 4.5)
  - Classitis: using classes doesn't automatically make your code "cleaner"
    - Use FileInputStream example p35
  - Information hiding and leakage
    - Red flags: information leakage and temporal decomposition
    - Use HTTP server example?
  - General-purpose modules are deeper
    - Difference between general-purpose and special-purpose modules
    - A module's functionality should reflect your current needs, but its interface should not
      - Example: storing text for an editor
    - Generality leads to better information hiding
    - Questions to ask yourself
      - What is the simplest interface that will cover all of my current needs?
      - In how many situations will this method be used?
      - Is this API easy to use for my current needs?

- Writing comments
  - The four excuses
  - Comments should describe things that aren't obvious

- Tips & tools
  - Choosing names
  - Assertive programming
  - Design it twice
  - Refactoring
  - Tracer bullets
  - Prototypes
  - Don't outrun your headlights
  - Write the comments first (chapter 16)

- Testing
  - Unit testing
  - Property testing
  - Design for testability
  - Test to help you think

- Design patterns
  - What are design patterns
  - Dependency injection
  - Decorator
  - Dispatcher (see philosophy 7.2)
  - ...

- Core principles
  - Design by contract
  - Decoupling


- Move to devops slides
  - Plain text
  - External configuration
  - Power editing (challenge: learn vim bindings, learn to use your editor with as little mouse as possible)
  - Mastering the shell, piping (challenge: try living in the terminal as much as possible)
