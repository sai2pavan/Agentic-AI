import logging
import os
from datetime import datetime

from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#creating a log file to store the logging records
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir,f"ml_pipeline_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    handlers = [
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

logging.info("Starting the ML pipeline")

try:
    data = load_breast_cancer()
    x,y = data.data, data.target #x is the feature and y is the target variable
    logging.debug(f"features names: {data.feature_names}")
    logging.info(f"Data loaded successfully: Feature shape: {x.shape}, Target shape: {y.shape}")
except Exception as e:
    logging.critical(f"Error loading data: {e}")

try:
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
    logging.info(f"Data split into train and test sets: Train shape: {x_train.shape}, Test shape: {x_test.shape}")
except Exception as e:
    logging.critical(f"Error splitting data: {e}")

try:
    model = LogisticRegression(max_iter=10000)
    model.fit(x_train,y_train)
    logging.info("Model training completed successfully")
except Exception as e:
    logging.critical(f"Error training model: {e}")
