## Create a simple flask application

from flask import Flask,render_template,request,redirect,url_for

## create the flask app

app=Flask(__name__)

@app.route('/')  # @pp.route is a function available in Flask which is used to create the url for the function welcome while / denotes the url
def home():  # We can reach the function welcome through the url, i.e., /
    return "<h2>Hello, World!</h2>"  # This is not a good practice

@app.route('/welcome') # /welcome is the url
def welcome():
    return "Welcome to the Flask Tutorials"

@app.route('/index')  # /index is the url
def index():
    return render_template('index.html') # render_template redirects the url to html page

@app.route('/success/<int:score>') # /success is the url while <int:score> is the parameter
def success(score):
    return "The person has passed and the score is "+str(score)

@app.route('/fail/<int:score>')  # /fail is the url
def fail(score):
    return "The person has failed and the score is "+str(score)


@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks=(maths+science+history)/3
        result="" 
        if average_marks>=50:
            result="success"
        else:
            result="fail"

        #return redirect(url_for(result,score=average_marks))


        return render_template('result.html',results=average_marks)
    


if __name__=='__main__':
    app.run(debug=True)


# GET method: This is used to send data through the url to another system
# POST method: This is used to send data through the body to another system
# Debug = True is used when you want make some changes in the file
# Debud = True is used in the development environment not in production environment