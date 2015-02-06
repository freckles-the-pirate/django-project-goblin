from distutils.core import setup

with open('README.md') as f:
    LONG_DESCRIPTION=f.read()
    f.close()

setup(
    name='django-project-goblin',
    version='1.0',
    description='Manage list of projects',
    long_description=LONG_DESCRIPTION,
    author="Jordan Hewitt",
    author_email='jordannh@sent.com',
    url='https://gitorious.org/django-project-goblin',
    packages=('goblin',),
)
