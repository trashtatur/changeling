![alt text](images/changeling.png )

#CHANGELING
## A wonderdraft profile manager

Changeling manages profiles for wonderdraft based on provided .yml configuration files.
It provides an easy to use command line interface to offer its functionality

A sample configuration file for changeling can look like this

### Profile example

````yaml
name: dungeon
modules:
  - "Dungeon Architecture"
  - "Dungeon Interior"
````

The modules listed, correspond to top level folders in the wonderdraft asset directory.
Right now changeling assumes that wonderdraft uses its standard directory for assets. That 
will be configurable in a later release.

### Installation

Changeling can be installed easily by cloning this github repository and installing
python on your local machine (docker functionality might come later...).

Then change into the downloaded repository and type the following:
``pip install --editable .``

After that you'll be able to use changeling in the commandline by typing ``changeling``.
It'll show you its available commands. In the beginning it'll just be a setup command

### Disclaimer

changeling is still in a really early release. I won't be responsible for any damage to your
wonderdraft assets or installation or whatever else. If you need support, create an issue or
contact me on the wonderdraft discord / reddit . Also right now changeling doesn't really have
all its functionality yet.