# Graduation_Project
The Data Science team follows the same approach done by this research paper:
https://link.springer.com/article/10.1007/s00417-018-04224-8

According to it, we path through this pipeline:
1-	Data Gathering 
2-	Data Preprocessing 
3-	Model Building 
4-	Model Training
5-	Model Evaluation
6-	Model Deployment 

1- Data Gathering:
-	We work on a public dataset downloaded from Kaggle: https://www.kaggle.com/datasets/paultimothymooney/kermany2018
-	The dataset contains 4 folders of different OCT images.
-	3 folders for 3 different retinal diseases and the last for the normal case.
-	The code below visualizes a sample of the dataset:
![image](https://github.com/mohamedelsharkawy-coder/Graduation_Project/assets/62524279/dd9a409c-838f-4f36-b025-c757e5e91629)
Output:
![image](https://github.com/mohamedelsharkawy-coder/Graduation_Project/assets/62524279/08c74d38-f2a7-4ea8-84e0-ecf116fcb48b)

2- Data Preprocessing:
-	The code below describes the data preprocessing stage. We choose 83484 images as training data and 1000 images as test data. We collect images into batches of 32 images size. In each batch, we make some transformations like resizing to (256, 256) and normalization of pixels’ values.
![image](https://github.com/mohamedelsharkawy-coder/Graduation_Project/assets/62524279/8fbfa262-0762-48b9-b3e4-02ad7e0ab2e0)

3- Model Building:
-	The code below describes the model-building stage. We add our built layers to the vgg16 architecture and use the transfer learning approach of the ImageNet pre-trained weights to build our final architecture.
![image](https://github.com/mohamedelsharkawy-coder/Graduation_Project/assets/62524279/77953964-e762-4c43-9442-cc518ac76335)

Final Architecture:

![image](https://github.com/mohamedelsharkawy-coder/Graduation_Project/assets/62524279/7deab292-b29a-4c86-b043-0ca3fa93cfdc)

4- Model Training:
-	The code below describes the model-training stage. We set up our hyperparameters and train our model for 30 epochs.
![image](https://github.com/mohamedelsharkawy-coder/Graduation_Project/assets/62524279/2cafc3ce-f2a6-46fc-a01a-35132bdf2593)

5- Model evaluation:
-	The code below describes the model-evaluation stage. We calculate the confusion matrix and use different metrics to evaluate the model.
![image](https://github.com/mohamedelsharkawy-coder/Graduation_Project/assets/62524279/fbac13c5-4e0d-4cbc-beff-5c6940e53cf3)

Confusion Matrix:
![image](https://github.com/mohamedelsharkawy-coder/Graduation_Project/assets/62524279/0468d649-0e7f-42ef-88b9-151c36e0a938)

6- Model deployment:
-	The code below describes the model-deployment stage. We build a function that describes the prediction process by getting the image as input in its parameter, making some process on it, loading the model, getting the prediction, and returning it as a JSON response. Finally, this function is used to build an API and complete the model-deployment stage.
![image](https://github.com/mohamedelsharkawy-coder/Graduation_Project/assets/62524279/2c56e9a2-9903-4811-8452-c274dff447c4)










