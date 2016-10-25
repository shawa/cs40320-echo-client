import clize
import socket
import time
from collections import namedtuple
from urllib.parse import quote_plus

Response = namedtuple('Response', ['status', 'headers', 'body'])


class Response:
    def __init__(self, raw_response):
        """
        parse a response bytes into a Response object with members

        status  : http status code line of the reposne
        headers : a dict whose keys are http header keys, values are
                  http header values
        body    : the raw body of the response
        """
        DELIM = '\r\n'
        head, self.body = raw_response.decode('utf-8').split(DELIM*2)
        self.status, *header_lines = head.split(DELIM)

        self.headers = dict(line.split(': ') for line in header_lines)


    def pretty_print(self, verbose=False):
        if verbose:
            print('Status: {}'.format(self.status))
            print('Headers:')
            for k, v in self.headers.items():
                print('  {}: {}'.format(k, v))

            print('Body:')
            print(' ' + repr(self.body))
        else:
            print(self.body)


def build_request(**kwargs):
    """
    from a basic template, according to the fields specified in kwargs,
    return a bytes of a GET corresponding to those values

    fields are:
        endpoint : resource requested
        message  : message to request to be echoed
        hostname : hostname of server
        port     : server port
    """
    HTTP_REQ_TEMPLATE = [
       'GET /{endpoint}?message={message} HTTP/1.1',
       'Host: {hostname}:{portnumber}',
       'Accept: text/plain',
       '\r\n'
    ]

    return ("\r\n".join(HTTP_REQ_TEMPLATE)
                  .format(**kwargs)
                  .encode('utf-8'))


def read_until_exhausted(sock, chunk_size=1024):
    """
    for a given `sock`et, `recv` it until there's no more data to read
    yields chunks of size `chunk_size`
    """
    data = True
    while data:
        data = sock.recv(chunk_size)
        yield data


def main(portnumber, *, endpoint='echo.php', message='Hello, world!',
         hostname='127.0.0.1', verbose:'v'=False):
    """
    http exercise.

    portnumber: port remote echo server is listening on

    endpoint: name of the endpoint to request, eg 'echo.php'

    message: message to send to echo server
    """

    port = int(portnumber)
    message_qstring = quote_plus(message)

    sock = socket.socket()
    sock.connect((hostname, port))

    sock.sendall(build_request(endpoint=endpoint, message=message_qstring,
                               hostname=hostname, portnumber=port))

    raw_response = b''.join([chunk for chunk in read_until_exhausted(sock)])

    resp = Response(raw_response)
    resp.pretty_print(verbose)

if __name__ == '__main__':
    clize.run(main)
