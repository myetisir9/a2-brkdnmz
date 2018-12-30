
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import route, run, default_app, debug, template, static_file, get, request, post
from hashlib import sha256

def hashcreator(pw):
    pw_bytestring = pw.encode()
    return sha256(pw_bytestring).hexdigest()
    
real_password_hash="378bc297aed78d68f2aa8dbb2064d8beb85f42fab45e1062e1749659a25b0524"


def htmlify(title,text):
    page = """
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8" />
                <title>%s</title>
            </head>
            <body>
            %s
            </body>
        </html>

    """ % (title,text)
    return page


	
    
@route("/")
def index():
	return template("index.html")
	
@route("/<filename:re:.*\.html>")
def website(filename):
	return template(filename, root="/")

@route("/static/<filename>")
def static(filename):
	return static_file(filename, root="./static")
	
login="""
	<form action="/comments.html" autocomplete="on">
	 <fieldset>
	  <legend>You Should Fill Those:</legend>
	  Name you want to be seen with:
	  <input type="text" name="nickname" size="36"
	  placeholder="Like 'crazy_boi', 'ituis18_student', 'ignore_me'..." autofocus required><br><br>
      The secret password you have to put in there:
	  <input type="password" name="password" placeholder="A very secret password :) ..." autocomplete="off" required><br><br>
	  Whose student are you?<br><br>
	  <input type="radio" name="lecturer" value="djduff">Damien Jade Duff<br>
	  <input type="radio" name="lecturer" value="turgutuyar">Hayri Turgut Uyar
	  <br><br>
	  Are you a boy or a girl?
	  <select name="gender">
	   <option value="boy">Boy</option>
	   <option value="girl">Girl</option>
	  <br><br>
	  <input type="image" src="./static/login_icon.gif" title="Login" alt="Login" width=100 height=100>
	 </fieldset>
	</form>
	"""
	
@route("/Login")
def login1():
	global login
	return htmlify("Login",login)
	
@route("/comments.html")
def comments():
	global login
	if hashcreator(request.GET["password"]) != real_password_hash:
		if request.GET["gender"] == "boy":
			login=login+"<br><br><h1>Wrong password :( Please try again, sir!</h1>"
			return htmlify("Wrong Password", login)
		elif request.GET["gender"] == "girl":
			login=login+"<br><br><h1>Wrong password :( Please try again, madam!</h1>"
			return htmlify("Wrong Password", login)
	else:
		write_comment="""
		Write your comment, please:<br><br>
		<form>
		<textarea name="comment" rows="10" cols="30" autofocus></textarea><br>
		<input type="submit" name="commentsubmit" value="Post">
		</form>
		"""
		return htmlify("Your Lovely Comments",write_comment)
		



#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()

