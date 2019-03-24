#!/usr/bin/env python
from subprocess import *
call("apt-get update",shell=True)
call("apt-get upgrade -y",shell=True)
call("apt-get install tightvncserver"shell=True)

