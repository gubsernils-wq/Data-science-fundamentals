
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split

# Load dataset
DATA_PATH = "egfr_processed.csv"
df = pd.read_csv(DATA_PATH)

df = df[["canonical_smiles", "pIC50", "fingerprint"]].dropna()

def fix_fp(x):
    if isinstance(x, str):
        return np.fromstring(x.replace("[","").replace("]",""), sep=" ", dtype=int)
    return np.array(x, dtype=int)

df["fingerprint"] = df["fingerprint"].apply(fix_fp)

X = np.stack(df["fingerprint"].values).astype(float)
y = df["pIC50"].values

x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

def neural_network_model(hidden1, hidden2):
    model = Sequential()
    model.add(Dense(hidden1, activation="relu"))
    model.add(Dense(hidden2, activation="relu"))
    model.add(Dense(1, activation="linear"))
    model.compile(loss="mse", optimizer="adam", metrics=["mse", "mae"])
    return model

batch_size = 32
epochs = 50
layer1_size = 64
layer2_size = 32

model = neural_network_model(layer1_size, layer2_size)

history = model.fit(
    x_train,
    y_train,
    batch_size=batch_size,
    epochs=epochs,
    validation_data=(x_test, y_test),
    verbose=2
)

model.save("egfr_model.h5")

with open("training_log.txt", "w") as f:
    f.write("Final validation loss: " + str(history.history["val_loss"][-1]) + "\n")
    f.write("Final validation MAE: " + str(history.history["val_mae"][-1]) + "\n")

print("Training complete.")
