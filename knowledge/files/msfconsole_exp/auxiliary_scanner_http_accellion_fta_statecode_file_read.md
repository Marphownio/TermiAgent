**The description of current metasploit exploit**
This module exploits a file disclosure vulnerability in the Accellion          File Transfer appliance. This vulnerability is triggered when a user-provided          'statecode' cookie parameter is appended to a file path that is processed as          a HTML template. By prepending this cookie with directory traversal sequence          and appending a NULL byte, any file readable by the web user can be exposed.          The web user has read access to a number of sensitive files, including the          system configuration and files uploaded to the appliance by users.          This issue was confirmed on version FTA_9_11_200, but may apply to previous          versions as well. This issue was fixed in software update FTA_9_11_210.

**The usage instruction:**

Start by loading the module:

```bash
use auxiliary/scanner/http/accellion_fta_statecode_file_read
```

Then set the required options:

```bash
# Required parameters with no default value
set RHOSTS <your target host(s) here>
# Repeat for each required parameter from Step 1
```

Carefully review the following network-related parameters. These have default values but **may need to be changed** depending on your environment:

* RPORT – default: 443 - The target port (TCP)

If the defaults match your setup, you do **not** need to change them. Otherwise, override them using `set`.

Finally, run the exploit:

```bash
exploit
```
Note:
1. Please execute the command step by step.
2. You can change default value if need.
3. You need to pay attention to whether the default RPORT is consistent with the port where the current service is running.