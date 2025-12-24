"""
WebSocket channels example for Tufts Hub.

Demonstrates real-time pub/sub messaging using WebSocket channels.
"""

from pyscript import WebSocket, when, web, window

# Global WebSocket connection.
ws = None
current_channel = None


def connect_to_channel(channel_name):
    """
    Connect to a WebSocket channel.
    """
    global ws, current_channel

    # Close existing connection if any.
    if ws:
        ws.close()

    # Build WebSocket URL (use wss:// for HTTPS, ws:// for HTTP).
    protocol = "wss" if window.location.protocol == "https:" else "ws"
    host = window.location.host
    url = f"{protocol}://{host}/channel/{channel_name}"
    print(url)

    # Create WebSocket connection.
    ws = WebSocket(url=url)
    ws.onopen = on_open
    ws.onmessage = on_message
    ws.onclose = on_close
    ws.onerror = on_error

    current_channel = channel_name


def on_open(event):
    """
    Handle WebSocket connection opened.
    """
    print(f"Connected to channel: {current_channel}")

def on_message(event):
    """
    Handle incoming message from WebSocket.
    """
    print('received')
    print(event.data)

def on_close(event):
    """
    Handle WebSocket connection closed.
    """
    print("Disconnected")

def on_error(event):
    """
    Handle WebSocket error.
    """
    print("Connection error - please refresh and login")

@when("click", "#connect-button")
def handle_connect(event):
    """
    Handle connect button click.
    """
    connect_to_channel('hackathon')

@when("click", "#send-button")
def handle_send(event):
    """
    Handle send button click.
    """
    # Send message to WebSocket.
    if ws:
        print('sending')
        ws.send('testing')
