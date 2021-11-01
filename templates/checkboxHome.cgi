// #!/usr/bin/python
// import cgi
// cgitb.enable()
// import cgitb

#!/usr/bin/python/

// # Import modules for CGI handling
import cgi, cgitb

// # Create instance of FieldStorage
form = cgi.FieldStorage()

// # Get data from fields
if form.getvalue('Cloud'):
   Cloud_flag = "ON"
else:
   Cloud_flag = "OFF"

if form.getvalue('DB'):
   DB_flag = "ON"
else:
   DB_flag = "OFF"

if form.getvalue('AI'):
   AI_flag = "ON"
else:
   AI_flag = "OFF"

if form.getvalue('NonTech'):
   NonTech_flag = "ON"
else:
   NonTech_flag = "OFF"
