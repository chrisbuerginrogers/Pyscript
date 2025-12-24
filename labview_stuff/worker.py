import time
import os
import threading
from thub.server import start_server, stop_server

server = []
logs = []  # Global log buffer

def read_output(process, log_list):
    """Thread function to read stdout from process."""
    for line in process.stdout:
        decoded = line.decode('utf-8').strip()
        if decoded:
            log_list.append(decoded)

def start(): 
    global server, logs
    os.chdir('/Users/crogers/GitHub/Pyscript/techelements')
    new = start_server(host="127.0.0.1", port=8006, block=False)
    
    # Start a thread to buffer the output
    log_thread = threading.Thread(target=read_output, args=(new, logs), daemon=True)
    log_thread.start()
    
    server.append(new)
    return len(server)

def end(n):
    global server
    stop_server(server[n])

def get_logs(clear=True):
    """Get all buffered logs. Set clear=True to empty buffer after reading."""
    global logs
    current_logs = logs.copy()
    if clear:
        logs.clear()
    return current_logs