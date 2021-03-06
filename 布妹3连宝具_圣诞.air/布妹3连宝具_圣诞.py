# -*- encoding=utf8 -*-
__author__ = "Topjoy"

from airtest.core.api import *
import random

auto_setup(__file__)
           
    
#位置坐标记录
pos = {
    #其他系统按钮位置
    'p_missonIn':[1519, 340],
    'p_helpChoice':[910, 368],
    'p_missonStart':[910, 368],
    #战斗UI位置
    'masterSkill':[1890, 485],
    'actorChoice1':[594, 637],
    'attack':[1823, 903],
    'fin1':[500,500],
    'fin2':[500,500],
#     fin3:
    #技能位置
    'sk1_1':[208, 860],
    'sk1_3':[492, 860],
    'sk2_1':[686, 853],
    'sk2_2':[828, 853],
    'sk2_3':[965, 863],
    'sk3_1':[1171, 860],
    'sk3_2':[1303, 858],
    'sk3_3':[1444, 859],
    'skM_2':[1599, 460],
    #卡牌位置
    'pb1':[723, 286]
}

randomCirt = 60#随机释放技能的概率
randomAttackCrit = 30
randomSleepCrit = 5
attackPos = [[300, 729],[676, 721],[1081, 733],[1460, 725],[1848, 708]]


#技能释放顺序
skface1 = ["sk2_1","sk3_1","sk2_2"]
skface2 = ["skM_2","sk1_3","sk3_3"]
skface3 = ["sk3_2","sk2_3"]

#所有技能



class sk(object): 
    def sk1_1():
        touch(randomPos(pos["sk1_1"],1))#sk11
        s_SkipShort()

    def sk2_1():
        touch(randomPos(pos["sk2_1"],1))#sk21
        touch(randomPos(pos["actorChoice1"],1))#ac
        
        s_SkipShort()

    def sk3_1():    
        touch(randomPos(pos["sk3_1"],1))#sk31
        touch(randomPos(pos["actorChoice1"],1))#ac1
        s_SkipShort()
        
    def skM_2():
        touch(randomPos(pos["masterSkill"],1))#msk
        sleep(0.9)
        touch(randomPos(pos["skM_2"],1))#msk2
        touch(randomPos(pos["actorChoice1"]))#ac1
        s_SkipShort()
    
    def sk2_3():
        touch(randomPos(pos["sk2_3"]))#sk23
        touch(randomPos(pos["actorChoice1"]))#ac1
        s_SkipShort()
    
    def sk3_2():
        touch(randomPos(pos["sk3_2"]))#sk32
        s_SkipShort()
        
    def sk1_3():
        touch(randomPos(pos["sk1_3"],1))#sk13
        touch(randomPos(pos["actorChoice1"]))#atc
        s_SkipShort()
        
    def sk2_2():
        touch(randomPos(pos["sk2_2"]))#sk22
        s_SkipShort()
        
    def sk3_3():
        touch(randomPos(pos["sk3_3"]))#sk33
        touch(randomPos(pos["actorChoice1"]))#atc
        s_SkipShort()

#基础

def w_mainCity():
    try:
        wait(Template(r"tpl1579247357625.png", record_pos=(-0.242, -0.043), resolution=(2244, 1080)))
    except:
        return false
    else:
        pass

def w_attack():
    wait(Template(r"tpl1579233374423.png", record_pos=(0.306, 0.167), resolution=(2244, 1080)))

def w_finish():
    wait(Template(r"tpl1579234004588.png", record_pos=(-0.329, -0.117), resolution=(2244, 1080)))

def s_SkipShort():
    sleep(randomTime(3.2,1))
    
def s_turnEnd():
    sleep(randomTime(24,2))
    
def Attack():
    sleep(randomTime(2,1))
    
    touch(randomPos(pos["pb1"],1))#b1
    sleep(randomTime(1.2))
    randomAttackChoice()
    
    s_turnEnd()
    
def randomPos(tarPos,scale = 1):
    variable = 0
    
    if scale == 1:
        variable = 20 #小图标用，技能图标的大小边长大概为100
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

def randomAttackChoice():
    if randomIfRandom(randomAttackCrit):
        a = random.sample(attackPos,2)
    else:
        a = attackPos
        
    touch(randomPos(a[0]))
    touch(randomPos(a[1]))

def randomIfRandom(randomIn):
    rint = random.randint(0,100)
    
    if rint < randomIn:
        reslut = True
    else:
        reslut = False

    return reslut
    
     
#步骤
def missionIn():
    touch(randomPos(pos['p_missonIn'],1))
    sleep(3)
    try:
        wait(Template(r"tpl1579427939294.png", threshold=0.85, record_pos=(0.313, -0.217), resolution=(2244, 1080)),timeout = 4)
    except:
        wait(Template(r"tpl1579427986763.png", record_pos=(-0.02, -0.195), resolution=(2244, 1080)))
        touch(randomPos([1110, 473]))
        sleep(1.5)
        touch(randomPos([1381, 835]))
        sleep(3)


def helpChoice():
    wait(Template(r"tpl1579427939294.png", threshold=0.85, record_pos=(0.313, -0.217), resolution=(2244, 1080)))
    a = exists(Template(r"tpl1579246556618.png", threshold=0.85, record_pos=(-0.361, 0.028), resolution=(2244, 1080)))

    if a != False:#存在斯卡迪
        touch(randomPos(a,1))
    else:
        touch([1393, 198])#列表刷新
        sleep(1.5)
        touch([1381, 841])#
        touch(Template(r"tpl1579246556618.png", threshold=0.85, record_pos=(-0.361, 0.028), resolution=(2244, 1080)))


def missionStart():
    sleep(randomTime(2))
    touch(randomPos(exists(Template(r"tpl1579257639809.png", record_pos=(0.34, 0.208), resolution=(2244, 1080))),1))
    sleep(15)

def firstBattle():
    w_attack()
    
    if randomIfRandom(randomCirt):
        random.shuffle(skface1)    
    for func in skface1:
        getattr(sk,func)()
        
    touch(randomPos(pos["attack"],1))#atk
    Attack()

def secondBattle():
    w_attack()
    
    if randomIfRandom(randomCirt):
        random.shuffle(skface2)
    for func in skface2:
        getattr(sk,func)()
        
    touch(randomPos(pos["attack"]))#atk
    Attack()
    
def thirdBattle_T():
    w_attack()
    
    if randomIfRandom(randomCirt):
        random.shuffle(skface3)
    for func in skface3:
        getattr(sk,func)()

    touch(randomPos(pos["attack"]))#atk
    s_SkipShort()
    Attack()
    
def finish():
    w_finish()
    touch(randomPos(pos["fin2"],2))#t
    touch(randomPos(pos["fin2"],2))#t
    sleep(randomTime(2.5))#
    touch(randomPos(pos["fin2"],2))#t
    sleep(randomTime(2.2))
    touch(Template(r"tpl1579234188020.png", record_pos=(0.283, 0.209), resolution=(2244, 1080)))#tnx #卡点#
    sleep(randomTime(20,3))
    
def newFriednAdd():
    try:
        w_mainCity()
    except:
        exists(Template(r"tpl1579326259995.png", record_pos=(-0.027, -0.098), resolution=(2244, 1080)))
        touch(Template(r"tpl1579326288526.png", record_pos=(-0.23, 0.168), resolution=(2244, 1080)))
    

           
def __main__():
    #appIn()
#     missionIn()
#     helpChoice()
    missionStart()
    firstBattle()
    secondBattle()
    thirdBattle_T()
    finish()
#    newFriednAdd()


def __test__():
#     print(skface1List)
#     random.shuffle(skface1List)
#     for func in skface1List:
#         getattr(sk,func)()
#     print(skface1List)
    #helpChoice()
    #print(randomTime(5,))
#     newFriednAdd()
#   Attack()
    pass

__main__()
#__test__()

##设置
# for i in range(2):
#     __main__()
#     print("====================="+str(i)+"=====================")
