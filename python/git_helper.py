#!/Users/siyer/virtualenv/flask/bin/python

import sh

sh.cd("/Users/siyer/workspace/github/scripts")
print sh.git("pull")
