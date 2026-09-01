import wittgenstein as lw
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

url_dataset = 'https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/mushrooms.csv'

df = pd.read_csv(url_dataset)

X = df.drop('type', axis = 1)
y = df['type'].apply(lambda x: True if x == 'p' else False)

X = pd.get_dummies(X)

X_train, X_test, y_train, y_test = train_test_split (X, y, test_size = 0.2, random_state = 25)

floresta = RandomForestClassifier(n_estimators=100, random_state=25)
floresta.fit(X_train, y_train)

y_pred = floresta.predict(X_test)

print("Acurácia: ", accuracy_score(y_test, y_pred))

importantes = floresta.feature_importances_
importantes_df = pd.DataFrame({'Atributo': X.columns, 'Importância': importantes})
importantes_df = importantes_df.sort_values(by='Importância', ascending=False).head(10)

plt.figure(figsize=(20,10))

plt.bar(importantes_df['Atributo'], importantes_df['Importância'])

plt.show()

