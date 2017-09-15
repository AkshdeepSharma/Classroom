from sklearn import datasets
iris = datasets.load_iris()

X = iris.data
y = iris.target

# Splits data
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

# Tree classifier
from sklearn import tree
my_classifier = tree.DecisionTreeClassifier()

# Train data
my_classifier.fit(X_train, y_train)
predictions = my_classifier.predict(X_test)

# Prints accuracy score
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))


# KNeighborsClassifier + train
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier()
clf.fit(X_train, y_train)

clf_predict = clf.predict(X_test)

print(accuracy_score(y_test, clf_predict))

