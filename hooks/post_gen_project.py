import subprocess

init_instructions = [
    "pip install --upgrade pip".split(),
    "git init".split(),
    "poetry install --with dev".split(),
]

print("Initializing repository and installing development dependencies")

for i in init_instructions:
    subprocess.run(i, stdout=subprocess.DEVNULL)

subprocess.run(
    'git add --a && git commit -m "Initial Commit"',
    shell=True,
    stdout=subprocess.DEVNULL,
)

print("Collecting and initializing pre-commit scripts")
precommit_instructions = [
    "poetry run pre-commit install".split(),
    "poetry run pre-commit run --all-files".split(),
]

for c in precommit_instructions:
    subprocess.run(c, stdout=subprocess.DEVNULL)

print("Pre-commit scripts configured: Running for initial commit")
subprocess.run(
    "git add --a && git commit --amend --no-edit", shell=True, stdout=subprocess.DEVNULL
)

print("Configuration successful! Entering virtual environment.\n")

subprocess.run("poetry shell".split())
