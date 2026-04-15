# Background Questions

## 1. Which packages are available for Machine Learning? Pros, cons, and availability

Common machine learning packages include **scikit-learn**, **TensorFlow**, **PyTorch**, and **XGBoost**.
- **scikit-learn** is easy to use and well documented, but not suitable for very large neural networks.
- **TensorFlow** is powerful and scalable, especially for deep learning, but has a steep learning curve.
- **PyTorch** is very flexible and popular in research, but sometimes less optimized for production.
- **XGBoost** is very efficient for structured data, but less intuitive for beginners.


---

## 2. What is ChEMBL? How do you access it?

ChEMBL is a large, open-access database containing information about bioactive molecules with drug-like properties.  
It is widely used in drug discovery to link chemical compounds to biological targets.

You can access ChEMBL via:
- The ChEMBL website
- REST API
- Python package (`chembl_webresource_client`)

---

## 3. What is machine learning, and how does it differ from traditional programming?

Machine learning is a method where a computer learns patterns from data to make predictions or decisions.  
In traditional programming, rules are explicitly written by humans, while in machine learning the rules are learned from data.

---

## 4. What are the key concepts and techniques in machine learning?

Key concepts include:
- Features
- Labels
- Training and testing
- Overfitting and underfitting

Common techniques include regression, classification, clustering, and neural networks.

---

## 5. What are the different types of machine learning algorithms?

The main types are:
- **Supervised learning** (e.g. classification, regression)
- **Unsupervised learning** (e.g. clustering)
- **Semi-supervised learning**
- **Reinforcement learning**

---

## 6. What are common applications of machine learning?

Machine learning is used in:
- Drug discovery
- Image and speech recognition
- Recommendation systems
- Fraud detection
- Autonomous vehicles

---

## 7. How do you evaluate the performance of a machine learning model?

Performance is evaluated using metrics such as accuracy, precision, recall, F1-score, ROC-AUC, or mean squared error.  
Cross-validation is commonly used to ensure reliable evaluation.

---

## 8. How do you prepare data for use in a machine learning model?

Data preparation includes:
- Cleaning missing values
- Removing duplicates
- Feature scaling and normalization
- Encoding categorical variables
- Splitting data into training and test sets

---

## 9. What are common challenges in machine learning, and how can they be addressed?

Common challenges include:
- Overfitting → solved by regularization or more data
- Imbalanced datasets → solved by resampling
- Poor data quality → solved by careful data cleaning
- High computational cost → solved with HPC or GPUs

---

## 10. What are resources and tools available to learn and practice machine learning?

Useful resources include:
- Online courses (Coursera, edX)
- Documentation and tutorials
- GitHub repositories
- Google Colab
- Scientific publications


# Talktorial questions

## 1. What is in the training set, and how big is it?

The training set is based on a ChEMBL dataset containing experimentally
measured, drug‑like molecules with kinase activity data.

The file contains 179’827  rows and the following columns:
- smiles
- standard_value
- standard_units
- target_chembl_id
- molecule_chembl_id
- an unnamed column

---

## 2. What modifications are needed to perform the tutorial?

To successfully run the tutorial, several structural modifications
are required:
- The unnamed index column is removed.
- A single kinase target is selected (the most common target).
- Activity values are converted to pIC50.
- SMILES strings are validated before fingerprint generation.

---

## 3. What is a test set? Are there other types of sets?

A test set is a portion of the data kept completely separate from
training and used only to evaluate model performance on unseen data.

Other common dataset splits include:
- Training set → used to fit the model
- Validation set → used to tune hyperparameters and monitor overfitting
- Test set → used once for final evaluation

---

## 4. What is done in each notebook cell of the talktorial?

1. Import required libraries.
2. Sets paths to the notebook location
3. Loads dataset
4. Inspects dataset structure 
5. Displays first rows and titles
6. Keeps only required columns like pIC50 and smiles
7. Defines a SMILES to fingerprint helperfunction, because learning model can only work with numbers.
8. This code generates molecular fingerprints, verifies the dataframe structure, previews sample rows, and marks the cell output for automated notebook validation.
9. Split data into training and test sets (70/30).
10. Define the neural network architecture.
11. Set training parameters.
12. Trains models using different batch sizes and plots training and validation loss curves.
13. Saves the trained model
14. Evaluate the model on the test set: Measures how well the trained model generalizes unseen data
15. Generate test predictions.
16. Plot predicted vs. true pIC50 values.
17. Load external unlabeled data.
18. Same thing as before --> converting string to numbers.
19. Loads the before trained model.
20. With this the model can now predict the pIC50 of the new data
21. Saves the predicted data
22. Shows the top 3 drugs
23. Draws the top 3 drugs


# T022 used on kinase.csv
<img width="1328" height="277" alt="image" src="https://github.com/user-attachments/assets/91f9bd41-b0ea-4c71-a9a0-bc6ecb153a43" />
<img width="1315" height="474" alt="image" src="https://github.com/user-attachments/assets/4d7b892c-642b-4019-93bb-2d5a42c2f0a7" />
<img width="1318" height="431" alt="image" src="https://github.com/user-attachments/assets/a7a0f1d2-1f67-4cf7-bc9f-4c6c7e874904" />
<img width="1328" height="477" alt="image" src="https://github.com/user-attachments/assets/e45e3319-a1f4-44a1-a2c9-f67b0bf284ec" />
<img width="1331" height="236" alt="image" src="https://github.com/user-attachments/assets/511fc72d-740f-4e0b-be70-03e2120cd9e7" />
<img width="941" height="393" alt="image" src="https://github.com/user-attachments/assets/aa71308b-b089-43f6-a748-4023f18256bf" />
<img width="1315" height="310" alt="image" src="https://github.com/user-attachments/assets/6ec41306-b4a7-48b6-a4e5-4f48a1384fd1" />
<img width="1244" height="562" alt="image" src="https://github.com/user-attachments/assets/00472d45-ac0a-4299-ad15-37464b8f910d" />
<img width="982" height="313" alt="image" src="https://github.com/user-attachments/assets/829b72b4-11dc-4320-aadd-b7dde00add93" />
<img width="1500" height="637" alt="image" src="https://github.com/user-attachments/assets/0802cc5d-ca5d-4701-b496-924684494df7" />
<img width="1684" height="603" alt="image" src="https://github.com/user-attachments/assets/7ccc204a-6c2a-4dbd-be4e-2f6f9be8941f" />
<img width="1722" height="340" alt="image" src="https://github.com/user-attachments/assets/40c85305-8d7e-457b-a2b7-89f21a00a1f0" />
<img width="1604" height="379" alt="image" src="https://github.com/user-attachments/assets/f7241fa8-16c8-4e30-b5d4-d1fd3528d968" />
<img width="1699" height="346" alt="image" src="https://github.com/user-attachments/assets/31bc9052-63f4-4182-8868-66b53155bdc7" />
<img width="1711" height="600" alt="image" src="https://github.com/user-attachments/assets/e3ded0bf-b4aa-487f-9c32-06f5f4d664d6" />
<img width="1726" height="411" alt="image" src="https://github.com/user-attachments/assets/d11bd8f7-5fef-431f-b4b1-ec9ef0aa60c2" />
<img width="1420" height="566" alt="image" src="https://github.com/user-attachments/assets/5e93f503-69d5-43fc-8ae2-0bae17af6a21" />
<img width="1722" height="160" alt="image" src="https://github.com/user-attachments/assets/f4a33c82-831d-4b53-b228-432e15c1ecd7" />
<img width="1716" height="443" alt="image" src="https://github.com/user-attachments/assets/a6bff5e7-88df-4e4a-a673-c9ddf17536bd" />
<img width="1719" height="460" alt="image" src="https://github.com/user-attachments/assets/dfb0ee0b-0843-4e42-9b8e-8a8a162e4912" />
<img width="1723" height="619" alt="image" src="https://github.com/user-attachments/assets/0e7b8912-ac45-4737-8660-247e2e77f636" />



# UBELIX

## What is Ubelix?
It is a high performing computer cluster, which can be used by the scientist of the university of Bern, when big computing power is needed. 
## How do you gain access?
Under the following link a application with why you need it must be written:
https://serviceportal.unibe.ch/esc?id=sc_cat_item&sys_id=1d137767db54141078ed3e48229619a7&tech=hpc
## How do you submit a job?
You write the code in pycharm for example and via sbatch run it then in ubelix.
## Who can have access?
Everybody who gets excess from the IT- of uni Bern, which is from students to partner companies to employees. 
# UBELIX training code:
<img width="1709" height="672" alt="image" src="https://github.com/user-attachments/assets/0733e454-2789-4880-b081-849ccc475e35" />
<img width="1709" height="71" alt="image" src="https://github.com/user-attachments/assets/cdf28fd5-59ff-46ce-a1cf-66394a5a052b" />
<img width="1642" height="502" alt="image" src="https://github.com/user-attachments/assets/62df5855-b789-4227-885f-cc3e82d7e723" />
<img width="1360" height="671" alt="image" src="https://github.com/user-attachments/assets/621d4c16-7a85-487a-bd6f-1ddecb459b15" />
<img width="1364" height="807" alt="image" src="https://github.com/user-attachments/assets/b979e17e-7e62-437d-b744-f0ac0fb86892" />











