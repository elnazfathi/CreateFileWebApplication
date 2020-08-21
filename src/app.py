
from flask import Flask, render_template, request
from datetime import datetime

#from jinja2 import

app = Flask(__name__) #'__main__'

#app.config.from_object(__name__)
#app.config['SECRET_KEY'] = '123455677889900'

@app.route('/') #inut here is empty end point. It means the last character of this example URL: www.mysite.com/api/
def home_method():#define the method that will execute when you get to above access point in the browser
    return render_template('submit.html')

@app.route('/submit', methods = ['POST'])
def submit_form():
    input_id = request.form['input_id']
    input_number = request.form['input_number']
    input_comment = request.form['input_comment']
    input_start_date = request.form['input_start_date']
    input_end_date = request.form['input_end_date']
    filePath = 'new_file_{}_{}_{}.txt'.format(input_id, input_number, datetime.now().strftime("%Y-%m-%d %H-%M"))
    with open(filePath, 'a') as f:
        f.write('{}|{}|{}|{}|{}'.format(input_id, input_number, input_comment, input_start_date, input_end_date))
    return render_template('message.html')



#new_file_$ID_$NUMBER_$sysdate.txt
#And following content, WITHOUT HEADER:
#ID|NUMBER|COMMENT|START_DATE|END_DATE

if __name__ == '__main__': #means if we are running the app and expecting it to initialize and start from zero then we will run the app.
                           # and if the app is running as part of a separate process then we will not run the app and leave it for other process to run the app.
    app.run(port= 5000)



'''
from flask import Flask, request, render_template,jsonify
app = Flask(__name__)



def submit_form(id, number):
    with open('/Users/elnazfathi/Documents/new_file_${}_${}_$inserrrrtdate.txt'.format(id, number), 'a') as f:
        f.write('{}|{}'.format(id, number))


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit/', methods=['GET','POST'])
def my_form_post():
    input_id = request.form['id']
    #word = request.args.get('id')
    input_number = request.form['number']
    #combine = do_something(input_id,input_number)
    #result = {
    #    "output": combine
    #}
    #result = {str(key): value for key, value in result.items()}
    #return jsonify(result=result)
    submit_form(input_id, input_number)
    #return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

'''

