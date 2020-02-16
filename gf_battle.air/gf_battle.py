# -*- encoding=utf8 -*-
__author__ = "Shang"

from airtest.core.api import *

auto_setup(__file__)
import random 

####
#夜神模拟器
#1280*720
#2020/2/1
#zcw
####


pos = {
    "qihuiqiIII":[441, 389],
    
    "hq":[635, 359],
    "airport1":[272, 226],
    "airport2":[62, 384],
    "pos1":[447, 300],
    "pos2":[631, 545],
    "pos3":[462, 692],
    "pos4":[349, 558],
    
    "plan":[66, 590],
    
    "random1":[1164, 366],
    
}

battleDuration = 240


# 基础方法
def randomPos(tarPos,scale = 1):
    variable = 0
    
    if scale == 1:
        variable = 10 #小图标用，技能图标的大小边长大概为100
    elif scale == 2:
        variable = 70 #长方形图标用，上下200，左右
    elif scale == 3:
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
        variableTime = 8 #战斗结束
    elif scale == 99:
        variableTime = customTime
    
    tarTime = tarTime + random.uniform(-variableTime,variableTime)
    
    return tarTime



#
def mainCity():
    wait(Template(r"tpl1581392598891.png", record_pos=(0.312, 0.002), resolution=(1280, 720)))

def addMember():
    touch(Template(r"tpl1581393335334.png", record_pos=(0.405, 0.219), resolution=(1280, 720)))
    
def touchPos(posid):
    touch(randomPos(pos[posid],1))
    s_sleepShort()
    
def t_oppositePos(localPos,relativeNumber):
    pass
#     if relativeNumber ==1:
#         temp = localPos
#         temp[0] = 
#         touch(randomPos(pos[local],1)
    
def t_PosList():
    pass
    
def s_sleepShort():
    sleep(randomTime(1.6,1))
    
def s_sleepMiddle():
    sleep(randomTime(5.5,1))


#
def missonIn():
    mainCity()
    touch(Template(r"tpl1581392567047.png", record_pos=(0.354, 0.139), resolution=(1280, 720)))
    pass
    

def battlePrepare():
    touchPos("hq")
    s_sleepShort()
    addMember()
    s_sleepShort()
    
    touchPos("airport1")
    s_sleepShort()
    addMember()
    s_sleepShort()    
    
    touch(Template(r"tpl1581393825759.png", record_pos=(0.384, 0.23), resolution=(1280, 720)))
    s_sleepMiddle()


def battlePathSet():
    touchPos("plan")
    touchPos("airport1")
    touchPos("airport2")
    touchPos("hq")
    touch([727, 362])#相对选择1
    touchPos("pos1")
    touchPos("pos2")
    touchPos("pos3")
    
    touchPos("airport1")
    touch([355, 217])
    touchPos("pos4")
    
    touch(Template(r"tpl1581587967208.png", record_pos=(0.425, 0.228), resolution=(1280, 720)))

    
    pass
    
def s_Battle(times):
    sleep(times)
    pass
    
def battleFinish():
    wait(Template(r"tpl1581394727624.png", record_pos=(-0.278, -0.155), resolution=(1280, 720)),timeout= 80)
    s_sleepShort()
    sleep(2)
    touchPos("random1")#出角色
    s_sleepMiddle()
    touchPos("random1")#关角色
    s_sleepMiddle
    touchPos("random1")#[1164, 366] 随记位置100 *2
    s_sleepShort()
    touchPos("random1")
    
              
    pass
    
def reStart():
    wait(Template(r"tpl1581592298002.png", record_pos=(-0.315, -0.24), resolution=(1280, 720)))
    touch(randomPos(pos["qihuiqiIII"],1))
    sleep(randomTime(1.6,1))
    touch(Template(r"tpl1581392815027.png", record_pos=(0.392, 0.059), resolution=(1280, 720)))
    s_sleepMiddle()




#流程开始

def __main__():
    #missonIn()
    
    for i in range(7):
        reStart()
        battlePrepare()
        battlePathSet()
        s_Battle(battleDuration)
        battleFinish()
#         reStart()
    

def __test__():
    print(touch(Template(r"tpl1581393825759.png", record_pos=(0.384, 0.23), resolution=(1280, 720))))

    
    
__main__()
#__test__()



