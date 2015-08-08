import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


HOST = '0.0.0.0'
PORT = 2121
USER = 'user'
PASSWD = '12345'

THIS_DIR = os.path.dirname(os.path.realpath(__file__))


def main(RdyEvent = None):
    if 0: # for Wing
        import threading
        assert isinstance(RdyEvent, threading._Event)
    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = DummyAuthorizer()

    # Define a new user having full r/w permissions
    authorizer.add_user(USER, PASSWD, THIS_DIR, perm='elradfmwM')

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # Instantiate FTP server class and listen on 0.0.0.0:2121
    address = ('', PORT)
    server = FTPServer(address, handler)

    # start ftp server
    if RdyEvent:
        RdyEvent.set()
    server.serve_forever()


if __name__ == '__main__':
    main()
