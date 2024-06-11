import joblib
from flask import Flask, render_template, request, jsonify

def make_prediction(chkacct, duration, balanceInSavings, history, creditAmount, purposeofcredit, age, install_rate, RealEstate):
    try:
        model = joblib.load('randomForest.joblib')
        sc = joblib.load('scaler.joblib')
    except FileNotFoundError:
        print("Model files not found. Ensure 'randomForest.joblib' and 'scaler.joblib' are in the correct directory.")
        return None
    
    try:
        inputAttri = [[chkacct, duration, balanceInSavings, history, creditAmount, purposeofcredit, age, install_rate, RealEstate]]
        inputAttri = sc.transform(inputAttri)
        prediction = model.predict(inputAttri)
        if prediction[0] == 1:
            return 'GOOD'
        else:
            return 'BAD'
    except Exception as e:
        print("An error occurred:", e)
        return None

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        data = request.get_json()
        chkacct = int(data['chkacct'])
        duration = int(data['duration'])
        balanceInSavings = int(data['balanceInSavings'])
        history = int(data['history'])
        creditAmount = int(data['creditAmount'])
        purposeofcredit = int(data['purposeofcredit'])
        age = int(data['age'])
        install_rate = int(data['install_rate'])
        RealEstate = int(data['RealEstate'])
        
        # Call your prediction function
        result = make_prediction(chkacct, duration, balanceInSavings, history, creditAmount, purposeofcredit, age, install_rate, RealEstate)
        
        return jsonify({'prediction': result})
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run()

