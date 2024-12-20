from flask import Flask, request, render_template
import main

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Home page with a form to input site URL and Google Sheet name."""
    if request.method == 'POST':
        site_url = request.form['site_url']
        sheet_name = request.form['sheet_name']
        try:
            urls = main.main(site_url, sheet_name)
            return render_template('results.html', urls=urls, sheet_name=sheet_name)
        except Exception as e:
            return render_template('error.html', error_message=str(e))
    return render_template('index.html')

@app.route('/results')
def results():
    """Results page (optional, as results are handled in POST response)."""
    return render_template('results.html', urls=[])

if __name__ == '__main__':
    app.run(debug=True)
