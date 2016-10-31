# cs4032 Lab 1 - Echo Client

Depends on [`clize`](https://github.com/epsy/clize) for pain-free CLI generation

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
