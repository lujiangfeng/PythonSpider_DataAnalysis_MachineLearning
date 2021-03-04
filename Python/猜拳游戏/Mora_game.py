import turtle
import random
myscreen = turtle.Screen()
# 计数
count = 0
#局数
num = 10 
# 玩家，电脑，平局，作废
p_win,c_win,h_win,f_win = 0,0,0,0
# 出拳列表
player = ['剪刀','石头','布']
# 玩家胜利的3种组合，嵌套列表实现
winer = [['石头','剪刀'],['剪刀','布'],['布','石头']]
while count<num:
    count = count+1
    # 电脑，随机生成一个值
    computer_player = random.choice(player)
    # 玩家，在对话框中输入剪刀石头布
    single_player = myscreen.textinput('猜拳游戏', '请输入对应的名称：石头 剪刀 布：')
    # 玩家，输入错误
    if single_player not in player:
        print('您输错了，第【%s】局作废，视为您放弃此局，电脑获胜'%(count),
        '还剩【%s】局'%(num-count))
    else:
        # 输出出拳情况
        print('第【%s】局'%(count),
        '玩家出了',single_player,
        '，电脑出了',computer_player)  
        # 判断玩家出拳列表，是否在玩家出拳胜利的嵌套列表中
        if [single_player,computer_player] in winer:
            print('你获胜了')
            p_win = p_win +1
        # 是否平局
        elif single_player == computer_player:   
            print('平局') 
            h_win = h_win +1
        else:
            c_win = c_win +1
            print('电脑获胜了')
        f_win =num-(p_win + c_win + h_win)  
        print('截至到第【%s】局'%(count),
            '玩家赢了【%s】局'%(p_win),
            '电脑赢了【%s】局'%(c_win+f_win),
            '平局【%s】局'%(h_win))
        print('*' * 50)
turtle.done()
