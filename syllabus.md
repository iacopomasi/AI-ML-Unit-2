---
layout: default
---

# Syllabus <a name="syllabus"></a>

## ℹ️ Provisional course agenda at a glance


| Topic                | Hours       | 
| :-------------:      |:-------------:
| Intro, Math Recap    | 5
|          **Unsupervised Learning**      |
| Dimensionality Reduction (PCA, Eigenvectors, SVD) | 5 |
|   Clustering (kmeans, GMM)         | 5           |
|          **Supervised Learning, Non-parametric**      |
| Decision trees | 5 |
| Random Forest/Nearest Neigh. | 5 |
|          **Supervised Learning, Parametric**      |
| Linear Regression with Least Squares | 5 |
| Polynomial regression, under/overfitting | 5 |
| Perceptron, Logistic Regression (LR) | 5 |
| SVM | 5 |
| **Deep Learning** |
| from LR to Neural Nets | 15 |
| **Total** | 60 |

## Program Outline in Detail *(Tentative)*: 

**Intro:**
 - What is Machine Learning (ML)?
 - From rule-based systems to learning taking decisions
 - Type of problems we can solve with ML
 - Basic Statistics, Recap of Linear Algebra and Probability Theory
 - Multivariate Gaussian distribution, Mahalanobis distance, L_p norm
 - Correlation vs Causality
 - The “curse” of dimensionality and the manifold assumption. Unintuitive properties of high-dimensional geometry.
 
**Unsupervised Learning:**
- Dimensionality Reduction: Principal Components Analysis (PCA), t-SNE
- Clustering, Kmeans, Expectation-Maximization (EM)
- Gaussian Mixture Model (GMM)

**Supervised Learning:**
 - Regression vs Classification
 - Non-parametric models: The Nearest Neighbour (NN) Classifier, Decision Trees/Random Forest
 - Polynomial Curve Fitting
 - Parametric, Linear models: Linear regression, Least-Squares, Logistic regression, Perceptron, 
 - Gradient Descent
 - Model complexity and Bias-Variance Tradeoff; Overfitting and underfitting problems; Empirical - Risk minimization, learning theory, regularization;
 - Support Vector Machines: Optimal hyperplane, margin, kernels
 -  **“Deep Learning”**: Overparametrized, non-linear models and differential programming
	-  Multilayer Perceptron
	- The backpropagation algorithm
	- Activation functions
	- Analytical gradient and numerical with finite differences
	- Computational Graph and Automatic Differentiation
	- Stochastic Gradient Descent (SGD) over mini-batches
	- DNN parameters estimation for classification as MLE (maximum likelihood estimation)
	- Loss function for classification: softmax+cross-entropy loss, information-theory interpretation.

**Toolsets**: Python, NumPy (matrix manipulation and linear algebra), scikit learn (basic ML), matplotlib (visualization), PyTorch (automatic differentiation and neural nets).


**Credits:** This program and material was inspired by the following courses: [Stanford CS299](http://cs229.stanford.edu/syllabus-spring2021.html),  [Doretto CS691A](http://vision.csee.wvu.edu/~doretto/courses/2016-fall-ml/), [Intro to ML Padova](https://en.didattica.unipd.it/off/2018/LT/SC/SC1167/000ZZ/SCP8084699/N0), [Stanford CS231](https://cs231n.github.io/),  [Sapienza DLAI](https://github.com/erodola/DLAI-s2-2021),  [Sapienza ML](https://twiki.di.uniroma1.it/twiki/view/ApprAuto/WebHome)
