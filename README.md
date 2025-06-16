Name: Vaibhav
Roll Number: 24b0003
Topics Covered: NumPy, Pandas, Scikit-learn, NLP Pipeline, Regex

This repository contains my solutions to the first week of the Machine Learning track under Learners' Space. The questions focused on exploring core Python libraries like NumPy and Pandas, and introduced basic machine learning workflows using Scikit-learn, including data preprocessing, vectorization, model training, and evaluation.

Q1: NumPy Array Manipulation
Created a 5x4 NumPy array with random integers.

Extracted anti-diagonal elements.

Found max value of each row manually (without using NumPy’s built-in methods).

Constructed a new array with only elements ≤ overall mean, rest replaced with 0.

Implemented a boundary traversal function to output the matrix elements around the edge.

Key Concepts Used:
np.random.randint, array indexing, manual mean comparison, nested loops, boundary traversal logic.

Q2: NumPy Array Statistics and Custom Sort
Generated a 1D array of 20 floats scaled between 1 and 10.

Applied rounding using np.round().

Computed max, min, and median.

Applied element-wise transformation for values < 5.

Implemented a custom "alternate min-max" sort pattern.

Key Concepts Used:
np.random.rand, element-wise operations, array sorting, custom index logic.

Q3: Pandas DataFrame Grading and Filtering
Created a DataFrame with names, subjects, and scores.

Assigned grades (A-F) based on scores.

Sorted data by scores and calculated subject-wise averages.

Wrote a custom filter function to retain only students with grades A or B.

Key Concepts Used:
pd.DataFrame, .groupby(), .sort_values(), conditional filtering, custom function creation.

Q4: NLP Sentiment Classification using CountVectorizer
Created a labeled dataset of movie reviews.

Applied CountVectorizer for text vectorization.

Used train_test_split() to split data.

Trained a MultinomialNB classifier.

Measured model accuracy and implemented a custom review prediction function.

Key Concepts Used:
Bag-of-Words model, train/test split, Naive Bayes classifier, accuracy evaluation, CountVectorizer.

Q5: Text Classification using TF-IDF and Logistic Regression
Built a small review dataset for product feedback.

Applied TfidfVectorizer for text transformation.

Trained a logistic regression model to classify 'good' or 'bad' reviews.

Evaluated the model using classification_report().

Included a sample test to predict sentiment of new input text.
