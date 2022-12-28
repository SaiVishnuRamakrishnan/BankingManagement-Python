#!"C:\Users\vijay\AppData\Local\Programs\Python\Python37-32\pythonw.exe"
import pyodbc

import random
def pas():
    a=[chr(b) for b in range(ord('a'),ord('z')+1)]
    b=[chr(b) for b in range(ord('A'),ord('Z')+1)]
    c=[chr(b) for b in range(ord('0'),ord('9')+1)]
    sy=['@','!','&','*','#','@']
    password=''

    password+=str(random.choice(a))
    password+=str(random.choice(b))
    password+=str(random.choice(c))
    password+=str(random.choice(sy))
    a=a+b+c+sy
    for b in range(5):
        password+=str(random.choice(a))
    return password
try:
    import cgi
    form = cgi.FieldStorage()
    name=form.getvalue('n')
    mobile=form.getvalue('mo')
    email=form.getvalue('email')
    password=pas()
    conn=pyodbc.connect('Driver={SQL Server};''Server=suresh-pc;''Database=bank')
    z=conn.execute('insert into bank(name,password,mobile,emailid,balance) values (?,?,?,?,?)',(name,password,mobile,email,"500"))
    conn.commit()
    b=conn.execute("select top 1 accountno, password,emailid from bank order by id desc")
    for c in b:
       pass
    import smtplib
    msg="username- "+c[0]+"password- "+c[1]
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("hariharanvimal@gmail.com", "hari@niit")
    server.sendmail("hariharanvimal@gmail.com",str(c[2]) , msg)
    print("""
<html>
<head>
    <title>Suresh Bank</title>
<script>
setTimeout(function()
		{
			window.location.href='index.py'
			},0);
			alert('Account no and Password is mailed to %s')
		</script>
</head>

<body>

</body>
</html>
""" %(email))
    
    
except Exception as e:
    
    print("""
<html>
<head>
    <title>Suresh Bank</title>
<script>
setTimeout(function()
		{
			window.location.href='first.py'
			},0);
			alert('Error in creating try again later')
		</script>
</head>

<body>

</body>
</html>
""" )
