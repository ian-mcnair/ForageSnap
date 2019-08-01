<a href="Loading Page"><img src="https://github.com/ian-mcnair/ForageSnap/blob/master/newlogo.png" align="right" height="450" width="450" ></a>
# ForageSNAP
ForageSNAP is the name of our team's final project for Google's Applied Machine Learning Intensive. ForageSNAP is an application that utilizes MobileNetV2, developed by Google, in order to create a lightweight model using Keras, which is ported to Tensorflow Lite, and inserted into the java based application. 

The overall final goal of ForageSNAP is to allow people to have an easy to use app which identifies edible and not edible plants. Before that occurs, the model is first being tested to see whether it can identify harmful and harmless plants to a relative level of success. Harmless vs Harmful is much more general than edible vs non-edible, so we decided this would be a good place to start.

## Goals:
1. Create a deep learning model and application that easily tells the users if a plant is edible or not.
2. Have a complete mobile application to be published on the Google Play Store.

## TO-DO
### Data
- [x] Find data
- [x] Grab data URLs
- [x] Create ML folder structure (train, test, val) 
- [x] Download half of images directly into google drive (to be used with colab)
- [x] Download all data into drive

### Base ML Model
- [x] Create model using MobileNetV2 with simple classifiers for testing
- [x] Create model with FastAI (ResNet50+) using more data/classes
- [x] Create mobile ready model with 5+ classes
- [x] Create mobile model with all desired classes
- [x] Create webapp ready model with all desired classes

### Mobile Application
- [x] Go through TFLite tutorial and get working base image classification app
- [x] Modify app - Loading Screen
- [x] Modify app - Banner
- [x] Modify app - "drag up" information
- [x] Modify app - Notice Screen
- [x] Modify app - Simple ForageSnap Model
- [x] Modify app - More complex ForageSnap Model (30 - 50% of data)
- [x] Modify app - Final ForageSnap model (90%+ of Data)
- [x] Make mobile app more aesthetic

### Web Application
- [x] Create base Flask App + Server
- [x] Get upload image button working
- [x] Use pretrained model to predict
- [x] Upload ForageSnap webapp ready model
- [x] Make web app more aesthetic
- [ ] Deploy web app

## Current State of Mobile Application
<a href="Splash Screen"><img src="https://github.com/ian-mcnair/ForageSnap/blob/master/splashscreen.png" align="left" height="500" width="250" ></a>
<a href="Warning Screen"><img src="https://github.com/ian-mcnair/ForageSnap/blob/master/warningscreen.png" height="500" width="250" ></a>
<a href="Camera Screen"><img src="https://github.com/ian-mcnair/ForageSnap/blob/master/cameraactivity.png" align="right" height="500" width="250" ></a>
## Live Demo
<a href="Live Demo"><img src="https://github.com/ian-mcnair/ForageSnap/blob/master/live_demo.gif" align="left" height="500" width="250" ></a>
<a href="Live Demo"><img src="https://github.com/ian-mcnair/ForageSnap/blob/master/live_demo2.gif" align="right" height="500" width="250" ></a>
