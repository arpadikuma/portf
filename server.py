from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
# print(__name__)

@app.route('/')
def my_home():
    return render_template("./index.html")

@app.route('/<string:page_name>')
def show_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open("./db.txt", "a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email}|||{subject}|||{message}")

def write_to_csv(data):
    with open("./db.csv", "a", newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",", quotechar="\"", quoting=csv.QUOTE_ALL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        try:
            data =  request.form.to_dict()
            write_to_csv(data)
            return redirect("./thankyou.html")
        except:
            return 'data could not be saved! ⚠️'
    else:
        return "Something went wrong, try again 😓"

# @app.route('/submit_form', methods=['POST', 'GET'])
# def login():
#     if request.method == "POST":
#         data =  request.form.to_dict()
#         mail_address = data["email"]
#         print(data)
#         return redirect("./thankyou.html", mail_address=mail_address)
#     else:
#         return "Something went wrong, try again 😓"



# @app.route('/favicon.ico')
# def favicon():
#     return render_template("./favicon.ico")

# @app.route('/blog')
# def blog():
#     return "<h2>bloOog</h2>"

# @app.route('/<username>')
# def hello_user(username=None):
#     return render_template("./index.html", name=username)


# @app.route('/<username>/<int:post_id>')
# def hello_user_id(username=None, post_id=None):
#     return render_template("./index.html", name=username, post_id=post_id)
