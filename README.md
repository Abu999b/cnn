
### ✅ ScalpDiseaseDetection Convulational Neural Network Model

```markdown
# ScalpDiseaseDetection

A web-based deep learning application to detect hair and scalp diseases from uploaded images using a fine-tuned InceptionV3 model.

## 🚀 Features
- Upload scalp/hair images for classification
- Predicts 14 dermatological conditions
- Displays confidence score and treatment info
- JSON-based disease knowledge integration

## 📦 Tech Stack
- Python, Flask
- TensorFlow (InceptionV3 CNN Model)
- HTML/CSS + JavaScript (Frontend)
- Hosted via Render (or other platforms)

## 📁 Folder Structure


cnn/                                                                                                                                                                                  
├── model/inception_v3_finetuned_L2.h5

├── splittor.py                                                                                                                                                                                 
├── static/uploads/

├──dataset/all
                                                                                                                                                                    
├── templates/index.html                                                                                                                                                                             
├── disease_info.json                                                                                                                                                                   
├── app.py


```

```markdown

## 🧠 Model Info
- Fine-tuned InceptionV3
- Input: 150x150 RGB
- Output: 14-class softmax

### ⚙️ Setup Instructions

1. Clone the repository

2. Move into cnn/.. using >>cd cnn

3. Move into environment:
   >>python -m venv env
   >>.\env\Scripts\Activate.ps1

4. Install dependencies:   
   run >>pip install -r requirements.txt

5. Load hairdisease dataset into root directory from https://www.kaggle.com/datasets/abubakar4u900/hair-and-scalp-disease-dataset
   run >>python splittor.py
   to create train/..,test/.. and val/.. in dataset folder from all/.. folder
   
6. Train model using dataset
   run >>jupyter notebook
   ```bash
   run ...\Gaussian InceptionV3.ipynb in jupitor notebook.
   inception_v3_finetuned_L2.h5 model gets created in root folder automatically
   move inception_v3_finetuned_L2.h5 into model/..
   ```

7. Run the app:

   ```bash
   python app.py
   ```
```

```

## 🔍 Sample Conditions

* Alopecia Areata
* Acne Keloidalis
* Folliculitis Decalvans
* Trichotillomania

```
```
## 📄 License

MIT License

```

```

## 📑 Abstract

**Title:** InceptionV3 Convulational Neural Network - Deep Learning-Based Hair and Scalp Disease Detection

**Abstract:**
This project presents *ScalpDiseaseDetection*, a deep learning-powered web application designed for early detection of scalp and hair diseases. Leveraging a fine-tuned InceptionV3 convolutional neural network, the system classifies uploaded scalp images into 14 dermatological conditions, including alopecia, folliculitis, and more. The application provides instant predictions with confidence scores, coupled with condition-specific information such as symptoms, treatments, and expert advice. Designed for both patients and dermatologists, this tool serves as a scalable AI-assisted pre-diagnostic system accessible through any browser.





## 📘 Documentation:

```markdown

1. ## Introduction
      Scalp diseases are often underdiagnosed due to limited access to dermatologists, especially in rural areas.  
   This project provides an automated solution for **image-based classification** of scalp diseases using deep learning and a lightweight web interface for real-time             predictions.


2.  ## Model Architecture
   - **Base Model:** [InceptionV3](https://keras.io/api/applications/inceptionv3/) (pre-trained on ImageNet)
   - **Transfer Learning:** Removed the top layers and added custom dense layers
   - **Fine-Tuning:** Unfrozen the last few layers and retrained on a labeled scalp disease dataset

3. ## Preprocessing Pipeline
   Image inputs are standardized to ensure model compatibility:

   * 🔄 **Resize:** 150x150 pixels
   * 🎨 **Color Conversion:** RGB
   * ⚖️ **Normalization:** Pixel values scaled to \[0, 1]
   * 📦 **Batch Dimension:** Added for TensorFlow input

4. ## Flask Backend
   A lightweight Flask server handles prediction, file uploads, and routing.

   * 🔁 API Endpoints
   
   | Endpoint          | Description                              |
   | ----------------- | ---------------------------------------- |
   | `/`               | Home route (renders upload UI)           |
   | `/upload`         | POST route for image upload & prediction |
   | `/uploads/<file>` | Serves uploaded image to frontend        |
   | `/health`         | Basic health check for deployment        |
   
   * Predictions are returned along with disease name and short info.
   * Uploaded images are stored temporarily.


5. ## Frontend (index.html) 
   User interface built with HTML & Bootstrap.

* 📋 Features:

   * 📤 Upload button with file preview
   * 📊 Displays predicted class and description
   * 🔄 Dynamically updates results via Flask backend

6. ## Deployment Guide 
   * ⚙️ Deploy on [Render](https://render.com)

      1. Push your project to a public GitHub repository
      2. Create a new **Web Service** in Render and connect your repo
      3. Set:
      
         * **Build Command**:
      
           ```bash
           pip install -r requirements.txt
           ```
         * **Start Command**:
      
           ```bash
           gunicorn app:app
           ```
      
   * 🧠 Model Hosting Workaround
      
      If model size > 100MB:
      
      * Upload the `.h5` model to:
      
        * [Google Drive](https://drive.google.com)
        * [Hugging Face Hub](https://huggingface.co)
        * Amazon S3
      * In your code, download it at runtime using:
      
        >> gdown.download() or requests.get()

7. ## Performance & Accuracy

      * ✅ **Test Accuracy**: \~85% on unseen images
      * 🧪 Handles a variety of hair types and lighting conditions
      
      ### 🔬 Evaluation Metrics:
      
      * Precision, Recall, F1-score (for each class)
      * Confusion matrix included in Jupyter notebook

8. ## Future Improvements

   * 📱 Build a mobile version (React Native / Flutter)
   * 🏷️ Expand dataset for more scalp conditions
   * 🔐 Add JWT-based auth for upload protection


## 🙌 Made with ❤️ using Python, TensorFlow, Flask & Streamlit
```
