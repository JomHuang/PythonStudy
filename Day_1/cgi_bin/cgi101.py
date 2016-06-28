#!C:\Users\Administrator\AppData\Local\Programs\Python
import cgi;

form = cgi.FieldStorage();
print('Content-type:text/html\n');
print('<title>reply page</title>');

if not 'user' in form:
    print(' <h1>who are you?</h1>');
else:
    print('<h1>hello <i>%s</i></h1>' % cgi.escape(form['user'].value));
