# next-python-web-platfor



<br>

## Usage

The repository employed Next.js and Python for the backend to build the website environment.
In the `frontend/` directory, place the Next.js project and the associated eslint, prettier and stylelintrc configurations. In the `backend/` directory, we will put the Python code and Python lint tools (flake8 and black). husky will be placed in the root directory and configured to run both frontend and backend lint. Configure GitHub Actions to automatically run CI/CD tasks. We also built a Docker environment.

<br>

## Article

- https://zenn.dev/arsaga/articles/0fdee431a8374a <br>
- https://zenn.dev/arsaga/articles/d07358c709bc73

<br>

## Installation

#### frontend

```zsh
cd frontend
npm i
```

<br>

#### backend

```zsh
cd backend
./pip_install.sh <package_name>
```
