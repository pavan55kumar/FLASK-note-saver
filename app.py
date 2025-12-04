from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Store notes as a list of dictionaries
notes = []

@app.route('/')
def home():
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    title = request.form.get('title')
    description = request.form.get('description')
    if title and description:
        notes.append({'title': title, 'description': description})
    return redirect('/')

@app.route('/clear')
def clear_notes():
    notes.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
