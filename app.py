from flask import Flask, render_template, url_for, request, redirect
from FinalModel import *
import warnings
warnings.filterwarnings("ignore")



app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/results', methods = ['POST'])
def upload_file():
	if request.method == 'POST':
		img = request.files['userfile']


		img.save("static/img/"+img.filename)

	
		caption = caption_this_image("static/img/"+img.filename)



		
		result_dic = {
			'image' : "static/img/" + img.filename,
			'description' : caption
		}
	return render_template('results.html', results = result_dic)



if __name__ == '__main__':
	app.run(threaded=False)
