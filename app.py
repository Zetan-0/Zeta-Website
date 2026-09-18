from flask import Flask, render_template, request

app = Flask(__name__, template_folder='.')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/join')
def join_page():
    return render_template('join.html')


@app.route('/submit', methods=['POST'])
def handle_form():

    student_name = request.form.get('name')
    student_email= request.form.get('email')
    student_year= request.form.get('year')
    student_track= request.form.get('track')



    print(f"NEW RECRUIT: {student_name} ({student_email}) - {student_year}, focusing on {student_track}")

    return f"<h3>Thank You, {student_name}! Your interest form has been sent to the Zeta Psi Alpha committee.</h3><br>a< href='/'>Return Home</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9095, debug=True)