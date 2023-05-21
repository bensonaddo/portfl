from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

# Handles all requests for the root page
@app.route('/')
def home():
    return render_template('./index.html')

# @app.route('/<username>')
# def print_name(username=None):
#     return render_template('./index.html', name=username)

# This allows our pages to render dynamically
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    # The following function receives a 
    # distionary object in the form of data
    # retrieve items from the data and 
    # Writes or appends those items to database.txt file.
    with open('database.txt', mode='a') as database_txt:
      name = data['contact_name']
      email = data['contact_email']
      message = data['contact_message']
      file = database_txt.write(f'\n{name},{email},{message}')
      return file
    
def write_to_csv(data):
    with open('database.csv', mode='a', newline="") as database_csv:
        name = data['contact_name']
        email = data['contact_email']
        message = data['contact_message']
        # page_header = ['Name', 'Email', 'Message']
        # csv_writter = csv.DictWriter(database_csv,fieldnames=page_header)
        # csv_writter.writeheader()
        # csv_writter.writerow({'Name': name, 'Email': email, 'Message': message})
        csv_writter = csv.writer(database_csv,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) #Use no quotes characters, seperate data the delimiter
        #Write to data using the format specified in the csv file
        csv_writter.writerow([name, email, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # The Code below uses the post request 
    # data from the submit form
    # writes the data to a database.txt file
    # Redirects the user to a Thank you page
    if request.method == 'POST':
        try:
            data = request.form.to_dict() #Converts data into dictionary
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong, Try again'

if __name__ == '__main__':
    app.run()