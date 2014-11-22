projectapple
================


Code for intuit hackathon

# Setting up your environment
Be sure to have the following dependencies:

- Python 2.7 (http://www.python.org)

## Some Prereqs

### Install Ruby & RubyGems
After installing Ruby, run the following command to install the first set of
front-end dependencies.

    gem update --system && gem install compass

### Install Node.js requirements
Make sure you are in the root of the project where the package.json file
is located.

    npm install

### Alternative npm and Node.js Installation
If you are having problems with installing npm, or installing Node.js, try one
of these alternatives:
[https://gist.github.com/isaacs/579814](https://gist.github.com/isaacs/579814).


### Install Javascript/CSS dependencies
Next we make sure bower ( a javascript/css package manager ) is installed and
accessible globally. You may need admin access to install globally. (learn more about bower: bower.io)

    (sudo) npm install -g bower
    bower install


## Backend environment
Make sure you have the following Python modules installed:

- pip ( http://pip.readthedocs.org/en/latest/installing.html )
- virtualenv  ( https://virtualenv.pypa.io/en/latest/)
- virtualenvwrapper ( http://virtualenvwrapper.readthedocs.org/en/latest/ )


### Create your development workspace (run this only the very first time)
    mkvirtualenv projectapple
    pip install -r reqs.txt

### From now on you should this run to get back on the environment
    workon projectapple 


