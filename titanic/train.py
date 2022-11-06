import numpy as np
import pandas as pd
import torch
import torch.optim as optim
import torch.nn.functional as F

from dnn import DNN

train_dataset = pd.read_csv("train.csv")

# Fill NaN values to median of ages.
train_dataset['Age'].fillna(train_dataset['Age'].median(), inplace=True)

# Replace ages under 1.0 to 1.0
train_dataset[train_dataset['Age'] < 1.0] = 1.0

# Encoding object('male', 'female') to integer(0, 1)
train_dataset['Sex'].replace(['male', 'female'], [0, 1], inplace=True)

# Selecting features
features = ['Fare', 'Pclass', 'Sex', 'Parch', 'SibSp', 'Age']
train_x = train_dataset[features].to_numpy(dtype=np.float64)
train_y = train_dataset["Survived"].to_numpy(dtype=np.float64).reshape(len(train_dataset), 1)

# Create tensors
train_x, train_y = torch.Tensor(train_x), torch.Tensor(train_y)

# Ready for train my model
model = DNN()
optimizer = optim.SGD(model.parameters(), lr=0.15)

# Training
num_epochs = 1000
highest_accuracy = 0.0
for epoch in range(1, num_epochs + 1):
    prediction = model(train_x)
    cost = F.binary_cross_entropy(prediction, train_y)

    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    if epoch % 100 == 0:
        over_half = prediction >= 0.5
        correct_pred = over_half == train_y
        accuracy = correct_pred.sum().item() / len(correct_pred)
        print(f"Epoch: {epoch}\tLoss: {cost:3f}\tAccuracy: {accuracy:3f}")

        # Save my model
        if accuracy > highest_accuracy:
            highest_accuracy = accuracy
            torch.save(model.state_dict(), './custom_dnn.pt')
            print(f"Model saved at {epoch} epoch.")