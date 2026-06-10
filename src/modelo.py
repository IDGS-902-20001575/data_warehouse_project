import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error, accuracy_score

# Cargar datos
df = pd.read_csv("../data/dataset.csv")

# Variables
X = df[['tiempo']]
y_reg = df['accesos']
y_clf = df['tipo']

# División
X_train, X_test, y_train_reg, y_test_reg = train_test_split(X, y_reg, test_size=0.2, random_state=42)
_, _, y_train_clf, y_test_clf = train_test_split(X, y_clf, test_size=0.2, random_state=42)

# Regresión
modelo_reg = LinearRegression()
modelo_reg.fit(X_train, y_train_reg)
pred_reg = modelo_reg.predict(X_test)

# Clasificación
modelo_clf = DecisionTreeClassifier()
modelo_clf.fit(X_train, y_train_clf)
pred_clf = modelo_clf.predict(X_test)

# Resultados
print("=== RESULTADOS ===")
print("MSE:", mean_squared_error(y_test_reg, pred_reg))
print("Accuracy:", accuracy_score(y_test_clf, pred_clf))
