# service fingerprint
<chunk>

To identify the service, you need to try the following in sequence:

1. Firstly, analyse the url with port by `whatweb` command.
For example, `whatweb http://<ip>:<port>` for http server or `whatweb https://<ip>:<port>` for https server, 

2. If the Whatweb method doesn't find the target server, then analyse the url with port by `curl` command.
For example, `curl -i http://<ip>:<port>` for http server or `curl -i https://<ip>:<port>` for https server, in order to identify the corresponding service in the returned HTML code
</chunk>