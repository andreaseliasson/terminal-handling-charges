# Anomaly/Outlier Detection for Terminal Handling Charges

This application checks for outliers in a sample of terminal handling charges using the value property (a floating point number). The check is made on a per-country basis and all the values have been normalized to USD. Given that we are dealing with an unlabeled data set and that the distribution is not perfectly normally distributed, we are using a percentile based and a median absolute deviation based algorithm to detect potential outliers. Somewhat naively, we are using the same algorithm to check if a new observation is an outlier or not. This works for now, but another approach using the likelihood function and the probability density function together with cross-validation is under development (need a little bit more time on this one).

## How to run the application

## Before we start
1.  Make sure you put the `sample_data.json` inside the dir `./backend/data`. Note that this dir does not exist after cloning.
2.  Make sure you have `python3` and `npm` installed

### How to run the Backend
1.  `cd backend`
2.  `python3 -m pip install -r requirements.txt` or however you prefer to pip install using a specific Python version
3.  `cd src`
4.  `python3 main.py` (This will the start the local flask server)

### How to run the Frontend
1.  `cd frontend`
2.  `npm install`
3.  `npm start`

### Example imgages
![Alt text](/../graph-images/backend/img/cn_kde.png?raw=true "Optional Title")
