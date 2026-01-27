from setuptools import setup, find_packages

setup(
    name="mkdocs-list-callouts",
    version="0.2.0",
    author="EmergentTwilight",
    description="MkDocs List Callouts Plugin",
    url="https://github.com/EmergentTwilight/mkdocs-list-callouts",
    python_requires=">=3.8",
    install_requires=[
        "mkdocs>=1.4.0",
    ],
    packages=find_packages(),
    entry_points={"mkdocs.plugins": ["list_callouts = mkdocs_list_callouts.list_callouts:ListCalloutsPlugin"]},
    include_package_data=True,
)
