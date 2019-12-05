from numpy import array
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import pandas as pd
import random as rd

def model():


    RSP = pd.read_csv("RPS/data.csv")

    This_Id = list(RSP["id"])
    Playerlist = list(RSP["Player"])
    AI = list(RSP["Lose_or_Win"])

    DataA = [0]*len(Playerlist)
    for i in range(0,len(Playerlist)):
        if Playerlist[i] =='rock':
            DataA[i] = 1
        elif Playerlist[i] =='paper':
            DataA[i] = 20
        elif Playerlist[i] == 'scissors':
            DataA[i] = 300
    DataX = AI
    for i in range(0,len(Playerlist)):
        DataX[i] = DataA[i] * DataX[i]
    DataY = This_Id

    X = array(DataX).reshape(len(DataX),1,1)

    model = Sequential()
    model.add(LSTM(50,activation='relu',return_sequences=True,input_shape=(1,1)))
    model.add(LSTM(50,activation='relu'))
    model.add(Dense(1))
    model.compile(optimizer='adam',loss='mse')
    # print(model.summary())

    model.fit(X,DataY,epochs=100,validation_split=0.01,batch_size=1)

    test_input = array([len(DataX)+1])
    test_input = test_input.reshape((1,1,1))
    test_output = model.predict(test_input,verbose=0)
    #print(test_output)


    #user => scissors
    if test_output/100 >=1:
        output = "rock"
    #user => paper
    elif test_output/100 < 1 and test_output/10 >=1:
        if test_output >= 67 :
            output = "rock"
        elif test_output <67 and test_output >= 33:
            output = "scissors"
        else:
            output = "papper"
    # user => rock
    else:
        output = "paper"

    return output
