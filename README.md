# Real-Time Stock Price Prediction System

This repository presents a comprehensive real-time stock price prediction system that combines Django, Docker, Jenkins, and OpenShift to deliver end-to-end capabilities for collecting stock data, training prediction models, and presenting predictions through a user-friendly web interface.

## Project Overview

The main goal of this project is to showcase a practical implementation of a real-time stock price prediction system. The system's architecture is designed to highlight the integration of various technologies and tools. It enables users to interact with a web application to receive predictions for stock prices based on historical and current data.

## Project Structure

The repository is structured into several distinct components, each serving a specific purpose within the system.

### Data Collection and Preprocessing

The `data` directory contains scripts responsible for collecting stock data from the Yahoo Finance API. The collected data is then preprocessed to format and organize it for further use. The preprocessing step involves segregating the data into historical data (older than 30 days) and current data (within the last 30 days). The preprocessed data is stored in a designated folder.

### Model Training and Update

The `models` section is a key element of the project. It includes scripts and files related to model training and updating. The process begins with the `model_training` script, which trains an initial predictive model using the historical data. Following this, the `model_update` script refines the model using a combination of historical and current data. To evaluate model performance, the `model_evaluation` script assesses both models against newly acquired real-time data. If the updated model outperforms the initial model, it replaces the latter. This updating process takes place on an hourly basis following data retrieval.

### Web Application

The `stock_predict_webapp` directory houses a Django application that serves as the front-end of the system. The web application enables users to input a desired time and subsequently displays predicted stock prices for the top 10 stocks using the trained models. The seamless integration of the web app with the predictive models showcases the practicality of the developed system.

### Dockerization

The project employs Docker to encapsulate various components. Three distinct Dockerfiles are provided to cater to different aspects of the project:

1. `data`: This Dockerfile facilitates the collection and preprocessing of data. It runs a combined script that collects data using the Yahoo Finance API and performs necessary preprocessing steps before storing the prepared data in a shared volume.
2. `model`: This Dockerfile orchestrates the training, evaluation, and updating of predictive models. The script within this container leverages data from the shared volume to train and evaluate the models, subsequently storing the trained models back into the shared volume.
3. `webapp`: The Dockerfile dedicated to the web application handles the deployment of the front-end interface. It interacts with the saved models in the shared volume to generate predictions based on user input.

### OpenShift Deployment

For streamlined deployment, the project leverages OpenShift. The `openshift` directory encompasses configuration files that are essential for deploying the project's components on an OpenShift cluster. Within this directory, two deployment files are present:

1. `deployment-model`: This configuration file sequences the execution of the data processing and model training Docker images. It manages networking connections, the shared volume, and ensures a minimum of one replica is actively running.
2. `django-app-deployment`: The deployment configuration for the web server ensures optimal load balancing through multiple replicas, guaranteeing consistent and uninterrupted availability of the web application.

### Jenkins Integration

Jenkins plays a crucial role in facilitating continuous integration and deployment for the project. The `jenkins` directory encompasses pipeline configurations stored in the `Jenkinsfile`. These configurations define the automation processes for data processing, model training, and deployment. The pipelines can be triggered by a range of events, including specific time intervals or changes in the codebase. By integrating Jenkins, the project demonstrates the practicality of continuous integration in a real-world scenario.

## Getting Started

To get the project up and running, follow these steps:

1. Clone the repository to your local machine.
2. Create and activate a Python virtual environment using `python -m venv venv` and `source venv/bin/activate`.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Build the Docker images using the provided Dockerfiles.
5. Deploy the various components on an OpenShift cluster using the configuration files in the `openshift` directory.
6. Configure Jenkins by installing necessary plugins and setting up pipeline jobs using the provided `Jenkinsfile`.

## Notes

- Be sure to tailor configuration files (Dockerfiles, deployment configurations, Jenkinsfiles) to match your specific environment and requirements.
- You can further refine the data collection, preprocessing, and model training scripts to better align with your unique use case.

## My Workflow

1. **Data Collection**:
   - Utilized the `yfinance` library to gather stock data from the Yahoo Finance API for the top 10 popular stocks.
   - Segregated the collected data into historical and current sets.
   - Implemented data preprocessing steps to ensure data quality and consistency.

2. **Model Training**:
   - Employed the `HistGradientBoostingRegressor` algorithm for predictive modeling.
   - Saved trained models in the `models/saved_models` directory.
   - Divided the model training process into three scripts:
     - `model_training`: Initial model training with historical data (executed if no trained model exists), saving the trained model.
     - `model_update`: Updated the model using a combination of historical and current data, saving the updated model.
     - `model_evaluation`: Evaluated both trained and updated models against real-time data updates. Replaced the trained model with the updated model if the latter performed better. This process occurred hourly after new data retrieval.

3. **Web Application**:
   - Leveraged the Django framework to develop a user-friendly web application.
   - Enabled users to input a desired time and view predicted stock prices for the top 10 stocks.
   - Integrated the trained models into the web application to provide real-time predictions.

4. **Dockerization**:
   - Created dedicated Dockerfiles for three components:
     1. Data collection and processing.
     2. Model training, evaluation, and updating.
     3. Web application deployment.
   - Each Dockerfile encapsulated specific functionality, promoting modularity and portability.

5. **OpenShift Cluster**:
   - Set up a local OpenShift cluster using the CodeReady Containers (CRC) tool.
   - Implemented two distinct deployment files:
     1. `deployment-model`: Orchestrated sequential execution of data processing and model training Docker images, managed networking, shared volumes, and ensured minimum replica availability.
     2. `django-app-deployment`: Orchestrated web server deployment, load balancing through multiple replicas, and ensured continuous application availability.

6. **Jenkins Integration**:
   - Configured a Jenkins instance on an Azure virtual machine.
   - Installed recommended plugins, including the OpenShift plugin, to facilitate seamless integration.
   - Defined a `Jenkinsfile` to automate the deployment-model pipeline, which ran on an hourly basis, showcasing the power of continuous integration and deployment.

The comprehensive project workflow highlighted the synergy between diverse technologies and tools, ultimately resulting in a robust real-time stock price prediction system. The documentation, configuration files, and pipelines provided a clear roadmap for implementing similar systems in real-world scenarios.