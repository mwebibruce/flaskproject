# import main Flask class and request object
from flask import Flask, request

# create the Flask app
app = Flask(__name__)

@app.route('/query-example')
def query_example():
    return 'Query String Example'

@app.route('/form-example')
def form_example():
    return 'Form Data Example'

@app.route('/json-example')
def json_example():
    return 'JSON Object Example'
# allow both GET and POST requests
@app.route('/form-example2', methods=['GET', 'POST'])
def form_example2():
    return '''
              <form method="POST">
                  <div><label>Language: <input type="text" name="language"></label></div>
                  <div><label>Framework: <input type="text" name="framework"></label></div>
                  <input type="submit" value="Submit">
              </form>'''
# allow both GET and POST requests
@app.route('/form-example3', methods=['GET', 'POST'])
def form_example3():
    # handle the POST request
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form.get('framework')
        return '''
                  <h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>Language: <input type="text" name="language"></label></div>
               <div><label>Framework: <input type="text" name="framework"></label></div>
               <input type="submit" value="Submit">
           </form>'''
# GET requests will be blocked
@app.route('/json-example2', methods=['POST'])
def json_example2():
    request_data = request.get_json()

    language = request_data['language']
    framework = request_data['framework']

    # two keys are needed because of the nested object
    python_version = request_data['version_info']['python']

    # an index is needed because of the array
    example = request_data['examples'][0]

    boolean_test = request_data['boolean_test']

    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5010)
    
    