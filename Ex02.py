# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 19:04:26 2022

@author: watson
"""

#format  格式化

#{}  依照位置放
print("今天有{}人，劃圓，半徑為：{}，在{}分鐘完成".format(100,5.88,10))

msg = "{}銀行於今日放款利率為：{}".format("聯成",0.111)

print(msg)

# 0   表示位置
msg = "{0}學生於今日獲獎，學校特別頒發獎金給{0}，獎金共{1}元".format("張惠妹",600)
                                                                #   0       1                                                                
print(msg)                                                                

# {位置:格式}
msg = "今天領了{:,}元，銀行利率為：{:.2f}".format(1000000,3.14159)

print(msg)

# 5.2f   長度最少5個，取到小數第二位

msg = "今天領了{0:,}，利率：{1:5.2f}, 姐姐將{0:,}元統統拿走".format(1000000,3.14159)

print(msg)

msg = "今天領了{0:,}，利率：{1:10.2f}, 姐姐將{0:,}元統統拿走".format(1000000,3.14159)

print(msg)

print("{}".format("Hello"))
print("{:<20}".format("Hello"))  # < 向左對齊
print("{:>20}".format("Hello"))  # > 向右對齊
print("{:^20}".format("Hello"))  # ^ 置中

print("分數：{:3d}".format(2))




