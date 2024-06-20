# Git & GitHub Basics

Welcome to the Git & GitHub Basics Repository! This repository is designed to help you understand the fundamentals of Git and GitHub and provide you with basic commands to get started.

## What is Git?

Git is a distributed version control system that helps you track changes to files and coordinate work on those files among multiple people. It is commonly used for source code management in software development.

### Key Features of Git

- **Version Control**: Keeps a history of changes and allows you to revert to previous states.
- **Collaboration**: Multiple people can work on the same project simultaneously.
- **Branching and Merging**: Enables you to work on different features or fixes in isolation and merge them back together.

## What is GitHub?

GitHub is a web-based platform that uses Git for version control. It allows you to host and manage your Git repositories, collaborate with others, and use various tools to enhance your workflow.

### Key Features of GitHub

- **Repository Hosting**: Stores your code in repositories.
- **Collaboration Tools**: Issues, pull requests, and project boards to manage work.
- **Integration**: Works with various CI/CD tools and other services.

## Basic Git Commands

Here are some basic Git commands for common tasks:

### Configuration

- **Set up your user name and email:**
  ```sh
  git config --global user.name "Your Name"
  git config --global user.email "your.email@example.com"
  ```

### Repository Operations

- **Initialize a new Git repository:**
  ```sh
  git init
  ```

- **Clone an existing repository:**
  ```sh
  git clone https://github.com/username/repository.git
  ```

### Working with Changes

- **Check the status of your files:**
  ```sh
  git status
  ```

- **Add changes to the staging area:**
  ```sh
  git add filename
  # or to add all changes
  git add .
  ```

- **Commit changes with a message:**
  ```sh
  git commit -m "Your commit message"
  ```

### Branching and Merging

- **Create a new branch:**
  ```sh
  git branch branch-name
  ```

- **Switch to a branch:**
  ```sh
  git checkout branch-name
  ```

- **Merge a branch into the current branch:**
  ```sh
  git merge branch-name
  ```

### Remote Repositories

- **Add a remote repository:**
  ```sh
  git remote add origin https://github.com/username/repository.git
  ```

- **Push changes to a remote repository:**
  ```sh
  git push origin branch-name
  ```

- **Pull changes from a remote repository:**
  ```sh
  git pull origin branch-name
  ```

## Conclusion

This repository provides an introduction to Git and GitHub, as well as some basic commands to help you get started. For more detailed information, refer to the [Git documentation](https://git-scm.com/doc) and [GitHub documentation](https://docs.github.com/).
