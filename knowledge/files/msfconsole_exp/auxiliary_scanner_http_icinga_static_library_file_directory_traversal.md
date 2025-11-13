**The description of current metasploit exploit**
Icingaweb versions from 2.9.0 to 2.9.5 inclusive, and 2.8.0 to 2.8.5 inclusive suffer from an          unauthenticated directory traversal vulnerability. The vulnerability is triggered          through the icinga-php-thirdparty library, which allows unauthenticated users          to retrieve arbitrary files from the targets filesystem via a GET request to          /lib/icinga/icinga-php-thirdparty/<absolute path to target file on disk> as the user          running the Icingaweb server, which will typically be the www-data user.          This can then be used to retrieve sensitive configuration information from the target          such as the configuration of various services, which may reveal sensitive login          or configuration information, the /etc/passwd file to get a list of valid usernames          for password guessing attacks, or other sensitive files which may exist as part of          additional functionality available on the target server.          This module was tested against Icingaweb 2.9.5 running on Docker.

---

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/icinga_static_library_file_directory_traversal
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 8080 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.