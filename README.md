
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
├── model/                                                                                                                                                                                    
├── static/uploads/                                                                                                                                                                        
├── templates/                                                                                                                                                                             
├── disease\_info.json                                                                                                                                                                   
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

5. Load hairdisease dataset into root directory from xyzkaggle.com
   run >>python splittor.py
   to create train/..,test/.. and val/.. in hairdisease folder from all/.. folder
   
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
   Brief about the motivation and problem.

2.  ## Model Architecture
   - Based on InceptionV3 (pre-trained on ImageNet)
   - Fine-tuned on scalp disease dataset

3. ## Preprocessing Pipeline
   - Image resize to 150x150  
   - RGB conversion  
   - Normalization and batch dimension

4. ## Flask Backend
   - Routes: `/`, `/upload`, `/uploads/<file>`, `/health`  
   - Handles prediction, file saving, and disease info retrieval

5. ## Frontend (index.html) 
   - File upload UI  
   - Result display with disease details

6. ## Deployment Guide 
   - How to deploy on Render  
   - Large model workaround using Hugging Face or Google Drive

7. ## Performance & Accuracy
   - 85%

```
