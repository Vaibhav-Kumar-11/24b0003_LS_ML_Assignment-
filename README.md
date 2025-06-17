# 💻 ML Week 1 Assignment – Learners’ Space  
**👤 Name:** Vaibhav  
**🆔 Roll No.:** 24b0003  

This assignment focuses on basic ML workflows and data handling using **NumPy**, **Pandas**, **Scikit-learn**, and simple **NLP pipelines**.

---

## 📌 Q1 – NumPy Tasks  
- Created a `5x4` array and extracted **anti-diagonal** values.  
- Found **row-wise max** values and elements ≤ **overall mean**.  
- Implemented **boundary traversal** of the matrix.

## 📌 Q2 – NumPy Stats & Custom Sort  
- Generated a float array (1–10), applied `round()`, found `max`, `min`, and `median`.  
- Squared values < 5 and applied **alternate min-max sorting**.

## 📌 Q3 – Pandas Grading  
- Built a student dataset, assigned grades (`A` to `F`).  
- Sorted by `Score` and filtered top performers with grades **A/B**.

## 📌 Q4 – Sentiment Classification (BoW + Naive Bayes)  
- Created a movie review dataset.  
- Used `CountVectorizer` and trained a `MultinomialNB` model (80–20 split and 75-25 split).  
- Predicted sentiment for a new custom review.

## 📌 Q5 – Product Review Classification (TF-IDF + Logistic Regression)  
- Applied `TfidfVectorizer` on review texts.  
- Trained a `LogisticRegression` model and evaluated with `classification_report`.  
- Predicted label for a sample input like:  
  `"This was the worst product I ever used"`

---

## 🧰 Libraries Used  
- `numpy`  
- `pandas`  
- `scikit-learn`

---

## 🛠️ How to Run  
Make sure the required libraries are installed:

```bash
pip install numpy pandas scikit-learn
