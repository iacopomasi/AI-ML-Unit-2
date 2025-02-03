# Machine Learning base

## Descrizione del corso


**Description:** Il corso ha lo scopo di introdurre il candidato all’apprendimento automatico (Machine Learning), una classe di metodi che apprendono modelli statistici e probabilistici dai dati ed eseguono previsioni su nuovi dati. In termini di struttura e filosofia, il corso bilancia la quantità di contenuti teorici (sapere cosa stai facendo) con sessioni pratiche (sapere come farlo). Le sessioni pratiche consistono in piccoli frammenti di codice python, numpy e sklearn che implementano gli algoritmi spiegati a lezione. Da notare che questo è un corso introduttivo al Machine Learning (ML) e non è un corso sul "Deep Learning" (DL). Il corso pone l'accento sulla parte teorica, anche se quest'ultima è sempre accompagnata da applicazioni pratiche su alcuni dati giocattolo al fine di capire concretamente il comportamento degli algoritmi di apprendimento. Quando possibile, il corso farà alcuni collegamenti a recenti articoli di ricerca in AI e ML e mostrerà alcune interessanti applicazioni di AI, come 3D Morphable Models (3DMM) e stima della posa umana che sta alla base del Microsoft Kinect.

## Preview
- A preview of the course slides can be found at [https://iacopomasi.github.io/AI-ML-Unit-2/](https://https://iacopomasi.github.io/AI-ML-Unit-2/)
- The slides can be viewed at [https://github.com/iacopomasi/AI-ML-Unit-2/tree/main/AA2324/course/ML.md](https://github.com/iacopomasi/AI-ML-Unit-2/tree/main/AA2324/course/ML.md)

##  🎯 Obiettivi

- Introduzione ai principi di base del Machine Learning
- Conoscenza delle principali modalità di apprendimento (supervisionato, non supervisionato, parametrico/non parametrico, modello discriminativo, modello generativo)
- Sviluppare la consapevolezza degli strumenti matematici alla base.
- Stabilire basi solide per corsi più avanzati (es. Deep Learning, Machine Learning Avanzato)
- Sviluppare il pensiero critico nell’utilizzo dell’apprendimento automatico e su come si valutano questi algoritmi.
- Mostra alcune applicazioni pratiche del Machine learning



## 📖 Syllabus

## 📖 Syllabus Corso Machine Learning Base

👨🏼‍🏫  = lezione frontale
🖥️  = sessione pratica con Google Colab

Syllabus indicativo per una settimana (**5 giorni**) di corso. L'ordine potrebbe non essere questo
e neppure l'associazione con i giorni della settimana.

Tutto il materiale e' disponibile a questo link https://github.com/iacopomasi/AI-ML-Unit-2/tree/main/AA2324/course

| Quando                      | Topic                                                                         					 | Notebook |
| -------------             | :-------------:                     | :-------------:                                                                |
| Lun mat                | 👨🏼‍🏫 Introduzione al ML, tipi di problemi risolti, e ripasso di Geometria ed Algebra Lineare         |       [`01_introduction.ipynb`](https://github.com/iacopomasi/AI-ML-Unit-2/blob/main/AA2324/course/01_introduction/01_introduction.ipynb) |
| Lun pom                | 👨🏼‍🏫 Decomposizione con Autovettori, Principal Component Analysis (PCA), 3D Morphable Models (3DMM)  |            [`02_math_recap_linear_algebra.ipynb`](https://github.com/iacopomasi/AI-ML-Unit-2/blob/main/AA2324/course/02_math_recap_linear_algebra/02_math_recap_linear_algebra.ipynb) [`03_math_recap_eig_pca_3dmm.ipynb`](https://github.com/iacopomasi/AI-ML-Unit-2/blob/main/AA2324/course/03_math_recap_eig_pca_3dmm/03_math_recap_eig_pca_3dmm.ipynb) |
| Merc mat               | 🖥️ Colab notebook su tensori, matrici e numpy             										 |  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://bit.ly/numpy_tensors) |
| Merc pom               | 👨🏼‍🏫 3DMM, PCA con dati ad alte dimensioni, the curse of dimensionality                              |    [`04_pca_svd_high_dim.ipynb`](https://github.com/iacopomasi/AI-ML-Unit-2/blob/main/AA2324/course/04_pca_svd_high_dim/04_pca_svd_high_dim.ipynb)         |
| Ven mat             | 🖥️ Colab notebook su SVD, PCA, modello generativo lineare                                          |        [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://bit.ly/svd-gen-mod) |
| Ven pom             | 👨🏼‍🏫 Clustering: The k-means algorithm		             								           | [`05_clustering_kmeans.ipynb`](https://github.com/iacopomasi/AI-ML-Unit-2/blob/main/AA2324/course/05_clustering_kmeans/05_clustering_kmeans.ipynb)  |
| Lun mat               | 👨🏼‍🏫 Linear Regression, Minimi Quadrati, Gradient Descent  	      									 |         [`11_regression_lsq_poly.ipynb`](https://github.com/iacopomasi/AI-ML-Unit-2/blob/main/AA2324/course/11_regression_lsq_poly/11_regression_lsq_poly.ipynb)     |                                         
| Lun pom               | 👨🏼‍🏫 Perceptron, Logistic Regression, L2 Regularization, K-nearest Neighbour Classifier              |     [`13_perceptron_logistic_reg.ipynb`](https://github.com/iacopomasi/AI-ML-Unit-2/blob/main/AA2324/course/13_perceptron_logistic_reg/13_perceptron_logistic_reg.ipynb) [`08_supervised_learning_knn.ipynb`](https://github.com/iacopomasi/AI-ML-Unit-2/blob/main/AA2324/course/08_supervised_learning_knn/08_supervised_learning_knn.ipynb)        |  
| Merc mat               | 🖥️ Colab notebook su Linear, Polynomial, Classificazione tramite Logistic Regression               |             [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](#) |
| Merc pom               | 👨🏼‍🏫 Model selection, Evaluation, Cross-Validation, ROC curve                        				 |   [`10_model_selection_crossvalid.ipynb`](https://github.com/iacopomasi/AI-ML-Unit-2/blob/main/AA2324/course/10_model_selection_crossvalid/10_model_selection_crossvalid.ipynb)              |
