**The description of current metasploit exploit**
On Titan FTP servers prior to version 9.14.1628, an attacker can      retrieve the username and password for the administrative XML-RPC      interface, which listens on TCP Port 31001 by default, by sending an      XML request containing bogus authentication information. After sending      this request, the server responds with the legitimate username and      password for the service. With this information, an attacker has      complete control over the FTP service, which includes the ability to      add and remove FTP users, as well as add, remove, and modify      available directories and their permissions.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/titan_ftp_admin_pwd
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
# Repeat for each required parameter from Step 1
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 31001 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.