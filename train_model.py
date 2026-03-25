import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import pickle 

#loading the dataset
df = pd.read_csv("dataset.csv")

#encode categorical column
le_comm = LabelEncoder()
le_lead = LabelEncoder()
le_cre = LabelEncoder()

df["Communication"] = le_comm.fit_transform(df["Communication"])
df["Leadership"] = le_lead.fit_transform(df["Leadership"])
df["Creativity"] = le_cre.fit_transform(df["Creativity"])

#seperating features and target 
X = df.drop("Career", axis = 1)
y = df["Career"]

#train test data
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

#training the model 
model = DecisionTreeClassifier()
model.fit(X_train,y_train)

#checking accuracy
accuracy = model.score(X_test,y_test)
print("Accuracy: ", accuracy)

#save the model
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("model/encoders.pkl", "wb") as f:
    pickle.dump({
        "communication": le_comm,
        "leadership": le_lead,
        "creativity": le_cre
    }, f)

importances = model.feature_importances_
features = X.columns

for f, imp in zip(features, importances):
    print(f, ":", imp)

print("Model successfully saved!")


