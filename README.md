# RCNN-code

Object detection and counting of tomatoes for further yield estimation by analyzing Unmanned Aerial Vehicles (UAVs) imagery acquired using Low Altitude Remote Sensing (LARS) 
1. Implemented R-CNN model for estimation of tomatoes in a given tomato farm. 
2. The model is based on one of the state-of-the-art CNN-based object detection and classification.
3. Proposed enhancements over original algorithm :
    - Improved accuracy by selecting the hyper parameters from the epoch that has least loss during training
    - Refined each bounding box using regression.

Sample frame extracted from the video acquired:
![fieldimage](https://user-images.githubusercontent.com/60587239/81495671-feb50700-927f-11ea-8fab-0cd903c59247.jpg)

Using labelImg, created the ground truth labels for training(takes a LOT of time):

    
![labelimg](https://user-images.githubusercontent.com/60587239/84558704-c41d0f00-ad02-11ea-9a62-59b7cc587fc6.png)

