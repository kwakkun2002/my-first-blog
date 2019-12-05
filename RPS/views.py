from django.shortcuts import render
from .models import *
from .RNNModel import model
# Create your views here.

from numpy import array
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import pandas as pd
import random as rd
import csv

import threading
import time

 
f = open('RPS/data.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

cach = []

for line in rdr:
    cach = line


f.close()    

static_num = int(cach[0])

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

    model.fit(X,DataY,epochs=40,validation_split=0.01,batch_size=1)

    test_input = array([len(DataX)+1])
    test_input = test_input.reshape((1,1,1))
    test_output = model.predict(test_input,verbose=0)
    #print(test_output)
    if test_output > 300:
        output = "rock"
    elif test_output <300 and test_output >150:
        output = "rock"
    elif test_output < 150 and test_output>25:
        output = "scissor"
    elif test_output == 150:
        num = rd.randrange(1,3)
        if num == 1:
            output = "scissor"
        elif num == 2:
            output = "rock"
    elif test_output == 25:
        num = rd.randrange(1,3)
        if num == 1:
            output = "paper"
        elif num ==2:
            output = "scissor"
    else:
        output = "paper"

    return output









def index(req):

    score = Score.objects.create(player_score=0,ai_score=0)

    context = {
        "score":score
    }

    return render(req,"index.htm",context = context)
    

def rock(req):
    result = model()
    time.sleep(5)
    Lose_or_win = 0

    #결과를 계산한다
    if(result == "rock"):
        Lose_or_win = 2
    elif(result == "scissor"):
        Lose_or_win = 1
    elif(result == "paper"):
        Lose_or_win = 3

    #input data를 준비한다
    global  static_num
    data = InputData()
    data.num = static_num
    data.Player = "rock"
    data.ai = result
    data.Lose_or_Win = Lose_or_win
    data.save()

    #score에 반영한다
    score = Score.objects.order_by("-pk")[0]
    if(Lose_or_win == 1):
        score.player_score+=1
    if(Lose_or_win == 3):
        score.ai_score+=1
    score.save()

    # #결과를 csv에 추가한다
    f = open('RPS/data.csv','a',encoding='utf-8',newline='')
    wr = csv.writer(f)
    wr.writerow([static_num,"rock",Lose_or_win])
    f.close()

    static_num += 1


    context = {
        "score":score,
        "data":data
    }

    return render(req,"index.htm",context = context)

def scissor(req):
    result = model()
    time.sleep(5)
    Lose_or_win = 0

    # 결과를 계산한다
    if (result == "rock"):
        Lose_or_win = 3
    elif (result == "scissor"):
        Lose_or_win = 2
    elif (result == "paper"):
        Lose_or_win = 1

    # input data를 준비한다
    global static_num
    data = InputData()
    data.num = static_num
    data.Player = "scissor"
    data.ai = result
    data.Lose_or_Win = Lose_or_win
    data.save()

    # score에 반영한다
    score = Score.objects.order_by("-pk")[0]
    if (Lose_or_win == 1):
        score.player_score += 1
    if (Lose_or_win == 3):
        score.ai_score += 1
    score.save()

    # #결과를 csv에 추가한다
    f = open('RPS/data.csv', 'a', encoding='utf-8', newline='')
    wr = csv.writer(f)
    wr.writerow([static_num, "scissor", Lose_or_win])
    f.close()

    static_num += 1

    context = {
        "score": score,
        "data": data
    }

    return render(req, "index.htm", context=context)

def paper(req):
    result = model()
    time.sleep(5)
    Lose_or_win = 0

    # 결과를 계산한다
    if (result == "rock"):
        Lose_or_win = 1
    elif (result == "scissor"):
        Lose_or_win = 3
    elif (result == "paper"):
        Lose_or_win = 2

    # input data를 준비한다
    global static_num
    data = InputData()
    data.num = static_num
    data.Player = "paper"
    data.ai = result
    data.Lose_or_Win = Lose_or_win
    data.save()

    # score에 반영한다
    score = Score.objects.order_by("-pk")[0]
    if (Lose_or_win == 1):
        score.player_score += 1
    if (Lose_or_win == 3):
        score.ai_score += 1
    score.save()

    # #결과를 csv에 추가한다
    f = open('RPS/data.csv', 'a', encoding='utf-8', newline='')
    wr = csv.writer(f)
    wr.writerow([static_num, "paper", Lose_or_win])
    f.close()

    static_num += 1

    context = {
        "score": score,
        "data": data
    }

    return render(req, "index.htm", context=context)



