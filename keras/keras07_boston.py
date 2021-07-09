from sklearn.datasets import load_boston
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


datasets = load_boston()
x = datasets.data
y = datasets.target

x_train, x_test, y_train, y_test = train_test_split(x, y,
        train_size=0.7)

print(x.shape)
print(y.shape)

#print(x_test)
#print(y_test)

#print(datasets.feature_names)
#print(datasets.DESCR)
'''
model = Sequential()
model.add(Dense(5, input_dim=13))
model.add(Dense(4))
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam')
model.fit(x_train, y_train, epochs=1000, batch_size=1)

loss = model.evaluate(x_test, y_test)
print('loss : ',loss)

y_predict = model.predict([x_test])
print('y_predict : ', y_predict)

r2 = r2_score(y_predict, y_test)
print('r2 : ',r2)

'''
# 완료!!