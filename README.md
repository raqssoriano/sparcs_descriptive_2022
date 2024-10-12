# **HHA507 || Module 3 || Python Assignment: Descriptive Analytics on SPARCS 2022 Data**
## _*Project Title: SPARCS Descriptive 2022*_

---

📌 This repository contains my analysis and documentation for the 2022 SPARCS (Statewide Planning and Research Cooperative System) dataset. It includes **loading a portion of de-identified data**, **performing basic descriptive statistics** and **creating visualizations**. This allows me to explore *healthcare trends*, *patient demographics*, and *hospital performance metrics*.👩🏻‍💻🏥📊

📌 Please refer to [**sparcsdescriptive2022.ipynb**](https://github.com/raqssoriano/sparcs_descriptive_2022/blob/main/sparcsdescriptive2022.ipynb), which I created using **`Google Colab`**. It contains scripts/codes and provides easy access to data visualizations associated with the scripts and results.

📌 Almost same scripts/codes can also be found in [**sparcs2022.py**](https://github.com/raqssoriano/sparcs_descriptive_2022/blob/main/sparcs2022.py), which I created using **`Python`** in **`Visual Studio Code`**

---

## _*Steps Taken to Perform the Analysis*_

### **(1) The De-identified Data:**

1. I downloaded the dataset from **`health.data.ny.gov`**
    - For further information and a link to the dataset: [Hospital Inpatient Discharges (SPARCS De-Identified): 2022](https://health.data.ny.gov/Health/Hospital-Inpatient-Discharges-SPARCS-De-Identified/5dtw-tffi/about_data)

2. I used **pandas** to load a subset of data into a **`Python`** environment using my **`Visual Studio Code`**. I was able to explore data which includes `Age Group`, `Gender`, `Length of Stay`, `Total Charges`, `Total Costs`, and `Types of Admission`.


### **(2) Exploring Categorical Variables:**

- **The distributions and trends within the following are explored:**
    - Age Group
    - Gender
    - Type of Admission
    - Length of Stay
    - Total Charges
    - Total Costs
    - Type of Admission


### (3) The Basic Descriptive Statistics:

- **To understand the typical patterns and variations in **`Length of Stay`**, **`Total Charges`**, and **`Total Costs`**, I calculated the following:**
    - Mean
    - Median
    - Standard Deviation
    - Min/Max
    - Percentiles (25th, 50th, 75th)
    - Quartiles


### **(4)Data Visualization:**

- **Histogram** of **`Length of Stay`**: It visually represents the distribution of hospital stay durations.

- **Boxplot** for **`Total Charges`**: It helps identify potential outliers in the healthcare costs.

- **Bar plot** for **`Type of Admission`**: It provides insights into the relative frequencies of different reasons of admission.


### **(5) Handling Missing Data:**

 - Check for missing data/values.
 - Remove rows with missing values.
 - Fill missing data with the mean.
 - Verify if the filling the missing data is successful.


### **(6) Summary Report and Insights:**

- (a) *Average Length of Stay:* **`5.72 days`**
 
- (b) *Total Cost Variation:*

    - **★Total Cost Variation (Age Group)★**

        - It's true that cost of care tends to increase with age, particularly between 50 and 69. This increase is largely due to the higher prevalence of chronic conditions in this age group, such as hypertension, heart disease, diabetes, pneumonia, and COPD (Chronic Obstructive Pulmonary Disease). This conditions often need more frequent medical intervention, including emergency room visits, urgent care visits, and outpatient appointments. Additionally, individuals/patients with multiple chronic illnesses may require hospitalization which may significantly contribute to higher costs of treatment. In contrast, the 0-17 age group typically experiences fewer chronic illnesses, resulting in lower overall healthcare costs.

     <img src="/Users/raqsmacbookair/Desktop/1 - Age Group - Total Cost.png" width="300" />

     <img src="/Users/raqsmacbookair/Desktop/2 - Age Group Bar Plot.png" width="500" />

    - **★Total Cost Variation (Type of Admission)★**

        - **`TRAUMA admissions`** ➙ highest total cost; it involves serious and life-threatening injuries, which require specialized care and may include include advanced imaging such as MRI, ultrasound, and xrays. It often involves the use of operating rooms (OR) and surgical equipment. This can result in longer stays depending on the severity of the injuries sustained by patients.

        - **`NEWBORN admissions`** ➙ lowest total cost; healthy newborns may require shorter stay in the hospital, which is likely why it gets the lowest total cost, as most can be discharged once deemed safe.

     <img src="/Users/raqsmacbookair/Desktop/3 - Types of Admission - Total Cost.png" width="300" />

     <img src="/Users/raqsmacbookair/Desktop/4 - Types of Admission Bar Plot.png" width="500" />


- (c) *Noticeable Trends:*

    - **`EMERGENCY ADMISSIONS`** *(1,394,328)* - This is the highest volume of admission rates among the list within the health dataset. This could mean that acute care requires special attention, particularly in New York, which is the focus of this health dataset. It is essential to note the age group and the location or area of the contributing admission rates, as this could provide valuable insights on where the private/public health officials should allocate most of the financial support. Additionally, this data is crucial for hospitals or health systems to prepare in allocating beds, staffing, and other necessary resources to better meet the needs of the public or patients.

    - **`TRAUMA ADMISSIONS`** *(7,312)* - This is the second lowest admission rate in New York within this health dataset. As a former ED nurse, I am not surprised this is one of the lowest, as not all hospitals are considered level 1 trauma centers or may not even be trauma centers. This means patients who needed specialized care due to life-threatening injuries may require transfer to trauma center hospitals.

     <img src="/Users/raqsmacbookair/Desktop/5 - Type of Admission Distribution.png" width="300" />

     <img src="/Users/raqsmacbookair/Desktop/6 - Admission Type Bar Plot.png" width="500" />



