# Car-Price Prediction

This repository consists of files required for end to end implementation and deployment of Machine Learning Car Price Prediction web application created with Pycharm using streamlit and deployed on the Heroku platform.

## Project Link
https://car-amount.herokuapp.com/
![2022-07-26](https://user-images.githubusercontent.com/76897778/181051660-75d48320-7174-4114-8d08-dd488260da60.png)


## Aim
This project aims to predict the Price of an used Car by taking it's Company name, it's Model name, Year of Purchase, and other parameters.
![2022-07-26](https://user-images.githubusercontent.com/76897778/181051714-ae95451d-42f7-49bd-8acf-0462ff78c32c.png)


## How to Use?
- Clone the repository
- Install the required packages in "requirements.txt" file

Some packages are:

- numpy
- pandas
- scikit-learn
- streamlit
- Run the "main.py" file And you are good to go.

# Description

## What this project does?
-  This project takes the parameters of an used car like: Company name, Model name, Year of Purchase, Fuel Type and Number of Kilometers it has been driven.
- It then predicts the possible price of the car. For example, the image below shows the predicted price of our Hyundai Grand i10.
 ![2022-07-26](https://user-images.githubusercontent.com/76897778/181051776-67b0c256-213b-4d20-bda0-57b2a96cfd52.png)


## How this project does?
- First of all the data was scraped from Quikr.com (https://quikr.com) Link for data:https://github.com/Vineetkumar99/car_price_prediction/blob/main/quikr_car.csv
- The data was cleaned (it was super unclean :( ) and analysed.

- Then a Linear Regression model was built on top of it which had 0.88 R2_score.

- Link for notebook: https://github.com/Vineetkumar99/car_price_prediction/blob/main/Car%20Price%20Predictor.ipynb

- This project was given the form of an website built on pycharm using streamlit where we used the Linear Regression model to perform predictions.
