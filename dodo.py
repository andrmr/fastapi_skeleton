def task_build():
    """Builds image"""
    return {
        "actions": [
            "poetry export --without-hashes --format=requirements.txt > requirements.txt",
            "docker build -t app .",
        ],
        "verbosity": 2,
    }


def task_check():
    """Runs checks"""
    targets = " ".join(("./dodo.py", "./app", "./tests"))
    return {
        "actions": [
            "poetry install --with dev",
            f"poetry run mypy {targets}",
            f"poetry run ruff check {targets}",
            f"poetry run black {targets}",
        ],
        "verbosity": 2,
    }


def task_test():
    """Runs tests"""
    return {
        "actions": [
            "poetry install --with test",
            "poetry run pytest -s --verbose --color yes",
        ],
        "verbosity": 2,
    }
