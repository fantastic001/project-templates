#!python

import sys 
import os 
import os.path
import json 
import logging
from ArgumentStack import * 

from {{ project_name }} import * 

FORMAT = '%(asctime)-15s  %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('{{ project_name }}')
logger.debug('Starting application')

config = {}

try:
    config = json.loads(open("%s/.config/{{ project_name }}/{{ project_name }}.json" % os.environ["HOME"]).read())
except:
    print("Configuration cannot be read in ~/.config/{{project_name}}/{{ project_name }}.json")

stack = ArgumentStack("Wrong command") 
stack.popAll()
stack.pushCommand("help")
stack.assignAction(lambda: print(stack.getHelp()), "Get help")
stack.popAll()
