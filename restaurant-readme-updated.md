# Restaurant Success Prediction App 🍽️

A machine learning application that predicts restaurant success based on various features using a Decision Tree model. The application is containerized using Docker and provides an interactive web interface built with Streamlit.

## 🚀 Quick Start

You have two options to access the application:

### Option 1: Web Browser (No Installation Required)
Visit the live application at:
```
https://restaurantsuccess-bysabryfarraj.streamlit.app/
```
This option requires no setup - just click and use!

### Option 2: Run using Docker

If you prefer to run the application locally:

```bash
# Pull the image from Docker Hub
docker pull sabryfarraj/restaurant-success-predictor

# Run the container
docker run -p 8501:8501 sabryfarraj/restaurant-success-predictor:latest
```

After running these commands, open your browser and visit:
```
http://localhost:8501
```

## 🛠️ Project Structure
```
Restaurant_Success_prediction/
├── Restaurant_Success.py        # Main Streamlit application
├── Restaurant_Success.ipynb     # Model development notebook
├── decision_tree_pipeline.pkl   # Trained model
├── min_max_values.pkl          # Feature scaling values
├── unique_values.pkl           # Categorical features mapping
├── requirements.txt            # Python dependencies
└── zomato.rar                 # Dataset
```

## 📋 Prerequisites
For Docker option only:
- Docker installed on your machine ([Install Docker](https://docs.docker.com/get-docker/))

## 🔧 Local Development

If you want to build the Docker image locally:

```bash
# Clone the repository
git clone https://github.com/sabryfarraj/Restaurant_Success_prediction.git

# Navigate to project directory
cd Restaurant_Success_prediction

# Build Docker image
docker build -t restaurant-success-predictor .

# Run container
docker run -p 8501:8501 restaurant-success-predictor
```

## 📊 Features
- Predicts restaurant success probability
- Interactive web interface
- Real-time predictions
- Available as web application and containerized application
- Pre-trained machine learning model

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Authors
- Sabry Farraj

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## 🙏 Acknowledgments
- Dataset provided by Zomato
- Built with Streamlit and scikit-learn
- Hosted on Streamlit Cloud
