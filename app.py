from flask import Flask, render_template, request
import subprocess

app = Flask(__name__, template_folder='./templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        stock_ticker = request.form['stock_ticker']
        period_type = request.form['period_type']
        statement_type = request.form['statement_type']
        target_currency = request.form['target_currency']
        
        # Run the extract_data.py script as a subprocess
        subprocess.run(['python', 'extract_data.py', stock_ticker, period_type, statement_type, target_currency])
        
        return 'Data extraction process initiated.'
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)