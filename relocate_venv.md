 cd ~/first

$ virtualenv my-venv

$ grep 'VIRTUAL_ENV=' my-venv/bin/activate

VIRTUAL_ENV="/home/username/first/my-venv"

$ virtualenv --relocatable my-venv

Making script my-venv/bin/easy_install relative
Making script my-venv/bin/easy_install-2.7 relative
Making script my-venv/bin/pip relative
Making script my-venv/bin/pip2 relative
Making script my-venv/bin/pip2.7 relative
### Note that `activate` has not been touched
$ mkdir ~/second
$ mv my-venv ~/second
$ cd ~/second
$ grep 'VIRTUAL_ENV=' my-venv/bin/activate
VIRTUAL_ENV=/home/username/first/my-venv
### (This variable hasn't been changed, it still refers to the old, now non-existent directory!)
$ sed -i -e 's|username/first|username/second|' my-venv/bin/activate
## sed can be used to change the path.
## Note that the `-i` (in place) flag won't work on all machines.
$ source my-venv/bin/activate
(my-venv) $ pip install foass
...
(my-venv) $ python
[...]
> import foass
