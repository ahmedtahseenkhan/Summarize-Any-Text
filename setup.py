import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()


REPO_NAME = "Summarize Any Text",
AUTHOR_USER_NAME = "ahmedtahseenkhan"
SRC_REPO = "Summarize-Any-Text"
AUTHOR_EMAIL = "ahmed.tahseen.khan@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version="1.0",
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)