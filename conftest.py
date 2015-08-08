import os
import multiprocessing
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from FTP import server


@pytest.fixture(scope="session")
def run_ftp():
    p = multiprocessing.Process(target=server.main)
    p.start()
