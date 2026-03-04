# 🍽️ Yelp Restaurant Recommendation System: A Comparative Study
A comparative study of rank-based, user-user, item-item, and matrix factorization recommendation algorithms applied to Yelp restaurant review data.
![Graphical Summary](attachments/yelp.png)

## 📂 Table of Contents
- [Overview](#-overview)
- [Dataset](#-dataset)
- [Problem Statement](#-problem-statement)
- [Methodology](#-methodology)
- [Results](#-results)
- [Insights & Recommendations](#-insights--recommendations)
- [Technologies Used](#technologies-used)
- [How to Run](#how-to-run)

## 🧠 Overview
This project implements multiple restaurant recommendation approaches, including rank-based (average ratings), user–user similarity, item–item similarity, and model-based collaborative filtering using matrix factorization. Model performance is evaluated using Precision@K, Recall@K, and F₁-score, enabling the generation of personalized top-N restaurant recommendations.

## 📊 Dataset
This dataset was originally provided as part of the **Yelp Dataset Challenge**. It consists of a large collection of user reviews and business information, where each row represents a user’s rating of a restaurant. For this project, a **subset of the original dataset** was used due to hardware constraints.

Each record contains features describing **which user**, **which restaurant**, and **the rating** provided by the user.

| Variable      | Description                                   |
|---------------|-----------------------------------------------|
| user_id       | Unique identifier for each user               |
| business_id   | Unique identifier for each restaurant         |
| stars         | Rating given by the user (1–5 scale)           |

> **Note:** The original dataset exceeds GitHub's upload limit.  
> To access the data, please contact me via my portfolio website:  
> [Contact Charles Jiao](https://charles-jiao.netlify.app/contact)

## ❓ Problem Statement
Restaurant discovery platforms list thousands of dining options, making it challenging for users to find restaurants that match their tastes and preferences. Traditional recommendations, such as word-of-mouth or online reviews, are often limited by personal networks and information overload.

The goal of this project is to **build a recommendation system** that can predict a user’s restaurant preferences and provide **personalized top-N restaurant recommendations**. This is achieved by implementing and comparing multiple approaches, including **rank-based methods, collaborative filtering (user–user and item–item), and model-based matrix factorization**, and evaluating their performance using **Precision@K, Recall@K, F₁-score, and RMSE**.


## 🔎 Methodology
The recommendation system development followed an **end-to-end workflow** from data preprocessing to model evaluation and delivery:

1. **Data Preparation**  
   - Loaded the dataset containing user–restaurant ratings.  
   - Performed basic exploratory data analysis to understand rating distributions, user activity, and restaurant popularity.  
   - Created a **user–item interaction matrix** for collaborative filtering models.

2. **Model Implementation**  
   - **Rank-based recommendation:** Predicted ratings based on average restaurant ratings.  
   - **User–User collaborative filtering:** Estimated ratings using similarity between users.  
   - **Item–Item collaborative filtering:** Estimated ratings using similarity between restaurants.  
   - **Model-based collaborative filtering (matrix factorization):** Factorized the user–item matrix to capture latent features.

3. **Model Evaluation**  
   - Split data into training and test sets.  
   - Evaluated models using **Precision@K, Recall@K, F₁-score, and RMSE** to measure recommendation accuracy and coverage.  

4. **Hyperparameter Optimization**  
   - Applied **grid search cross-validation** to identify optimal parameters for similarity-based and matrix factorization models.  
   - Selected the best-performing models for generating final recommendations.

5. **Recommendation Delivery**  
   - Generated **top-N personalized restaurant recommendations** for each user based on predicted ratings.  
   - Optionally, ranked recommendations using **corrected ratings** that account for both predicted ratings and restaurant popularity.

This methodology ensures a **robust, end-to-end pipeline** for building and evaluating restaurant recommendation systems.

## 📈 Results
The recommendation models were evaluated using **Precision@K, Recall@K, F₁-score, and RMSE**. Key observations include:

1. **Rank-based Recommendation**  
   - Simple average-based predictions  
   - Achieved moderate RMSE but limited personalization  

2. **User–User Collaborative Filtering**  
   - Leveraged similarity between users to predict ratings  
   - **Highest F₁-score**, indicating the best overall recommendation performance  

3. **Item–Item Collaborative Filtering**  
   - Used restaurant similarity for rating prediction  
   - Performed slightly lower than user–user filtering but still improved over rank-based model  

4. **Model-Based Collaborative Filtering (Matrix Factorization)**  
   - Captured latent features through matrix factorization  
   - Provided balanced performance in terms of accuracy and scalability  

**Performance Metrics (Example)**

| Model                           | RMSE   | Precision@K | Recall@K | F₁-score |
|---------------------------------|--------|-------------|----------|----------|
| Rank-based                       | 0.98   | 0.76        | 0.54     | 0.63     |
| User–User CF                     | 0.88   | 0.74        | 0.51     | 0.60     |
| Item–Item CF                     | 0.95   | 0.76        | 0.55     | 0.64     |
| Model-Based CF (Matrix Factorization) | 0.94   | 0.76        | 0.55     | 0.64     |

**Key Takeaways**

- Collaborative filtering models significantly outperform rank-based recommendations.  
- User–User similarity-based CF achieved the **best F₁-score**, making it the most effective approach for this dataset.  
- Matrix factorization provides good scalability and comparable performance, suitable for larger datasets.  
- Performance can be further improved through **hyperparameter tuning** and **hybrid recommendation strategies**.

## 💡 Insights & Recommendations

**Insights:**
- Collaborative filtering models (both user-user and item-item) consistently outperform rank-based methods, highlighting the importance of leveraging user or restaurant similarities.  
- User–User collaborative filtering achieved the highest F₁-score, indicating strong alignment between predicted and actual user preferences.  
- Matrix factorization effectively captures latent features, providing a scalable solution for large restaurant datasets with performance comparable to similarity-based methods.  
- Restaurants with higher rating counts tend to stabilize predictions, emphasizing the role of popularity in recommendation accuracy.  

**Recommendations:**
- Deploy **User–User collaborative filtering** as the primary recommendation engine for this dataset to maximize user satisfaction.  
- Consider **hybrid recommendation systems** combining collaborative filtering with rank-based methods to further improve recommendations.  
- Continuously update models with **new user ratings** to maintain accuracy and relevance over time.  
- Explore additional **hyperparameter tuning** and feature engineering (e.g., temporal trends, cuisine types, or location-based preferences) to enhance model performance.

<a id="technologies-used"></a>
## ⚙️ Technologies Used
- **Python** – General purpose programming
- **Pandas** – Data manipulation and analysis
- **NumPy** – Numerical computations
- **Matplotlib & Seaborn** – Data visualization
- **Surprise** - Recommendstion System Library
- **Scikit-learn** – Machine Learning tools for metrics and evaluation

<a id="how-to-run"></a>
## ▶️ How to Run
```bash
# Clone the repository
git clone https://github.com/elescj/015-yelp-lr.git
cd 015-yelp-lr

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the script
python main.py
```
