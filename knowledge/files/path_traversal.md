# path traversal
<chunk>

You can try to get the web page first:
```bash
curl http://<url>:<port>
```
If you do not get any HTML page after using the `curl` command, then your conditions do not meet expectations.

If the resulting HTML page contains tags that specify optional page parameters (e.g. `?page=` or `?p=`), we can try to modify the parameters to access the specified file. When summarizing, you need to focus on whether there are such parameters
 
For example, if you observe the html page hints at the available parameters `?p=`, you can construct the following command to access the file you want:
```bash
curl http://<url>:<port>?p=<path to the file you want>
```


The file path can be an absolute path like `/root/flag.txt`, or relative path `../../../root/flag.txt`. To avoid possible checks, you can replace a `../../` with a `..././`. If the target file cannot be found, you can try increasing the number of `../../`



</chunk>