import subprocess

packages = [
    "hyperopt", "ipywidgets", "matplotlib", "mlflow", "nltk", "numpy", "numpyencoder",
    "pandas", "python-dotenv", "ray[air]", "scikit-learn", "snorkel==0.9.9", "SQLAlchemy",
    "torch", "transformers", "cleanlab", "jupyterlab", "lime", "seaborn", "wordcloud",
    "mkdocs", "mkdocs==1.6.1", "mkdocstrings[python]>=0.18", "black", "flake8",
    "Flake8-pyproject", "isort", "pyupgrade", "great-expectations", "pytest", "pytest-cov",
    "fastapi", "pre-commit", "typer", "anyscale"
]

for package in packages:
    try:
        subprocess.check_call(["python", "-m", "pip", "install", package])
        print(f"✅ Successfully installed {package}")
    except subprocess.CalledProcessError:
        print(f"❌ Failed to install {package}")
