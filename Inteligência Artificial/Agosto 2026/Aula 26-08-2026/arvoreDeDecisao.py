import wittgenstein as lw
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

url_dataset = 'https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/mushrooms.csv'

df = pd.read_csv(url_dataset)

X = df.drop('type', axis = 1)
y = df['type'].apply(lambda x: True if x == 'p' else False)

X = pd.get_dummies(X)

X_train, X_test, y_train, y_test = train_test_split (X, y, test_size = 0.2, random_state = 25)

arvore = DecisionTreeClassifier(max_depth=5, random_state=25)
arvore.fit(X_train, y_train)

y_pred = arvore.predict(X_test)

print("Acurácia: ", accuracy_score(y_test, y_pred))

plt.figure(figsize=(20, 10))

plot_tree(arvore, feature_names=X.columns, class_names=['Comestível', 'Venenoso'], filled=True)
plt.show()

