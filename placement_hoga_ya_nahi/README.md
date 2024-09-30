Disclaimer: ```This dataset is hypothetical and does not reflect real-life scenarios. For example, having a 0 IQ or 0 CGPA is unrealistic and would not result in job placement. Please focus on the methodology rather than the outcomes 🥲.```

Screenshots:

![Screenshot 2024-09-29 220047](https://github.com/user-attachments/assets/467f91af-15c0-4c13-b6d3-294b115282ec)

----------------------------------------------------

![Screenshot 2024-09-29 215722](https://github.com/user-attachments/assets/386cc895-da5d-41e8-b5f0-334617cdd777)

----------------------------------------------------

![Screenshot 2024-09-29 215742](https://github.com/user-attachments/assets/f732cef2-51e7-48b3-94d7-6342357c904e)



<h4> Purpose of this project: </h4> 
The purpose of this project was to create a predictive model that can accurately(🥲) predict the likelihood of job placement.


### Flow of this project

1. Dataset: Hypothetical dataset of 50 students, asked Gemini to make one.

2. Dropped a column named ```Student ID```.

3. Used ```Label Encoder``` on dependent(y) feature/column i.e. ```Placement```.

4. Applied ```Standardization``` on ```CGPA``` and ```IQ```.

5. Split the dataset into training and testing dataset using ```train_test_split``` .

6. Applied ```k-Nearest Neighbor``` & ```Logistic Regression``` algorithms on training dataset.

7. Used testing dataset to ```predict``` the outcome using both the algorithms.

8. Calculated accuracy using ```accuracy_score```  which was ```0.9``` in both the cases.

9. Exported both the models, ```kNN Model``` as ```knn_model.pkl``` and ```Logistic Regression Model``` as ```logistic_model.pkl``` using ```pickle```.

10. Used these models in ```app.py``` to integrate it into the UI which was made using ```streamlit```.
