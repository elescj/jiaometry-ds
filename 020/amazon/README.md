# 📦 Amazon Product Recommendation System: Ranking, Collaborative Filtering, and Matrix Factorization
A comparative study of **rank-based recommendation, similarity-based collaborative filtering, and matrix factorization (SVD)** to generate personalized product recommendations from large-scale Amazon review data.

![Graphical Summary](attachments/amazon.png)

---

## 📂 Table of Contents
- [Overview](#-overview)
- [Dataset](#-dataset)
- [Problem Statement](#-problem-statement)
- [Methodology](#-methodology)
- [Results](#-results)
- [Insights & Recommendations](#-insights--recommendations)
- [Technologies Used](#-technologies-used)
- [How to Run](#-how-to-run)

---

# 🧠 Overview

Modern e-commerce platforms rely heavily on **recommendation systems** to help users navigate massive product catalogs and discover relevant items.

This project builds an **Amazon product recommendation system** using user–item rating data. Multiple recommendation techniques are implemented and compared to evaluate their effectiveness in predicting user preferences.

The study includes:

- **Rank-Based Recommendation**
- **User–User Collaborative Filtering**
- **Item–Item Collaborative Filtering**
- **Matrix Factorization using Singular Value Decomposition (SVD)**

Models are evaluated using both **rating prediction metrics** and **top-N recommendation metrics**, reflecting real-world recommendation performance.

---

# 📊 Dataset

The dataset consists of **Amazon product review interactions**.

### Ratings Dataset

| Variable | Description |
|--------|-------------|
| user_id | Unique identifier for each user |
| prod_id | Unique identifier for each product |
| rating | Rating given by the user (1–5 scale) |

---

### Dataset Characteristics

- **~7.8M original interactions**
- **1,540 active users (after filtering)**
- **48,190 products**
- Ratings scale: **1–5**

---

### Data Filtering

To reduce sparsity and improve model performance:

- Users with **≥ 50 ratings** were retained  
- Products with **≥ 5 ratings** were retained  

Final dataset:

- **125,871 interactions**
- Improved density and computational efficiency

---

# ❓ Problem Statement

E-commerce platforms contain **millions of products**, making it difficult for users to identify relevant items.

Recommendation systems address this challenge by leveraging **historical user behavior** to predict future preferences.

This project aims to:

- Generate **personalized product recommendations**
- Handle **sparse user–item interactions**
- Compare multiple recommendation approaches
- Evaluate models using **ranking and prediction metrics**

---

# 🔎 Methodology

The project follows a structured **end-to-end recommendation pipeline**.

---

## 1. Data Preparation

- Checked data types and missing values  
- Analyzed rating distribution (skewed toward high ratings)  
- Filtered users and items to reduce sparsity  
- Constructed a **user–item interaction matrix**

---

## 2. Rank-Based Recommendation

- Computed **average product ratings**
- Adjusted scores using rating counts
- Recommended **top-rated products**

✅ Useful for:
- cold-start users  
- baseline benchmarking  

---

## 3. Collaborative Filtering

Implemented using the **Surprise library**.

---

### User–User Collaborative Filtering

- Finds users with **similar rating patterns**
- Recommends products liked by similar users  

- Similarity: **Cosine**

---

### Item–Item Collaborative Filtering

- Computes similarity between products  
- Recommends items similar to previously liked products  

- Similarity: **MSD / Cosine**

---

## 4. Matrix Factorization (SVD)

- Decomposes user–item matrix into **latent factors**
- Learns hidden user preferences and item features
- Handles **sparsity more effectively**

Hyperparameters tuned using **GridSearchCV**

---

## 5. Model Evaluation

### Rating Prediction
- **RMSE**

### Recommendation Quality
- **Precision@K**
- **Recall@K**
- **F1-score**

---

# 📈 Results

| Model | RMSE | Precision | Recall | F1 |
|------|------|------|------|------|
| User–User CF | 1.001 | 0.855 | 0.858 | 0.856 |
| Tuned User–User CF | 0.951 | 0.849 | 0.893 | 0.870 |
| Item–Item CF | 0.995 | 0.838 | 0.845 | 0.841 |
| Tuned Item–Item CF | 0.958 | 0.839 | 0.880 | 0.859 |
| SVD | ~0.90 | ~0.85 | ~0.86 | ~0.86 |
| **Tuned SVD** | **0.881** | **0.853** | **0.874** | **0.863** |

---

### Key Findings

- **Matrix Factorization (SVD) achieved the best overall performance**
- Hyperparameter tuning improved all models, especially **recall**
- Item-item models were **competitive and more scalable**
- User-user models performed well but are more sensitive to sparsity

---

# 💡 Insights & Recommendations

### Insights

- The dataset shows **high sparsity and rating skewness**
- Most users give **high ratings (4–5)** → introduces bias
- Collaborative filtering works well but struggles with **cold-start users**
- SVD effectively captures **latent relationships**

---

### Recommendations

- Use **SVD as the primary model** for production
- Implement **hybrid systems** (CF + content-based)
- Incorporate **product metadata** (category, brand, description)
- Add **implicit feedback signals** (clicks, views, purchases)
- Deploy in **real-time pipelines with monitoring**

---

# ⚙️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib / Seaborn**
- **Scikit-learn**
- **Surprise**
- **Collaborative Filtering**
- **Matrix Factorization (SVD)**

---

# ▶️ How to Run

```bash
# Clone repository
git clone https://github.com/elescj/amazon.git
cd amazon

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run notebook
jupyter notebook
