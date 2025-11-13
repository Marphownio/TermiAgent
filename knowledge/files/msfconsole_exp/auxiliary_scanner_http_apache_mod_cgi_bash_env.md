**The description of current metasploit exploit**
This module scans for the Shellshock vulnerability, a flaw in how the Bash shell          handles external environment variables. This module targets CGI scripts in the          Apache web server by setting the HTTP_USER_AGENT environment variable to a          malicious function definition.          PROTIP: Use exploit/multi/handler with a PAYLOAD appropriate to your          CMD, set ExitOnSession false, run -j, and then run this module to create          sessions on vulnerable hosts.          Note that this is not the recommended method for obtaining shells.          If you require sessions, please use the apache_mod_cgi_bash_env_exec          exploit module instead.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/apache_mod_cgi_bash_env
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
set TARGETURI <your path to CGI script here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 80 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.