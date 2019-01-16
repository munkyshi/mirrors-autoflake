from setuptools import setup


setup(
    name='pre_commit_dummy_package',
    version='0.0.0',
    install_requires=['autoflake==v1.3.dev0'],
    dependency_links=[
        "https://munkyshi.github.io/python-packages/autoflake",
    ],
)
