# Neural Network Flask Web Application

A simple Flask web application that uses a neural network to predict the sum of two numbers.

## Project Structure
```
Pipelining_pythonApp/
├── model.py          # Neural network training logic
├── app.py            # Flask web server
├── data.csv          # Training dataset
├── requirements.txt  # Python dependencies
├── Jenkinsfile       # CI/CD pipeline configuration
└── templates/
    └── index.html    # Web form interface
```

## Setup Instructions

### Local Development
1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://127.0.0.1:5000`

### Jenkins Pipeline Setup
1. Install Jenkins and Git on your system
2. Configure GitHub credentials in Jenkins:
   - Go to Manage Jenkins → Credentials → Add Credentials
   - Kind: Username with password
   - Username: Your GitHub username
   - Password: GitHub Personal Access Token (PAT)
   - ID: github-https

3. Create a new pipeline job in Jenkins
4. Choose "Pipeline script from SCM"
5. Set Git repository URL and branch to `*/main`
6. Build the job and monitor console output

## Features
- Neural network trained on addition patterns
- Web interface for user input
- Real-time prediction display
- Jenkins CI/CD pipeline integration

## Dependencies
- Flask 2.3.3
- TensorFlow 2.13.0
- Pandas 2.0.3
- NumPy 1.24.3
