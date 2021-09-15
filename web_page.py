from flask import Flask
import os
import shutil
from flask import Flask, render_template, Response, request, redirect, url_for, send_file,send_from_directory
import run
import os
app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = 'input'
PATH = '/Users/kataria/Projects/python/MiDaS-master/'

@app.route('/success', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        file1 = request.files['file1']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file1.save(path)
        return render_template("index.html", name=file1.filename, check=True)


@app.route('/process', methods=['GET', 'POST'])
def process():
    option = request.form['options']
    name = request.form['file']
    print(option)
    value = run.run('input', 'output', None, option, True)
    return render_template("/complete.html", name=value,file= name, check=True)


@app.route('/download1',methods=['POST'])
def downloadFile1 ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = request.form['file']
    path = path[:path.index('.')]
    path = path+'.pfm'
    print(path)
    return send_from_directory(PATH+'output/', path)

@app.route('/download2',methods=['POST'])
def downloadFile2():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = request.form['file']
    path = path[:path.index('.')]
    path = path+'.png'
    return send_from_directory(PATH+'output/', path)

@app.route('/delete',methods=['POST'])
def delete():
    shutil.rmtree(PATH + 'input')
    shutil.rmtree(PATH + 'output')
    os.mkdir(PATH + 'input')
    os.mkdir(PATH + 'output')
    return render_template('index.html', check=False)

@app.route('/')
def index():
    return render_template('index.html', check=False)


if __name__ == '__main__':
    app.run(debug=True)
