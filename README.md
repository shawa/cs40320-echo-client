# cs4032 Lab 1 - Echo Client

Depends on python3 for runtime.
Depends on [`clize`](https://github.com/epsy/clize) for pain-free CLI generation.

## Setup/running
Ensure python3 is installed and that `venv`s are working.

Then:

```
# initialize a venv and install dependencies
./createvirtualenv.sh

# use env created for this projct
source env/bin/activate

# show usage instructions
python3 client.py -h
```

For possible `<ARGUMENTS>`, run `./env/bin/python3 client.py -h` or see:

```
Usage: client.py [OPTIONS] portnumber

http exercise.

Arguments:
  portnumber       port remote echo server is listening on

Options:
  --hostname=STR    (default: 127.0.0.1)
  -v, --verbose
  --endpoint=STR   name of the endpoint to request, eg 'echo.php' (default:
                   echo.php)
  --message=STR    message to send to echo server (default: Hello, world!)

Other actions:
  -h, --help       Show the help
```


## Example run

From the client
```
~shawa@vm-62.0.10:source env/bin/activate
› python3 client.py --hostname 10.62.0.199 9876 --message="Hello, world"
HELLO, WORLD\n

~/repos/cs40320-echo-client master cs40320-echo-client

# again, with the --verbose option to show headers and status
› python3 client.py --hostname 10.62.0.199 9876 --message="Hello, world" --verbose
Status: HTTP/1.1 200 OK
Headers:
  Content-type: text/html; charset=UTF-8
  Host: 10.62.0.199:9876
  Connection: close
  X-Powered-By: PHP/5.6.24-0+deb8u1
Body:
 'HELLO, WORLD\\n'


```


And the server console:
```
root@vm-62-0-199:~/servers# php -S 0.0.0.0:9876
PHP 5.6.24-0+deb8u1 Development Server started at Tue Nov  1 16:29:58 2016
Listening on http://0.0.0.0:9876
Document root is /root/servers
Press Ctrl-C to quit.
[Tue Nov  1 16:30:08 2016] 10.62.0.10:37064 [200]: /echo.php?message=Hello%2C+world
[Tue Nov  1 16:30:13 2016] 10.62.0.10:37065 [200]: /echo.php?message=Hello%2C+world
