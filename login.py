#!"C:\Users\vijay\AppData\Local\Programs\Python\Python37-32\pythonw.exe"
print("Content-Type: text/html")    
print()
import pyodbc#python open database connectivity
conn=pyodbc.connect('Driver={SQL Server};''Server=suresh-pc;''Database=bank')
import cgi
form = cgi.FieldStorage()
name=form.getvalue('n')
pas=form.getvalue('mo')
b=conn.execute("select * from bank where accountno=? and password=?",(name,pas))
for c in b:
   pass
try:    
    if c[0]!=0:
           print("""
    <html>
    <head >
        <title>Suresh Bank</title>
    <script >
    setTimeout(function()
                    {
			window.location.href='account.py?ac=%s&c=%s'
			},0);
			alert('logged successfuly')
		</script>
    </head>
    
    <body>
    
    </body>
    </html>
    """ %(c[1],c[2]))

except Exception as e:
            print("""
<html>
<head>
    <title>Suresh Bank</title>
<script>
setTimeout(function()
		{
			window.location.href='index.py'
			},0);
			alert('Wrong user')
		</script>
</head>

<body>

</body>
</html>
""")
