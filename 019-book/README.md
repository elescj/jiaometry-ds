# 📚 Book Recommendation System: Ranking, Collaborative Filtering, and Matrix Factorization
A comparative study of **rank-based recommendation, similarity-based collaborative filtering, and matrix factorization (SVD)** to generate personalized book recommendations from large-scale user–book rating data.

![Graphical Summary](attachments/book.png)

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

Recommendation systems play a central role in modern **e-commerce platforms**, helping users discover relevant products within large catalogs.

This project builds a **book recommendation system** using user–book interaction data. The study evaluates multiple recommendation approaches to understand their effectiveness in predicting user preferences.

Three major recommendation techniques are implemented and compared:

- **Rank-Based Recommendation**
- **User–User Collaborative Filtering**
- **Item–Item Collaborative Filtering**
- **Matrix Factorization using Singular Value Decomposition (SVD)**

The models are evaluated using both **rating prediction metrics** and **top-N recommendation metrics** to measure their performance in practical recommendation scenarios.

---

# 📊 Dataset

The dataset contains **user–book interaction data**, including user ratings and book metadata.

Two main tables are used:

### Ratings Dataset

| Variable | Description |
|--------|-------------|
| user_id | Unique identifier for each user |
| book_id | International Standard Book Number (ISBN) |
| rating | Rating given by the user (1–10 scale) |

### Books Dataset

| Variable | Description |
|--------|-------------|
| ISBN | Unique book identifier |
| Book-Title | Title of the book |
| Book-Author | Author of the book |
| Year-Of-Publication | Publication year |
| Publisher | Publishing company |

### Dataset Characteristics

- **1.1M user–book rating interactions**
- **77,805 unique users**
- **185,973 unique books**
- Ratings scale: **1–10**

After removing implicit ratings (rating = 0) and applying filtering rules:

- **Users with ≥ 50 ratings**
- **Books with ≥ 10 ratings**

Final modeling dataset:

- **26,698 interactions**
- Reduced sparsity and improved training efficiency.

---

# ❓ Problem Statement

Online bookstores often contain **hundreds of thousands of titles**, making it difficult for users to discover books that match their interests.

Recommendation systems address this challenge by analyzing **user–item interaction patterns** to predict which books a user may enjoy.

The objective of this project is to build and compare multiple recommendation models that:

- generate personalized book recommendations
- address cold-start scenarios
- handle sparse user–item interactions
- evaluate recommendation quality using ranking metrics

---

# 🔎 Methodology

The project follows an **end-to-end recommendation system pipeline**.

---

## 1. Data Preparation

Data preprocessing steps included:

- Removing **implicit ratings (rating = 0)**
- Handling missing book metadata
- Analyzing rating distributions
- Identifying highly active users and frequently rated books

To reduce sparsity:

- Users with **fewer than 50 ratings** were removed
- Books with **fewer than 10 ratings** were removed

---

## 2. Rank-Based Recommendation

A baseline recommendation model was implemented using **average book ratings**.

Steps:

1. Calculate the **average rating for each book**
2. Adjust scores using **corrected ratings** based on rating counts
3. Recommend the **highest-ranked books**

This model is particularly useful for **cold-start users** with no interaction history.

---

## 3. Collaborative Filtering

Two similarity-based collaborative filtering approaches were implemented using the **Surprise library**.

### User–User Collaborative Filtering

- Identifies users with **similar rating patterns**
- Recommends books liked by similar users

Similarity metric used:

- **Cosine Similarity**

---

### Item–Item Collaborative Filtering

- Computes similarity between **books based on rating patterns**
- Recommends books similar to those a user previously liked

Item-based methods often produce **more stable recommendations** because item relationships change less frequently.

---

## 4. Matrix Factorization (SVD)

To address sparsity and capture latent relationships, the project implements **Singular Value Decomposition (SVD)**.

Matrix factorization works by:

1. Decomposing the user–item interaction matrix
2. Learning **latent user preference vectors**
3. Learning **latent item feature vectors**
4. Predicting missing ratings from latent interactions

Hyperparameters were tuned using **grid search cross-validation**.

---

## 5. Model Evaluation

Models were evaluated using two categories of metrics:

### Rating Prediction

- **RMSE (Root Mean Squared Error)**

### Recommendation Quality

- **Precision@K**
- **Recall@K**
- **F1-score**

These metrics measure how accurately the model recommends relevant books.

---

# 📈 Results

The **SVD matrix factorization model** achieved the best performance.

| Model | RMSE | Precision | Recall | F1 |
|------|------|------|------|------|
| User–User CF | 1.845 | 0.816 | 0.812 | 0.814 |
| Tuned User–User CF | 1.686 | 0.834 | 0.891 | 0.862 |
| Item–Item CF | 1.621 | 0.802 | 0.800 | 0.801 |
| Tuned Item–Item CF | 1.588 | 0.818 | 0.836 | 0.827 |
| SVD | 1.511 | 0.827 | 0.860 | 0.843 |
| **Tuned SVD** | **1.502** | **0.829** | **0.856** | **0.842** |

Key findings:

- **Matrix factorization outperformed similarity-based models**
- Hyperparameter tuning significantly improved recommendation performance
- Collaborative filtering models successfully captured user preference patterns.

---

# 💡 Insights & Recommendations

### Insights

- Recommendation datasets typically exhibit **high sparsity**, requiring filtering or latent factor models.
- **Rank-based methods** are useful for cold-start scenarios.
- **Collaborative filtering** effectively captures user behavior patterns.
- **Matrix factorization** handles sparse data better by learning latent features.

---

### Recommendations

- Implement **hybrid recommendation systems** combining collaborative filtering with content-based features.
- Incorporate **book metadata** such as genre, author, or keywords.
- Apply **deep learning models** for large-scale recommendation systems.
- Deploy recommendation pipelines in **real-time production environments**.

---

# ⚙️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Scikit-learn**
- **Surprise (Recommendation System Library)**
- **Collaborative Filtering**
- **Matrix Factorization (SVD)**

---

# ▶️ How to Run

```bash
# Clone repository
git clone https://github.com/yourusername/book-recommendation-system.git
cd book-recommendation-system

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run notebook
jupyter notebook
