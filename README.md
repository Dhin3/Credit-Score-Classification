# Credit Score Classification App

This is a web application that predicts the credit score classification based on user input. The application is built using Flask for the backend and AngularJS for handling the frontend interactions.

## Features

- Form for user input regarding various financial and personal details.
- Prediction of credit score classification using a pre-trained model.
- Display of the prediction on the same page without refreshing.
- Clear button to reset the form fields.

## Technologies Used

- **Backend**: Flask
- **Frontend**: AngularJS
- **Styling**: CSS 

## Backend (Flask)

- **app.py**: The main Flask application file handling form submission and prediction.

## Frontend (AngularJS)

- **form.html**: The HTML file containing the form and AngularJS code to handle form submission and display of the result.

## Project Structure

```plaintext
.
├── static
│   └── wallpaperflare.com_wallpaper.jpg
├── templates
│   └── form.html
├── app.py
├── randomForest.joblib
├── scaler.joblib
├── requirements.txt
└── README.md

```

## Form Fields

- **Checking Account**: Dropdown with options for different account statuses.
- **Balance in Savings A/C**: Dropdown for balance ranges in savings.
- **History**: Dropdown for credit history status.
- **Purpose of Credit**: Dropdown for different purposes of credit.
- **Real Estate**: Dropdown for real estate ownership status.
- **Duration**: Number input for the duration in months.
- **Credit Amount**: Number input for the credit amount.
- **Age**: Number input for the age.
- **Installment Rate**: Number input for the installment rate.

## Usage

1. Fill out the form with the required details.
2. Click the Submit button to get the prediction.
3. The prediction will be displayed below the form.
4. Click the Clear button to reset the form.

## Setup Instructions

1. **Clone the repository**:

    ```sh
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a virtual environment and activate it**:

    ```sh
    Set-ExecutionPolicy RemoteSigned -Scope Process
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```sh
    pip install -r .\requirments.txt
    ```

4. **Run the Flask app**:

    ```sh
    python app.py
    ```

5. **Open the application in your browser**:
    ```sh
    Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
    ```
