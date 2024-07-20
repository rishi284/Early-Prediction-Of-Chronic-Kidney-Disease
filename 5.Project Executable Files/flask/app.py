from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the Prediction Form Page
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        form_data = request.form.to_dict()
        # Mock prediction logic
        prediction = mock_predict(form_data)
        return render_template('result.html', prediction=prediction)
    return render_template('index.html')

# Mock prediction function
def mock_predict(data):
    # Implement your prediction logic here
    # This is a placeholder logic for demonstration
    if int(data['age']) > 50:
        return 0  # Kidney Disease
    else:
        return 1  # Not Kidney Disease

if __name__ == '__main__':
    app.run(debug=True)
