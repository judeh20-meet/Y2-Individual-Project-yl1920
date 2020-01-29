from databases import add_picture,add_picture,edit_picture,delete_picture,return_all_pictures,query_by_id
from flask import Flask, request, redirect, render_template,url_for
from flask import session as login_session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route('/', methods =["GET", "POST"])
def home():
	if request.method == "GET":
		return render_template('index.html')
	else:
		if request.form['adminpassword'] == "judeharaj":
			login_session['password'] = request.form['adminpassword']
			return redirect(url_for('admin'))
		else:
			msg = "wrong password! try again!"
			return render_template('index.html', msg = msg)


@app.route('/videogame', methods =["GET", "POST"])
def Videogame():
	if request.method == "POST":

		photoname = request.form['name']
		photodescription = request.form['description']
		photolink = request.form['photo_link']
		add_picture(photoname,photodescription,photolink)
		
		return render_template('admin.html', pictures = return_all_pictures())
	else:
		return render_template('elements.html', pictures = return_all_pictures())





@app.route('/admin', methods =["GET", "POST"])
def admin():
	if request.method == "GET":
		if 'password' in login_session:
			if login_session['password'] == "judeharaj":
				return render_template('admin.html', pictures = return_all_pictures())
			else:
				pass
		else:
			return redirect(url_for('home'))
	else:

		return render_template('admin.html', pictures = return_all_pictures())

@app.route('/adminedit', methods =["GET", "POST"])
def adminedit():
	if request.method == "GET":
		if 'password' in login_session:
			if login_session['password'] == "judeharaj":
				return render_template('adminedit.html', pictures = return_all_pictures())
			else:
				pass
		else:
			return redirect(url_for('home'))
	else:

		photoID_foredit = request.form['photoID_foredit']
		name_foredit = request.form['name_foredit']
		description_foredit = request.form['description_foredit']
		photo_link_foredit = request.form['photo_link_foredit']
		edit_picture(photoID_foredit, name_foredit, description_foredit ,photo_link_foredit)
		
		return render_template('adminedit.html', pictures = return_all_pictures())

		
@app.route('/logout')
def logout():
	login_session.clear()
	return redirect(url_for('home'))

@app.route('/delete/<int:ID>')
def clever_function(ID):
	delete_picture(ID)
	return redirect(url_for('Videogame'))

if __name__ == '__main__':
	app.run(debug=True)