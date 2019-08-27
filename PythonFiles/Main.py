import time

from PythonFiles.Controller import Controller

running = True
controller = Controller()

while running:
    lastCheck = controller.runChecks()
    time.sleep(3600)