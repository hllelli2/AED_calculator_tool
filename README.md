# PYTHON COURSE - WORK IN PROGRESS

# AED calculator tool

Gene models can be assessed using mapped transcript or protein evidence using a metric called annotation edit distance (AED). The theory behind this can be found at https://link.springer.com/article/10.1186/1471-2105-10-67. 

This can be a useful measure to assess gene predictor accuracy. Here you can find a simple tool for calculating AED per gene model, given some evidence.


#####################



# PythonProjectTemplate
Template for Python projects


### Development setup

Before we start developing, make sure you have the following tools installed:

Prerequisites:
- pipx

pipx is a tool to help you install and run Python applications in isolated environments. It is all we need to install the rest of the development tools.

1. Install pipx if you haven't already. You can find instructions [here](https://pipxproject.github.io/pipx/installation/).

2. Use pipx to install nox, uv (Universal Versioner), and pre-commit:
Note: The `[pbs]` extra for nox includes additional plugins, allowing it to download Python.

```bash
pipx install nox[pbs] uv pre-commit
```

3. Now, we can use nox to set up our development environment. Run the following commands in your terminal:

```bash
 nox -s install 
```

This command will create a virtual environment and install all the development dependencies specified in the `pyproject.toml` file. Populate the pyproject.toml file with your desired dependencies before running this command. *Note: You can run this command multiple times to ensure all dependencies are installed correctly.*

```bash

nox -s chores 
```

This command will run various code quality and formatting tools to ensure your code adheres to best practices.

```bash
 nox -s tests 
```

This command will run the test suite to ensure everything is working as expected.

```bash
 nox -s lock 
```

This command will update the lock files for your dependencies to ensure you have the latest compatible versions.


4. (Optional) (But recommended) Set up pre-commit hooks to automatically run code quality checks before each commit:

```bash
 pre-commit install 
```

This command will install the pre-commit hooks defined in the `.pre-commit-config.yaml` file. This helps maintain code quality by running checks before each commit.

That's it! You now have a fully set up development environment for your Python project. You can start coding, and the tools will help you maintain code quality and consistency. When you want to run Python scripts, please use:

```bash
uv run python ./path/to/myscript.py
```

   



