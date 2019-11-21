# Project-Fitbit

This is a Readme for the fitbit project by JaVale and Klay.

Background: The purpose of the this project was to examine data extracted from multiple CSVs located on a thumb drive.

ADMINISTRATIVE NOTES:

Prophet Documentation:

Quick overview and installation - https://facebook.github.io/prophet/ In depth documentation - https://peerj.com/preprints/3190.pdf

Prophet is an open source software released by facebooks Core Data Science Team. We implemented it in Python. It is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects.

The following install are necessary for the ability to replicate the files in the repository:

conda install pystan



Data Dictionary
Daily Activity
Description​: Contains daily totals for steps, intensity, distance, and calories.
Data Dictionary (.csv files)
 Day Totals
Data Header
ActivityDate
TotalSteps
TotalDistance TrackerDistance LoggedActivitiesDistance VeryActiveDistance ModeratelyActiveDistance LightActiveDistance SedentaryActiveDistance VeryActiveMinutes FairlyActiveMinutes LightlyActiveMinutes SedentaryMinutes Calories
Floors CaloriesBMR
MarginalCalories RestingHeartRate
Data Type
date integer integer integer integer integer integer integer integer integer integer integer integer integer
integer integer
integer integer
Data Description
Date value in mm/dd/yyyy format.
Total number of steps taken.
Total kilometers tracked.
Total kilometers tracked by Fitbit device.
Total kilometers from logged activities. Kilometers travelled during very active activity. Kilometers travelled during moderate activity. Kilometers travelled during light activity. Kilometers travelled during sedentary activity. Total minutes spent in very active activity. Total minutes spent in moderate activity.
Total minutes spent in light activity.
Total minutes spent in sedentary activity.
Total estimated energy expenditure (in kilocalories).
Total number of floors climbed.
Total energy expenditure from basal metabolic rate
Total marginal estimated energy expenditure (in kilocalories)
                                                                                                               Resting heart rate value.
