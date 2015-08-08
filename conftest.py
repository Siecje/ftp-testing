import os
import threading
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from FTP import server


@pytest.fixture(scope="session")
def run_ftp():
    FTPReady = threading.Event()
    t = threading.Thread(target=server.main, args = (FTPReady, ))
    t.setDaemon(True)
    t.start()
    return FTPReady

