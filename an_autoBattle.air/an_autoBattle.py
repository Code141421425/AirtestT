# -*- encoding=utf8 -*-
__author__ = "Shang"

from airtest.core.api import *
import random

auto_setup(__file__)


####
#小米8se
#刘海向左
#2020/2/2
#zcw
####


#pos
pos = {
    "missonStart":[1979, 974],
    "missonIn":[1817, 748],
}


#基础数值
battleDuration = 180
battleSleep = 180




# 基础方法
def randomPos(tarPos = [500,500],scale = 3):
    variable = 0
    
    if scale == 1:
        variable = 20 #小图标用，技能图标的大小边长大概为100
    elif scale == 2:
        variable = 70 #长方形图标用，上下200，左右
    elif scale == 3:
        variable = 350
        pass
    finPos = [0,0]
    finPos[0] = tarPos[0]+random.randint(-variable,variable) 
    finPos[1] = tarPos[1]+random.randint(-variable,variable) 
    
    return finPos

def randomTime(tarTime,scale = 1,customTime = 0):
    variableTime = 0
    
    if scale == 1:
        variableTime = 0.5 #适用于战斗间隙（技能）
    elif scale == 2:
        variableTime = 6 #适用于长时间间隔（每面结束）
    elif scale == 3:
        variableTime = 5 #战斗结束
    elif scale == 99:
        variableTime = customTime
    
    tarTime = tarTime + random.uniform(-variableTime,variableTime)
    
    return tarTime

def w_battleFinish():
    wait(Template(r"tpl1580632302325.png", record_pos=(-0.321, 0.177), resolution=(2244, 1080)),timeout = battleSleep)

def w_battleIn():
    wait(Template(r"tpl1580632404494.png", record_pos=(0.351, 0.033), resolution=(2244, 1080)))

def s_shortSleep():
    sleep(randomTime(2.2,1))

def s_battle():
    sleep(battleDuration)
    w_battleFinish()
    

def missionStart():
    w_battleIn()
    touch(randomPos(pos["missonStart"],1))
    s_shortSleep()
    touch(randomPos(pos["missonIn"],1))
    
def battle():
    s_battle()
    w_battleFinish()
    
def missonFinish():
    w_battleFinish()
    sleep(randomTime(8,3))
    touch(randomPos())
    

def __main__():
    missionStart()
    battle()
    missonFinish()
    pass


for i in range(7):
    __main__()
    print("=============="+str(i)+"==============")