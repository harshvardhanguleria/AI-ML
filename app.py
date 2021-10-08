import streamlit as st

st.title("Iris Machine Learning")

from sklearn.datasets import load_iris
iris = load_iris()
x = iris.data
y = iris.target

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(x,y)

sp = st.slider("Enter the Sepal Length",4.3,7.9,4.9)
sw =st.slider("Enter the Sepal Width",2.0,4.4,2.2)
pl =st.slider("Enter the Petal Length",1.0,6.9,3.0)
pw =st.slider("Enter the Petal Width",0.1,2.5,0.9)

op = model.predict([[sp,sw,pl,pw]])
op = iris.target_names[op[0]]
st.title(f'The flower predicted is {op.upper()}')