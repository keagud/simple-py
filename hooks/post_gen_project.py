import subprocess

# generate venv and install dependencies in it
subprocess.run("env python -m virtualenv  .venv", shell=True)

# move the activation script into the venv, since it often doesn't generate in place

subprocess.run("mv .activate_this.py .venv/bin/activate_this.py", shell=True)


print("Initializing repository and installing development dependencies")

init_instructions = [
    i.split()
    for i in [
        "pip install --upgrade pip",
        "poetry config virtualenvs.in-project true",
        "poetry install --with dev",
        "git init",
    ]
]

for i in init_instructions:
    subprocess.run(i)

# activate the venv
activator = ".venv/bin/activate_this.py"

with open(activator) as f:
    exec(f.read(), {"__file__": activator})

# make the initial git commit
subprocess.run(
    'git add --a && git commit -m "Initial Commit"',
    shell=True,
    stdout=subprocess.DEVNULL,
)

print("Collecting and initializing pre-commit scripts")
precommit_instructions = [
    "poetry run pre-commit autoupdate",
    "poetry run pre-commit install",
    "poetry run pre-commit run --all-files",
    "poetry run pre-commit run --all-files",
]

for c in precommit_instructions:
    subprocess.run(c.split(), stdout=subprocess.DEVNULL)

print("Pre-commit scripts configured: Running for initial commit")
subprocess.run(
    "git add --a && git commit --amend --no-edit", shell=True, stdout=subprocess.DEVNULL
)

print("Configuration successful! Entering virtual environment.\n")

subprocess.run("poetry shell", shell=True)
