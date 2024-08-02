# Outlier Detection Web Application


#Overview
This project is a web-based application designed to detect outliers in datasets using an Isolation Forest model. The application allows users to upload datasets, detect outliers, and view results through a user-friendly interface.

#Technologies/Libraries Used
- **Python:** Programming language used for model implementation and data processing.
- **Scikit-learn:** Library used for the Isolation Forest algorithm.
- **Pandas:** Data manipulation and analysis library.
- **Joblib:** Used for saving and loading the trained model.
- **HTML/CSS:** For the frontend design and layout.
- **JavaScript:** For interactive elements in the web pages.

#Installation
**1. Clone the Repository:** git clone [repository-url]
**2. Set Up Python Environment:** Make sure you have Python installed. If not, download and install Python from the (https://www.python.org/downloads/) .<br>
**3. Install Required Libraries:** pip install pandas scikit-learn joblib
**4. Prepare the Model:** Run the model_training.py script to train and save the Isolation Forest model. 
     python model_training.py

#Usage
**1. Start the Flask Application:** python app.py
**2. Interact with the Web Application
- Home Page (index.html): Provides an overview and options to upload datasets and detect outliers.
- Detect Outliers Page (detect.html): Allows users to upload a dataset, process it, and detect outliers.
- About Model Page (about.html): Provides detailed information about the outlier detection model and its implementation.

#How It Works
- **Data Upload:** Users upload a CSV file containing the dataset to be analyzed.
- **Model Application:** The Isolation Forest model is used to detect outliers in the uploaded data.
- **Results Display:** The number of detected outliers is displayed to the user.

#File Structure
- **app.py:** Flask application that serves the web pages and handles user interactions.
- **index.html:** Home page of the application.
- **detect.html:** Page for detecting outliers.
- **about.html:** Page with information about the outlier detection model.
- **model_training.py:** Script for training and saving the Isolation Forest model.

#Notes
- Ensure that isolation_forest_model.joblib is located in the same directory as app.py for model loading.
- The application uses a fixed background image (images.webp) for styling. Make sure the image is located in the correct directory.

#For Any Inquiries or Feedback
For any inquiries or feedback, please contact 
- Eisha Haroon: [eishaharoon4@gmail.com](mailto:eishaharoon4@gmail.com)
