**The description of current metasploit exploit**
Generates a `GET` request to the provided web servers and executes an SSRF against                        the targeted EMBY server. Returns the server header, HTML title attribute and                        location header (if set). This is useful for rapidly identifying web applications                        on the internal network using the Emby SSRF vulnerability (CVE-2020-26948).

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/emby_ssrf_scanner
```

Then set the required options:

```bash
# Required parameters with no default value
set EMBY_SERVER <your Emby Web UI IP here>
set RHOSTS <your target host(s) here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* EMBY_PORT – default: 8096 - Web UI port for Emby Server
* PORTS – default: 80,8080,8081,8888 - Ports to scan

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.