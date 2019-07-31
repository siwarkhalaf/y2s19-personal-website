
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template(
    	"prsonalWeb.html")

@app.route('/aboutme')
def about_me():
	return render_template(
		"aboutme.html")

@app.route('/gallery')
def gallery():
	return render_template(
		"gallery.html")

if __name__ == '__main__':
	app.run(debug=True)
