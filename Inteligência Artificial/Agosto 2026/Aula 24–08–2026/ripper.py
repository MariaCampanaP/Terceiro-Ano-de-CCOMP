import wittgenstein as lw
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

url_dataset = 'https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/mushrooms.csv'

df = pd.read_csv(url_dataset)

X = df.drop('type', axis = 1)
y = df['type'].apply(lambda x: True if x == 'p' else False)

X_train, X_test, y_train, y_test = train_test_split (X, y, test_size = 0.2, random_state = 25)

modelo_ripper = lw.RIPPER(random_state = 25)
modelo_ripper.fit(X_train, y_train)

y_pred = modelo_ripper.predict(X_test)

print(f"\nAcurácia: {accuracy_score(y_test, y_pred) * 100:.2f}%")

print("Regras geradas:\n")
print(modelo_ripper.out_model())