from pyscript import document, window, when, sync
await window.init.promise

import asyncio

import code
code.interact()

from pyscript.js_modules import code_editor
python_terminal = document.getElementById("python-terminal")

@when('click','#REPLRun')
async def typeIt():
    python_terminal.process('\x03')
    mycode = code_editor.editor.getValue()
    lines = mycode.split("\n")
    #python_terminal.process('\x05')
    for line in lines:
        #for char in line:
        #    python_terminal.terminal.write(char)
        #python_terminal.terminal.write("\x1b[2K\r>>> ")
        python_terminal.process(line)
        await asyncio.sleep(0.1)
    #python_terminal.process('\x04')

def wait(waitTime):
    sync.wait(waitTime)

class Channel:
    def __init__(self):
        self.message = None
    def msg(self):
        return sync.fred('msg',None)
    def send(self, msg):
        return sync.fred('post',msg)

channel = Channel()

def waiting(msg, task = 'time'):
    if task == 'time':
        sync.wait(msg)
    elif task == 'channel':
        sync.wait_channel(msg)

class Wait:
    def time(self, waitTime):
        waiting(waitTime)
    def channel(self, msg):
        waiting(msg, 'channel')

wait = Wait()

class Motor:
    def hubType(self):
        return sync.george('hubType')
    def read(self):
        reply = sync.george('reply')
        self.position = reply['Motor_1']['position']
        self.angle = reply['Motor_1']['angle']
        self.speed = reply['Motor_1']['speed']
        self.battery = reply['hub info']['Battery']
        return self.position
    def run(self, speed = 100, port = 1, direction = 2):
        return sync.george("run", speed=speed, port=port, direction=direction)

'''
def run(speed = 100, port = 1, direction = 2):
def myspeed(speed_value = 100, port = 1): 
def stop(port = 1):    
def moveAngle(angle = 100, direction = 1):   
def movePos(pos = 100, direction = 2):
'''

motor = Motor()