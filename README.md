# Anomaly/Outlier Detection for Terminal Handling Charges :mag_right: :flashlight:

This application checks for outliers in a sample of terminal handling charges using the value property (a floating point number). The check is made on a per-country basis and all the values have been normalized to USD. Given that we are dealing with an unlabeled data set and that the distribution is not perfectly normally distributed, we can use a percentile based and a median absolute deviation based algorithm to detect potential outliers. Somewhat naively, we can use the same algorithm to check if a new observation is an outlier or not. This works for now, but another approach using likelihood and the probability density function together with cross-validation should be considered (need a little bit more time on this one) :simple_smile:.

## How to run the application

## Before we start
1.  Make sure you put the `sample_data.json` inside the dir `./backend/data`. Note that this dir does not exist after cloning. If you don't already have the json file it can be downloaded from [here](https://drive.google.com/file/d/0B-IfDydlbuP3MlZhLXdUTmJ0NF9XaEtNVDREVnNpaE1VN25B/view)
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

### Output images from running the comparison function inside
```
./backend/src/outlier_detection.py
```
![Alt text](/../graph-images/backend/img/cn_kde.png?raw=true "Optional Title")
![Alt text](/../graph-images/backend/img/us_kde.png?raw=true "Optional Title")
![Alt text](/../graph-images/backend/img/hk_kde.png?raw=true "Optional Title")
