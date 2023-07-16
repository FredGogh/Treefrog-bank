#-*-coding:utf-8 -*-
#连接数据库
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import pymysql as mdb
import datetime
import calendar

conn = mdb.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    db='treefrog_bank',
    charset='utf8'
    )
print("###已连接数据库treefrog_bank.###")

#当前用户
user_id = 0
#是否使用信用卡
var1 = 0
#初始界面
def initial():
    window = tk.Tk()
    window.title('TreeFrog Bank')
    window.geometry('430x330')
    l = tk.Label(window, 
        text='用户登录',
        font=('方正粗黑宋简体', 20),
        width=15, height=2)
    l.place(x=85,y=50)
    tk.Label(window, text='用户名: ').place(x=50, y= 150)
    tk.Label(window, text='密码: ').place(x=50, y= 190)
    entry_id = tk.Entry(window)
    entry_id.place(x=160, y=150)
    entry_pwd = tk.Entry(window,show='*')
    entry_pwd.place(x=160, y=190)
    #登录
    def login():
        global user_id
        cursor = conn.cursor()
        customer_id = entry_id.get()
        customer_pwd = entry_pwd.get()
        if(customer_id == ""):
            #未输入用户名
            tk.messagebox.showinfo(title="输入错误", message="请输入用户名")
        elif(customer_pwd == ""):
            #未输入密码
            tk.messagebox.showinfo(title="输入错误", message="请输入密码")
        else:
            #获取密码
            customer_pwd = int(customer_pwd)
            SQL = """select customer_pwd
                         from customers
                         where customer_id = {};
                         """.format(customer_id)
            cursor.execute(SQL)
            conn.commit()
            c = cursor.fetchall()
            if (len(c) != 0):
                #用户名存在
                if(customer_pwd == c[0][0]):
                    #登录成功，将用户设为当前登录用户，并进入主菜单
                    user_id = customer_id
                    print(customer_id)
                    window.withdraw()
                    user_main()
                else:
                    #密码错误
                    tk.messagebox.showinfo(title="输入错误", message="用户名或密码错误")
            else:
                #用户名不存在
                tk.messagebox.showinfo(title="输入错误", message="用户名或密码错误")
    btn_login = tk.Button(window, text='登录',width = 20, command=login)
    btn_login.place(x=120, y=230)
    btn_sign_up = tk.Button(window, text='注册',width = 20, command=signup)
    btn_sign_up.place(x=120, y=270)

#用户主界面
def user_main():
    print("用户主界面")
    window = tk.Tk()
    window.title('TreeFrog Bank - HomePage')
    window.geometry('450x700')
    l = tk.Label(window, 
        text='你好，用户{}.\n请选择功能:'.format(user_id),
        font=('方正粗黑宋简体', 20),
        width=15, height=2)
    l.place(x=20,y=20)
    
    def todeposit():
        window.withdraw()
        deposit()
    def towithdraw():
        window.withdraw()
        withdraw()
    def toloan():
        window.withdraw()
        loan()
    def toloan_repay():
        window.withdraw()
        loan_repay()
    def tocreditcard_repay():
        window.withdraw()
        creditcard_repay()
    def totransfer():
        window.withdraw()
        transfer()
    def tosearch_menu():
        window.withdraw()
        search_menu()
    def toanalyse():
        window.withdraw()
        analyse()
    def tosearch_loans():
        window.withdraw()
        search_loans()
    def tosearch_basicinfo():
        window.withdraw()
        search_basicinfo()
    def tosearch_info():
        window.withdraw()
        search_info()
    def tochange_pwd():
        window.withdraw()
        change_pwd()
    def logout():   
        window.withdraw()
        user = 0
        initial()
        
    btn_deposit = tk.Button(window, text='存款',width = 20, command=todeposit)
    btn_deposit.place(x = 160,y = 120)
    btn_withdraw = tk.Button(window, text='取款',width = 20, command=towithdraw)
    btn_withdraw.place(x = 160,y = 160)
    btn_loan = tk.Button(window, text='贷款',width = 20, command=toloan)
    btn_loan.place(x = 160,y = 200)
    btn_loan_repay = tk.Button(window, text='贷款还款',width = 20, command=toloan_repay)
    btn_loan_repay.place(x = 160,y = 280)
    btn_creditcard_repay = tk.Button(window, text='信用卡还款',width = 20, command=tocreditcard_repay)
    btn_creditcard_repay.place(x = 160,y = 320)
    btn_transfer = tk.Button(window, text='交易',width = 20, command=totransfer)
    btn_transfer.place(x = 160,y = 240)
    btn_search_transfer = tk.Button(window, text='查询交易记录',width = 20, command=tosearch_menu)
    btn_search_transfer.place(x = 160,y = 360)
    btn_analyse = tk.Button(window, text='交易统计分析',width = 20, command=toanalyse)
    btn_analyse.place(x = 160,y = 400)
    btn_change_pwd = tk.Button(window, text='查询贷款信息',width = 20, command=tosearch_loans)
    btn_change_pwd.place(x = 160,y = 440)
    btn_search_info = tk.Button(window, text='查询基本信息',width = 20, command=tosearch_basicinfo)
    btn_search_info.place(x = 160,y = 480)
    btn_search_info = tk.Button(window, text='查询个人信息',width = 20, command=tosearch_info)
    btn_search_info.place(x = 160,y = 520)
    btn_change_pwd = tk.Button(window, text='维护个人信息',width = 20, command=tochange_pwd)
    btn_change_pwd.place(x = 160,y = 560)
    btn_logout = tk.Button(window, text='退出',width = 20, command=logout)
    btn_logout.place(x = 160,y = 600)
    
#注册界面
def signup():
    print("注册界面")
    window_signup = tk.Tk()
    window_signup.title('TreeFrog Bank - Signup')
    window_signup.geometry('420x330')
    l = tk.Label(window_signup, 
        text='用户注册',
        font=('方正粗黑宋简体', 20),
        width=15, height=2)
    l.place(x=70,y=10)
    tk.Label(window_signup, text='姓名: ').place(x=50, y= 80)
    entry_name = tk.Entry(window_signup)
    entry_name.place(x=160,y=80)
    tk.Label(window_signup, text='密码: ').place(x=50, y= 120)
    entry_pwd = tk.Entry(window_signup)
    entry_pwd.place(x=160,y=120)
    tk.Label(window_signup, text='确认密码: ').place(x=50, y= 160)   
    entry_confirmpwd = tk.Entry(window_signup)
    entry_confirmpwd.place(x=160,y=160)
    tk.Label(window_signup, text='客户种类: ').place(x=50, y= 200)
    entry_type = tk.Entry(window_signup)
    entry_type.place(x=160,y=200)
    def signupdone():
        name = entry_name.get()
        pwd = entry_pwd.get()
        confirmpwd = entry_confirmpwd.get()
        usertype = entry_type.get()
        if(name == ""):
            #未输入姓名
            tk.messagebox.showinfo(title="输入错误", message="请输入姓名")
        elif(pwd == ""):
            #未输入密码
            tk.messagebox.showinfo(title="输入错误", message="请输入密码")
        elif(confirmpwd == ""):
            #未输入确认密码
            tk.messagebox.showinfo(title="输入错误", message="请输入确认密码")
        elif(usertype == ""):
            #未输入客户种类
            tk.messagebox.showinfo(title="输入错误", message="请输入客户种类")
        elif(pwd != confirmpwd):
            #两次输入密码不一致
            tk.messagebox.showinfo(title="输入错误", message="两次输入密码不一致")
        else:
            pwd = eval(pwd)
            confirmpwd = eval(confirmpwd)
            creditlimit = 0
            loanlimit = 0
            if(usertype == 'A'):
                #A类客户
                creditlimit = 25000
                loanlimit = 2500000
            if(usertype == 'B'):
                #B类客户
                creditlimit = 18000
                loanlimit = 1800000
            if(usertype == 'C'):
                #C类客户
                creditlimit = 13000
                loanlimit = 1300000
            if(usertype == 'D'):
                #D类客户
                creditlimit = 10000
                loanlimit = 1000000
            cursor = conn.cursor()
            #注册用户，插入客户表
            SQL = """insert into customers(customer_name,customer_pwd,customer_type,customer_lendingrate,customer_creditlimit,customer_loanlimit)
                      values("{}",{},'{}',{},{},{})
                         """.format(name,pwd,usertype,0.045,creditlimit,loanlimit)
            cursor.execute(SQL)
            conn.commit()
            tk.messagebox.showinfo(title="注册完成", message="注册完成")
            window_signup.withdraw()
    
    btn_signupdone = tk.Button(window_signup, text='注册',width = 20, command=signupdone)
    btn_signupdone.place(x=120, y=240)
    #返回按钮
    def back():
        window_signup.withdraw()
        initial()    
    btn_back = tk.Button(window_signup, text='返回',width = 20, command=back)
    btn_back.place(x=120, y=280)


#存款
def deposit():
    print("deposit")
    window = tk.Tk()
    window.title('TreeFrog Bank - Deposit Page')
    window.geometry('450x300')
    l = tk.Label(window, 
        text='存款',
        font=('方正粗黑宋简体', 20),
        width=15, height=2)
    l.place(x=50,y=20)
    tk.Label(window, text='存款金额: ').place(x=70, y= 120)
    entry_amount = tk.Entry(window)
    entry_amount.place(x=150,y=120)
    tk.Label(window, text='密码: ').place(x=70, y= 160)
    entry_pwd = tk.Entry(window,show = '*')
    entry_pwd.place(x=150,y=160)
    def depositdone():
        if(entry_amount.get() == ""):
            #未输入金额
            tk.messagebox.showinfo(title="输入错误", message="请输入存款金额")
        elif(entry_pwd.get() == ""):
            #未输入密码
            tk.messagebox.showinfo(title="输入错误", message="请输入密码")
        else:
            global user_id
            amount = eval(entry_amount.get())
            pwd = eval(entry_pwd.get())
            cursor = conn.cursor()
            SQL = """select customer_pwd,customer_balance
                    from customers
                    where customer_id = {};
                         """.format(user_id)
            cursor.execute(SQL)
            conn.commit()
            c = cursor.fetchall()
            balance = c[0][1]
            if(pwd == c[0][0]):
                #增加账户余额
                SQL2 = """update customers
                    set customer_balance = {}
                    where customer_id = {};
                         """.format(balance+amount,user_id)
                cursor.execute(SQL2)
                #记录存款
                SQL3 = """
                    insert into deposits(customer_id,deposit_amount)
                    values({},{});
                    """.format(user_id,amount)
                cursor.execute(SQL3)
                conn.commit()
                window.withdraw()
                user_main()
            else:
                #密码错误
                tk.messagebox.showinfo(title="密码错误", message="密码错误")
    btn_depositdone = tk.Button(window, text='存款',width = 20, command=depositdone)
    btn_depositdone.place(x=120, y=200)
    #返回按钮
    def back():
        window.withdraw()
        user_main()    
    btn_back = tk.Button(window, text='返回',width = 20, command=back)
    btn_back.place(x=120, y=250)



#取款
def withdraw():
    print("withdraw")
    window = tk.Tk()
    window.title('TreeFrog Bank - Withdraw Page')
    window.geometry('450x300')
    l = tk.Label(window, 
        text='取款',
        font=('方正粗黑宋简体', 20),
        width=15, height=2)
    l.place(x=50,y=20)
    tk.Label(window, text='取款金额: ').place(x=70, y= 120)
    entry_amount = tk.Entry(window)
    entry_amount.place(x=150,y=120)
    tk.Label(window, text='密码: ').place(x=70, y= 160)
    entry_pwd = tk.Entry(window,show = '*')
    entry_pwd.place(x=150,y=160)
    def withdrawdone():
        if(entry_amount.get() == ""):
            #未输入取款金额
            tk.messagebox.showinfo(title="输入错误", message="请输入取款金额")
        elif(entry_pwd.get() == ""):
            #未输入密码
            tk.messagebox.showinfo(title="输入错误", message="请输入密码")
        else:
            global user_id
            amount = eval(entry_amount.get())
            pwd = eval(entry_pwd.get())
            cursor = conn.cursor()
            SQL = """select customer_pwd,customer_balance
                    from customers
                    where customer_id = {};
                         """.format(user_id)
            cursor.execute(SQL)
            conn.commit()
            c = cursor.fetchall()
            balance = c[0][1]
            if(pwd == c[0][0]):
                if(balance < amount):
                    #余额不足
                    tk.messagebox.showinfo(title="余额不足", message="余额不足")
                else:
                    #扣除账户余额
                    SQL2 = """update customers
                        set customer_balance = {}
                        where customer_id = {};
                             """.format(balance-amount,user_id)
                    cursor.execute(SQL2)
                    #记录取款
                    SQL3 = """
                        insert into withdraws(customer_id,withdraw_amount)
                        values({},{});
                    """.format(user_id,amount)
                    cursor.execute(SQL3)
                    conn.commit()
                    window.withdraw()
                    user_main()
            else:
                #密码错误
                tk.messagebox.showinfo(title="密码错误", message="密码错误")

    btn_depositdone = tk.Button(window, text='取款',width = 20, command=withdrawdone)
    btn_depositdone.place(x=120, y=200)
    #返回按钮
    def back():
        window.withdraw()
        user_main()    
    btn_back = tk.Button(window, text='返回',width = 20, command=back)
    btn_back.place(x=120, y=250)

#贷款
def loan():
    print("loan")
    window = tk.Tk()
    window.title('TreeFrog Bank - Loan Page')
    window.geometry('450x300')
    l = tk.Label(window, 
        text='贷款',
        font=('方正粗黑宋简体', 20),
        width=15, height=2)
    l.place(x=50,y=15)
    tk.Label(window, text='贷款金额: ').place(x=70, y= 80)
    entry_amount = tk.Entry(window)
    entry_amount.place(x=150,y=80)
    tk.Label(window, text='贷款年限: ').place(x=70, y= 120)
    entry_term = tk.Entry(window)
    entry_term.place(x=150,y=120)
    tk.Label(window, text='密码: ').place(x=70, y= 160)
    entry_pwd = tk.Entry(window,show = '*')
    entry_pwd.place(x=150,y=160)
    def withdrawdone():
        if(entry_amount.get() == ""):
            #未输入贷款金额
            tk.messagebox.showinfo(title="输入错误", message="请输入贷款金额")
        elif(entry_term.get() == ""):
            #未输入贷款年限
            tk.messagebox.showinfo(title="输入错误", message="请输入贷款年限")
        elif(entry_pwd.get() == ""):
            #未输入密码
            tk.messagebox.showinfo(title="输入错误", message="请输入密码")
        elif(int(entry_term.get())>25):
            #超过最高年限25年
            tk.messagebox.showinfo(title="输入错误", message="贷款年限超过最高年限25年")
        else:
            global user_id
            amount = eval(entry_amount.get())
            term = eval(entry_term.get())
            pwd = eval(entry_pwd.get())
            cursor = conn.cursor()
            SQL = """select customer_pwd,customer_loanlimit,customer_loaned,customer_balance
                    from customers
                    where customer_id = {};
                         """.format(user_id)
            cursor.execute(SQL)
            conn.commit()
            c = cursor.fetchall()
            limit = c[0][1]
            loaned = c[0][2]
            balance = c[0][3]
            if(pwd == c[0][0]):
                if(limit-loaned < amount):
                    tk.messagebox.showinfo(title="额度不足", message="贷款额度不足")
                else:
                    #增加已借贷款和账户余额
                    SQL2 = """update customers
                        set customer_loaned = {},customer_balance = {}
                        where customer_id = {};
                             """.format(loaned+amount,balance+amount,user_id)
                    cursor.execute(SQL2)
                    conn.commit()
                    #记录贷款   
                    SQL3 = """insert into loans(customer_id,loan_amount,loan_term)
                              values({},{},{});
                           """.format(user_id,amount,term)
                    cursor.execute(SQL3)
                    window.withdraw()
                    user_main()
            else:
                tk.messagebox.showinfo(title="密码错误", message="密码错误")

    btn_depositdone = tk.Button(window, text='贷款',width = 20, command=withdrawdone)
    btn_depositdone.place(x=120, y=200)
    def back():
        window.withdraw()
        user_main()    
    btn_back = tk.Button(window, text='返回',width = 20, command=back)
    btn_back.place(x=120, y=250)

#贷款还款
def loan_repay():
    print("loan_repay")
    window = tk.Tk()
    window.title('TreeFrog Bank - Loan Repayment Page')
    window.geometry('450x330')
    l = tk.Label(window, 
        text='贷款还款',
        font=('方正粗黑宋简体', 20),
        width=15, height=2)
    l.place(x=50,y=20)
    
    cursor = conn.cursor()
    SQL = """select loan_amount,loan_term,loan_id
            from loans
            where customer_id = {} and loan_repayed = false;
            """.format(user_id)
    cursor.execute(SQL)
    conn.commit()
    c = cursor.fetchall()
    number = len(c)
    #各贷款应还金额
    topay = []
    #应还总额
    topay_total = 0
    #贷款编号
    loan_id = []
    #贷款期限
    loan_term = []
    #贷款总额
    loan_amount = []
    #已还年限
    payed_months = []
    if(len(c) != 0):
        for i in c:
            loan_id.append(i[2])
            SQL6 = """select *
                      from loan_repayments
                      where loan_id = {}
                   """.format(i[2])
            cursor.execute(SQL6)
            conn.commit()
            c2 = cursor.fetchall()
            months = len(c2)
            #各笔贷款应还金额
            topay.append((i[0]/(i[1]*12))+(0.045/12)*(i[0]-months*i[0]/(i[1]*12)))
            #总应还金额
            topay_total += (i[0]/(i[1]*12))+(0.045/12)*(i[0]-months*i[0]/(i[1]*12))
            loan_term.append(i[1])
            loan_amount.append(i[0])
            payed_months.append(months)
                         
    now = datetime.datetime.now()
    month_start = datetime.datetime(now.year,now.month,1).strftime('%Y-%m-%d %H:%M:%S')
    month_end = this_month_end = datetime.datetime(now.year, now.month, calendar.monthrange(now.year, now.month)[1]).strftime('%Y-%m-%d %H:%M:%S')
    SQL2 = """select loan_id
            from loan_repayments
            where customer_id = {} and loan_repayment_time between '{}' and '{}';
            """.format(user_id,month_start,month_end)
    cursor.execute(SQL2)
    conn.commit()
    c = cursor.fetchall()
    payed = len(c)
    payed_id = []
    if(len(c) != 0):
        for i in c:
            payed_id.append(i[0])            
    
    tk.Label(window, text='本月贷款应还：').place(x=70, y=120)
    tk.Label(window, text='{}项\t{}元'.format(number,topay_total)).place(x=150, y=120)
    tk.Label(window, text='本月还款状态：').place(x=70, y=160)
    tk.Label(window, text='已还{}项'.format(payed)).place(x=150, y=160)
    tk.Label(window, text='密码: ').place(x=70, y= 200)
    entry_pwd = tk.Entry(window,show = '*')
    entry_pwd.place(x=150,y=200)
    def repaydone():
        cursor = conn.cursor()
        SQL3 = """select customer_pwd,customer_balance,customer_loaned
                from customers
                where customer_id = {};
               """.format(user_id)
        cursor.execute(SQL3)
        conn.commit()
        c = cursor.fetchall()
        pwd = c[0][0]
        balance = c[0][1]
        customer_loaned = c[0][2]
        if(entry_pwd.get() == ""):
            tk.messagebox.showinfo(title="输入错误", message="请输入密码")
        elif(pwd != eval(entry_pwd.get())):
            tk.messagebox.showinfo(title="密码错误", message="密码错误")
        elif(payed == len(topay)):
            tk.messagebox.showinfo(title="无需还款", message="本月已还款或无贷款")
        elif(topay_total > balance):
            tk.messagebox.showinfo(title="余额不足", message="余额不足")
        else:
            for i in range(len(topay)):
                cursor = conn.cursor()
                #记录还款
                SQL4 = """insert into loan_repayments(loan_id,customer_id,loan_repayment_amount)
                        values({},{},{});
                        """.format(loan_id[i],user_id,topay[i])
                cursor.execute(SQL4)
                conn.commit()
                #扣除余额
                SQL5 = """update customers
                          set customer_balance = {}
                           where customer_id = {};
                        """.format(balance - topay[i],user_id)
                cursor.execute(SQL5)
                conn.commit()
             #偿清检查
            for i in range(len(loan_id)):
                if(payed_months[i] == loan_term[i]):
                    #在贷款表中将该笔贷款标为已还
                    SQL7 = """update loans
                              set repayed = true
                              from loan_repayments
                              where loan_id = {};
                            """.format(loan_id[i])
                    cursor.execute(SQL7)
                    conn.commit()
                    #减少已借贷款
                    SQL8 = """update customers
                              set loaned = {}
                              where customer_id = {};
                            """.format(customer_loaned - loan_amount[i],user_id)
                    cursor.execute(SQL8)
                    conn.commit()
            window.withdraw()
            user_main()
        
    btn_repaydone = tk.Button(window, text='还款',width = 20, command=repaydone)
    btn_repaydone.place(x=120, y=240)
    #返回按钮
    def back():
        window.withdraw()
        user_main()    
    btn_back = tk.Button(window, text='返回',width = 20, command=back)
    btn_back.place(x=120, y=280)

#交易
def transfer():
    print("transfer")
    window = tk.Tk()
    window.title('TreeFrog Bank - Transfer Page')
    window.geometry('450x450')
    l = tk.Label(window, 
        text='交易',
        font=('方正粗黑宋简体', 20),
        width=15, height=2)
    l.place(x=50,y=20)
    tk.Label(window, text='交易金额: ').place(x=70, y= 120)
    entry_amount = tk.Entry(window)
    entry_amount.place(x=150,y=120)
    tk.Label(window, text='收款方: ').place(x=70, y= 160)
    entry_receiver = tk.Entry(window)
    entry_receiver.place(x=150,y=160)
    tk.Label(window, text='交易种类: ').place(x=70, y= 200)
    entry_type = tk.Entry(window)
    entry_type.place(x=150,y=200)
    tk.Label(window, text='密码: ').place(x=70, y= 240)
    entry_pwd = tk.Entry(window,show = '*')
    entry_pwd.place(x=150,y=240)

    #修改是否使用信用卡
    def check():
        global var1
        if(var1 == 0):
            var1 = 1
        else:
            var1 = 0
    cb_creditcard = ttk.Checkbutton(window, text="使用信用卡",command = check,variable = var1)
    cb_creditcard.place(x=70,y=280)
    
    #开始交易
    def tranferdone():
        cursor = conn.cursor()
        SQL = """select customer_pwd,customer_balance,customer_creditloaned,customer_creditlimit
                from customers
                where customer_id = {};
               """.format(user_id)
        cursor.execute(SQL)
        conn.commit()
        c = cursor.fetchall()
        pwd = c[0][0]
        balance = c[0][1]
        loaned = c[0][2]
        limit = c[0][3]
        
        print("transferdone")
        if(entry_amount.get() == ""):
            tk.messagebox.showinfo(title="输入错误", message="请输入交易金额")
        elif(entry_receiver.get() == ""):
            tk.messagebox.showinfo(title="输入错误", message="请输入收款方")
        elif(entry_type.get() == ""):
            tk.messagebox.showinfo(title="输入错误", message="请输入交易种类")
        elif(entry_pwd.get() == ""):
            tk.messagebox.showinfo(title="输入错误", message="请输入密码")
        elif(pwd != eval(entry_pwd.get())):
            tk.messagebox.showinfo(title="密码错误", message="密码错误")
        else:
            amount = eval(entry_amount.get())
            receiver = eval(entry_receiver.get())
            catagory = entry_type.get()
            cursor = conn.cursor()
            SQL = """select *
                from customers
                where customer_id = {};
               """.format(receiver)
            cursor.execute(SQL)
            conn.commit()
            c = cursor.fetchall()
            if(len(c)==0):
                tk.messagebox.showinfo(title="输入错误", message="收款方不存在")
            else:
                #现金交易
                if(var1 == 0):
                    if(amount > balance):
                        tk.messagebox.showinfo(title="余额不足", message="余额不足")
                    else:
                        #记录交易
                        cursor = conn.cursor()
                        SQL = """insert into transfers(sender_id,receiver_id,transfer_amount,transfer_creditcard,transfer_catagory)
                                 values({},{},{},false,"{}")
                            """.format(user_id,receiver,amount,catagory)
                        cursor.execute(SQL)
                        conn.commit()
                        #扣除付款方余额
                        SQL2 = """update customers
                                  set customer_balance = {}
                                  where customer_id = {}
                            """.format(balance - amount,user_id)
                        cursor.execute(SQL2)
                        conn.commit()
                        #增加收款方余额
                        SQL3 = """select customer_balance
                        from customers
                        where customer_id = {};
                        """.format(receiver)
                        cursor.execute(SQL3)
                        conn.commit()
                        c = cursor.fetchall()
                        receiver_balance = c[0][0]
                        SQL4 = """update customers
                                  set customer_balance = {}
                                  where customer_id = {}
                        """.format(receiver_balance + amount,receiver)
                        cursor.execute(SQL4)
                        conn.commit()
                        window.withdraw()
                #信用卡交易
                else:
                    if(amount > limit - loaned):
                        print("信用卡额度不足")
                    else:
                        #记录交易
                        cursor = conn.cursor()
                        SQL = """insert into transfers(sender_id,receiver_id,transfer_amount,transfer_creditcard,transfer_catagory)
                                 values({},{},{},true,"{}")
                            """.format(user_id,receiver,amount,catagory)
                        cursor.execute(SQL)
                        conn.commit()
                        #增加付款方信用卡欠款
                        SQL2 = """update customers
                                  set customer_creditloaned = {}
                                  where customer_id = {}
                            """.format(loaned + amount,user_id)
                        cursor.execute(SQL2)
                        conn.commit()
                        #增加收款方余额
                        SQL3 = """select customer_balance
                        from customers
                        where customer_id = {};
                        """.format(receiver)
                        cursor.execute(SQL3)
                        conn.commit()
                        c = cursor.fetchall()
                        receiver_balance = c[0][0]
                        SQL4 = """update customers
                                  set customer_balance = {}
                                  where customer_id = {}
                        """.format(receiver_balance + amount,receiver)
                        cursor.execute(SQL4)
                        conn.commit()
                        window.withdraw()
                
    btn_transferdone = tk.Button(window, text='交易',width = 20, command=tranferdone)
    btn_transferdone.place(x=120, y=320)
    
    #返回
    def back():
        window.withdraw()
        user_main()
    btn_back = tk.Button(window, text='返回',width = 20, command=back)
    btn_back.place(x=120, y=360)
    window.mainloop()
    
#信用卡还款
def creditcard_repay():
    print("creditcard_repay")
    window = tk.Tk()
    window.title('TreeFrog Bank - Creditcard Repayment Page')
    window.geometry('450x300')
    l = tk.Label(window, 
        text='信用卡还款',
        font=('方正粗黑宋简体', 20),
        width=15, height=2)
    l.place(x=50,y=20)
    cursor = conn.cursor()
    SQL = """select customer_creditloaned,customer_pwd,customer_balance
             from customers
             where customer_id = {};
          """.format(user_id)
    cursor.execute(SQL)
    conn.commit()
    c = cursor.fetchall()
    topay = c[0][0]
    pwd = c[0][1]
    balance = c[0][2]
    tk.Label(window, text='本月信用卡应还：').place(x=70, y=120)
    tk.Label(window, text='{}元'.format(topay)).place(x=180, y=120)
    tk.Label(window, text='密码: ').place(x=70, y= 160)
    entry_pwd = tk.Entry(window,show = '*')
    entry_pwd.place(x=150,y=160)

    def creidtrepaydone():
        print("creidtrepaydone")
        if(entry_pwd.get() == ""):
            tk.messagebox.showinfo(title="输入错误", message="请输入密码")
        elif(pwd != eval(entry_pwd.get())):
            tk.messagebox.showinfo(title="密码错误", message="密码错误")
        else:
            if(balance < topay):
                tk.messagebox.showinfo(title="余额不足", message="余额不足")
            else:
                #扣除余额
                cursor = conn.cursor()
                SQL = """update customers
                         set customer_balance = {}
                         where customer_id = {}
                      """.format(balance - topay,user_id)
                cursor.execute(SQL)
                conn.commit()
                #清空欠款
                SQL2 = """update customers
                          set customer_creditloaned = {}
                          where customer_id = {}
                      """.format(0,user_id)
                cursor.execute(SQL2)
                conn.commit()
                #记录还款
                SQL3 = """insert into creditcard_repayments(customer_id,creditcard_repayment_amount)
                          values({},{})
                       """.format(user_id,topay)
                cursor.execute(SQL3)
                conn.commit()
                
                window.withdraw()
                user_main()
                
    button_credit_repay_done = tk.Button(window,text = "还款",width = 20,command = creidtrepaydone)
    button_credit_repay_done.place(x=120, y=200)
    
    #返回
    def back():
        window.withdraw()
        user_main()    
    btn_back = tk.Button(window, text='返回',width = 20, command=back)
    btn_back.place(x=120, y=240)
    window.mainloop()

#选择查询对象菜单
def search_menu():
    window = tk.Tk()
    window.title('TreeFrog Bank - Search Transactions Page')
    window.geometry('450x380')
    l = tk.Label(window, 
        text='选择查询项目',
        font=('方正粗黑宋简体', 20),
        width=15, height=2)
    l.place(x=50,y=20)

    #查询存款记录
    def tosearch_deposit():
        window.withdraw()
        search_deposit()
    btn_deposit = tk.Button(window,text="查询存款记录",width = 20,command = tosearch_deposit)
    btn_deposit.place(x=150,y=140)
    
    #查询取款记录
    def tosearch_withdraw():
        window.withdraw()
        search_withdraw()
    btn_withdraw = tk.Button(window,text="查询取款记录",width = 20,command = tosearch_withdraw)
    btn_withdraw.place(x=150,y=180)
    
     #查询转账记录
    def tosearch_transfer():
        window.withdraw()
        search_transfer()
    btn_transfer = tk.Button(window,text="查询转账记录",width = 20,command = tosearch_transfer)
    btn_transfer.place(x=150,y=220)
    
    #查询信用卡记录
    def tosearch_creditcard():
        window.withdraw()
        search_creditcard()
    btn_creditcard = tk.Button(window,text="查询信用卡记录",width = 20,command = tosearch_creditcard)
    btn_creditcard.place(x=150,y=260)
    
    #返回
    def back():
        window.withdraw()
        user_main()    
    btn_back = tk.Button(window, text='返回',width = 20, command=back)
    btn_back.place(x=150, y=300)
    window.mainloop()

#查询存款记录
def search_deposit():
    print("search_deposit")
    window = tk.Tk()
    window.title('TreeFrog Bank - Search Deposits Page')
    window.geometry('800x500')
    l = tk.Label(window, 
        text='查询存款记录',
        font=('方正粗黑宋简体', 20),
        width=15, height=2)
    l.place(x=50,y=20)
    tk.Label(window, text='起始时间: ').place(x=100, y=80)
    entry_starttime = tk.Entry(window)
    entry_starttime.place(x=170,y=80)
    tk.Label(window, text='截止时间: ').place(x=450, y=80)
    entry_endtime = tk.Entry(window)
    entry_endtime.place(x=520,y=80)
    
    table = ttk.Treeview(window,height=12,show='headings')
    table.place(x=200,y=120)
    table["columns"] = ("存款编号","存款时间","存款金额")
    table.column("存款编号",width=80)
    table.column("存款时间",width=150)
    table.column("存款金额",width=100)
    table.heading("存款编号",text = "存款编号")
    table.heading("存款时间",text = "存款时间")
    table.heading("存款金额",text = "存款金额")
    
    def search_trans_done():
        if(entry_starttime.get() == ""):
            tk.messagebox.showinfo(title="输入错误", message="请输入起始时间")
        elif(entry_endtime.get() == ""):
            tk.messagebox.showinfo(title="输入错误", message="请输入截止时间")
        else:
            #获取数据
            starttime = entry_starttime.get()
            endtime = entry_endtime.get()
            cursor = conn.cursor()
            SQL = """select deposit_id,deposits_time,deposit_amount
                     from deposits
                     where customer_id = {} and deposits_time between "{}" and "{}";
                  """.format(user_id,starttime,endtime)
            cursor.execute(SQL)
            conn.commit()
            c = cursor.fetchall()
            #清空表格
            x=table.get_children()
            for item in x:
                table.delete(item)
            for i in range(len(c)):
                table.insert("",i,values = (c[i][0],c[i][1],c[i][2]))
                
    btn_search_trans_done = tk.Button(window, text='查询',width = 20, command=search_trans_done)
    btn_search_trans_done.place(x=300, y=400)
    
    #返回
    def back():
        window.withdraw()
        search_menu()    
    btn_back = tk.Button(window, text='返回',width = 20, command=back)
    btn_back.place(x=300, y=440)
    window.mainloop()

#查询取款记录
def search_withdraw():
    print("search_withdraw")
    window = tk.Tk()
    window.title('TreeFrog Bank - Search Withdraws Page')
    window.geometry('800x500')
    l = tk.Label(window, 
        text='查询取款记录',
        font=('方正粗黑宋简体', 20),
        width=15, height=2)
    l.place(x=50,y=20)
    tk.Label(window, text='起始时间: ').place(x=100, y=80)
    entry_starttime = tk.Entry(window)
    entry_starttime.place(x=170,y=80)
    tk.Label(window, text='截止时间: ').place(x=450, y=80)
    entry_endtime = tk.Entry(window)
    entry_endtime.place(x=520,y=80)
    
    table = ttk.Treeview(window,height=12,show='headings')
    table.place(x=200,y=120)
    table["columns"] = ("取款编号","取款时间","取款金额")
    table.column("取款编号",width=80)
    table.column("取款时间",width=150)
    table.column("取款金额",width=100)
    table.heading("取款编号",text = "取款编号")
    table.heading("取款时间",text = "取款时间")
    table.heading("取款金额",text = "取款金额")
    
    def search_trans_done():
        if(entry_starttime.get() == ""):
            tk.messagebox.showinfo(title="输入错误", message="请输入起始时间")
        elif(entry_endtime.get() == ""):
            tk.messagebox.showinfo(title="输入错误", message="请输入截止时间")
        else:
            #获取数据
            starttime = entry_starttime.get()
            endtime = entry_endtime.get()
            cursor = conn.cursor()
            SQL = """select withdraw_id,withdraw_time,withdraw_amount
                     from withdraws
                     where customer_id = {} and withdraw_time between "{}" and "{}";
                  """.format(user_id,starttime,endtime)
            cursor.execute(SQL)
            conn.commit()
            c = cursor.fetchall()
            #清空表格
            x=table.get_children()
            for item in x:
                table.delete(item)
            for i in range(len(c)):
                table.insert("",i,values = (c[i][0],c[i][1],c[i][2]))
                       
    btn_search_trans_done = tk.Button(window, text='查询',width = 20, command=search_trans_done)
    btn_search_trans_done.place(x=300, y=400)
    
    #返回
    def back():
        window.withdraw()
        search_menu()    
    btn_back = tk.Button(window, text='返回',width = 20, command=back)
    btn_back.place(x=300, y=440)
    window.mainloop()



#查询转账记录
def search_transfer():
    print("search_transfer")
    window = tk.Tk()
    window.title('TreeFrog Bank - Search Transfers Page')
    window.geometry('800x500')
    l = tk.Label(window, 
        text='查询转账记录',
        font=('方正粗黑宋简体', 20),
        width=15, height=2)
    l.place(x=50,y=20)
    tk.Label(window, text='起始时间: ').place(x=100, y=80)
    entry_starttime = tk.Entry(window)
    entry_starttime.place(x=170,y=80)
    tk.Label(window, text='截止时间: ').place(x=450, y=80)
    entry_endtime = tk.Entry(window)
    entry_endtime.place(x=520,y=80)
    
    table = ttk.Treeview(window,height=12,show='headings')
    table.place(x=100,y=120)
    table["columns"] = ("交易编号","交易时间","付款方","收款方","交易金额","交易种类")
    table.column("交易编号",width=80)
    table.column("交易时间",width=150)
    table.column("付款方",width=80)
    table.column("收款方",width=80)
    table.column("交易金额",width=100)
    table.column("交易种类",width=100)
    table.heading("交易编号",text = "交易编号")
    table.heading("交易时间",text = "交易时间")
    table.heading("付款方",text = "付款方")
    table.heading("收款方",text = "收款方")
    table.heading("交易金额",text = "交易金额")
    table.heading("交易种类",text = "交易种类")
    
    def search_trans_done():
        if(entry_starttime.get() == ""):
            tk.messagebox.showinfo(title="输入错误", message="请输入起始时间")
        elif(entry_endtime.get() == ""):
            tk.messagebox.showinfo(title="输入错误", message="请输入截止时间")
        else:
            #获取数据
            starttime = entry_starttime.get()
            endtime = entry_endtime.get()
            cursor = conn.cursor()
            SQL = """select transfer_id,transfer_time,sender_id,receiver_id,transfer_amount,transfer_catagory
                     from transfers
                     where sender_id = {} and transfer_creditcard = 0 and transfer_time between "{}" and "{}";
                  """.format(user_id,starttime,endtime)
            cursor.execute(SQL)
            conn.commit()
            c = cursor.fetchall()
            #清空表格
            x=table.get_children()
            for item in x:
                table.delete(item)
            for i in range(len(c)):
                table.insert("",i,values = (c[i][0],c[i][1],c[i][2],c[i][3],c[i][4],c[i][5]))
                

            
    btn_search_trans_done = tk.Button(window, text='查询',width = 20, command=search_trans_done)
    btn_search_trans_done.place(x=300, y=400)
    
    #返回
    def back():
        window.withdraw()
        search_menu()    
    btn_back = tk.Button(window, text='返回',width = 20, command=back)
    btn_back.place(x=300, y=440)
    window.mainloop()

#查询信用卡记录
def search_creditcard():
    print("search_creditcard")
    window = tk.Tk()
    window.title('TreeFrog Bank - Search Creditcards Page')
    window.geometry('800x500')
    l = tk.Label(window, 
        text='查询信用卡记录',
        font=('方正粗黑宋简体', 20),
        width=15, height=2)
    l.place(x=50,y=20)
    tk.Label(window, text='起始时间: ').place(x=100, y=80)
    entry_starttime = tk.Entry(window)
    entry_starttime.place(x=170,y=80)
    tk.Label(window, text='截止时间: ').place(x=450, y=80)
    entry_endtime = tk.Entry(window)
    entry_endtime.place(x=520,y=80)
    
    table = ttk.Treeview(window,height=12,show='headings')
    table.place(x=100,y=120)
    table["columns"] = ("交易编号","交易时间","付款方","收款方","交易金额","交易种类")
    table.column("交易编号",width=80)
    table.column("交易时间",width=150)
    table.column("付款方",width=80)
    table.column("收款方",width=80)
    table.column("交易金额",width=100)
    table.column("交易种类",width=100)
    table.heading("交易编号",text = "交易编号")
    table.heading("交易时间",text = "交易时间")
    table.heading("付款方",text = "付款方")
    table.heading("收款方",text = "收款方")
    table.heading("交易金额",text = "交易金额")
    table.heading("交易种类",text = "交易种类")
    
    def search_trans_done():
        if(entry_starttime.get() == ""):
            tk.messagebox.showinfo(title="输入错误", message="请输入起始时间")
        elif(entry_endtime.get() == ""):
            tk.messagebox.showinfo(title="输入错误", message="请输入截止时间")
        else:
            #获取数据
            starttime = entry_starttime.get()
            endtime = entry_endtime.get()
            cursor = conn.cursor()
            SQL = """select transfer_id,transfer_time,sender_id,receiver_id,transfer_amount,transfer_catagory
                     from transfers
                     where sender_id = {} and transfer_creditcard = 1 and transfer_time between "{}" and "{}";
                  """.format(user_id,starttime,endtime)
            cursor.execute(SQL)
            conn.commit()
            c = cursor.fetchall()
            #清空表格
            x=table.get_children()
            for item in x:
                table.delete(item)
            for i in range(len(c)):
                table.insert("",i,values = (c[i][0],c[i][1],c[i][2],c[i][3],c[i][4],c[i][5]))
                

            
    btn_search_trans_done = tk.Button(window, text='查询',width = 20, command=search_trans_done)
    btn_search_trans_done.place(x=300, y=400)
    
    #返回
    def back():
        window.withdraw()
        search_menu()    
    btn_back = tk.Button(window, text='返回',width = 20, command=back)
    btn_back.place(x=300, y=440)
    window.mainloop()

    
#交易统计分析
def analyse():
    print("analyse")
    window = tk.Tk()
    window.title('TreeFrog Bank - Transfer Analyse Page')
    window.geometry('800x500')
    l = tk.Label(window, 
        text='交易统计分析',
        font=('方正粗黑宋简体', 20),
        width=15, height=2)
    l.place(x=50,y=20)

    tk.Label(window, text='输入年份: ').place(x=100, y=80)
    entry_year = tk.Entry(window)
    entry_year.place(x=170,y=80)
    tk.Label(window, text='输入月份: ').place(x=450, y=80)
    entry_month = tk.Entry(window)
    entry_month.place(x=520,y=80)
    
    table = ttk.Treeview(window,height=12,show='headings')
    table.place(x=150,y=120)
    table["columns"] = ("消费种类","消费金额","消费次数")
    table.column("消费次数",width=150)
    table.column("消费金额",width=150)
    table.column("消费种类",width=150)
    table.heading("消费次数",text = "消费次数")
    table.heading("消费金额",text = "消费金额")
    table.heading("消费种类",text = "消费种类")
    
    def search_trans_done():
        if(entry_year.get() == ""):
            tk.messagebox.showinfo(title="输入错误", message="未输入年份")
        elif(entry_month.get() == ""):
            #按年统计
            #获取数据
            year = entry_year.get()
            cursor = conn.cursor()
            SQL = """select transfer_catagory,sum(transfer_amount),count(*)
                     from transfers
                     where sender_id = {} and transfer_time between "{}-01-01 00:00:00" and "{}-12-31 23:59:59"
                     group by transfer_catagory
                     order by sum(transfer_amount) desc;
                  """.format(user_id,year,year)
            cursor.execute(SQL)
            conn.commit()
            c = cursor.fetchall()
            #清空表格
            x=table.get_children()
            for item in x:
                table.delete(item)
            for i in range(len(c)):
                table.insert("",i,values = (c[i][0],c[i][1],c[i][2]))
        else:
            #按月统计
            #获取数据
            year = int(entry_year.get())
            month = int(entry_month.get())
            if((year%4 == 0 and year%100 != 0) or year%400 == 0):
                #闰年
                if(month in [1,3,5,7,8,10,12]):
                    lastday = 31
                elif(month == 2):
                    lastday = 29
                else:
                    lastday = 30
            else:
                #平年
                if(month in [1,3,5,7,8,10,12]):
                    lastday = 31
                elif(month == 2):
                    lastday = 28
                else:
                    lastday = 30
                    
            cursor = conn.cursor()
            SQL = """select transfer_catagory,sum(transfer_amount),count(*)
                     from transfers
                     where sender_id = {} and transfer_time between "{}-{}-01 00:00:00" and "{}-{}-{} 23:59:59"
                     group by transfer_catagory
                     order by sum(transfer_amount) desc;
                  """.format(user_id,year,month,year,month,lastday)
            cursor.execute(SQL)
            conn.commit()
            c = cursor.fetchall()
            #清空表格
            x=table.get_children()
            for item in x:
                table.delete(item)
            for i in range(len(c)):
                table.insert("",i,values = (c[i][0],c[i][1],c[i][2]))
                

            
    btn_search_trans_done = tk.Button(window, text='查询',width = 20, command=search_trans_done)
    btn_search_trans_done.place(x=300, y=400)
    
    #返回
    def back():
        window.withdraw()
        user_main()    
    btn_back = tk.Button(window, text='返回',width = 20, command=back)
    btn_back.place(x=300, y=440)
    window.mainloop()


    
#查询贷款信息    
def search_loans():
    print("search_loans")
    window = tk.Tk()
    window.title('TreeFrog Bank - Search Loans Page')
    window.geometry('800x500')
    l = tk.Label(window, 
        text='查询贷款信息',
        font=('方正粗黑宋简体', 20),
        width=15, height=2)
    l.place(x=50,y=20)
    
    table = ttk.Treeview(window,height=15,show='headings')
    table.place(x=50,y=80)
    table["columns"] = ("贷款编号","贷款金额","已还金额","还款比例","贷款期限","贷款时间")
    table.column("贷款编号",width=70)
    table.column("贷款金额",width=100)
    table.column("已还金额",width=150)
    table.column("还款比例",width=150)
    table.column("贷款期限",width=70)
    table.column("贷款时间",width=150)
    table.heading("贷款编号",text = "贷款编号")
    table.heading("贷款金额",text = "贷款金额")
    table.heading("已还金额",text = "已还金额")
    table.heading("还款比例",text = "还款比例")
    table.heading("贷款期限",text = "贷款期限")
    table.heading("贷款时间",text = "贷款时间")
    cursor = conn.cursor()
    #优化前的查询
    SQL = """select loans.loan_id,loans.loan_amount,
                    sum(loan_repayments.loan_repayment_amount),
                    sum(loan_repayments.loan_repayment_amount)/loans.loan_amount,
                    loans.loan_term,loan_time
             from loans,loan_repayments
             where loans.loan_id = loan_repayments.loan_id and loans.loan_repayed = false
             group by loans.loan_id;
          """
    #优化后的查询
    SQL = """select t1.loan_id,t1.loan_amount,
                    sum(loan_repayments.loan_repayment_amount),
                    sum(loan_repayments.loan_repayment_amount)/t1.loan_amount,
                    t1.loan_term,t1.loan_time
            from (select *
                  from loans
                  where loans.loan_repayed = false) as t1,loan_repayments
            where t1.loan_id = loan_repayments.loan_id
            group by t1.loan_id;
          """
    cursor.execute(SQL)
    conn.commit()
    c = cursor.fetchall()
    for i in range(len(c)):
        table.insert("",i,values = (c[i][0],c[i][1],c[i][2],c[i][3],c[i][4],c[i][5]))
    #返回
    def back():
        window.withdraw()
        user_main()    
    btn_back = tk.Button(window, text='返回',width = 20, command=back)
    btn_back.place(x=300, y=440)
    window.mainloop()
    
#查询基本信息
def search_basicinfo():
    print("search_info")
    window = tk.Tk()
    window.title('TreeFrog Bank - Baisc Info Page')
    window.geometry('420x300')
    l = tk.Label(window, 
        text='查询基本信息',
        font=('方正粗黑宋简体', 20),
        width=15, height=2)
    l.place(x=50,y=20)
    cursor = conn.cursor()
    SQL = """select customer_lendingrate,customer_creditlimit,customer_balance
             from customers
             where customer_id = {};
          """.format(user_id)
    cursor.execute(SQL)
    conn.commit()
    c = cursor.fetchall()
    tk.Label(window, text='余额：').place(x=70, y=120)
    tk.Label(window, text='{}'.format(c[0][2])).place(x=180, y=120)    
    tk.Label(window, text='贷款利率：').place(x=70, y=160)
    tk.Label(window, text='{}'.format(c[0][0])).place(x=180, y=160)
    tk.Label(window, text='个人信用额度：').place(x=70, y=200)
    tk.Label(window, text='{}'.format(c[0][1])).place(x=180, y=200)
    #返回
    def back():
        window.withdraw()
        user_main()    
    btn_back = tk.Button(window, text='返回',width = 20, command=back)
    btn_back.place(x=120, y=240)
    window.mainloop()

#查询个人信息
def search_info():
    print("search_info")
    window = tk.Tk()
    window.title('TreeFrog Bank - Personal Info Page')
    window.geometry('420x300')
    l = tk.Label(window, 
        text='查询个人信息',
        font=('方正粗黑宋简体', 20),
        width=15, height=2)
    l.place(x=50,y=20)
    cursor = conn.cursor()
    SQL = """select customer_type,customer_name
             from customers
             where customer_id = {};
          """.format(user_id)
    cursor.execute(SQL)
    conn.commit()
    c = cursor.fetchall()
    tk.Label(window, text='用户名：').place(x=70, y=100)
    tk.Label(window, text='{}'.format(user_id)).place(x=150, y=100)
    tk.Label(window, text='姓名：').place(x=70, y=140)
    tk.Label(window, text='{}'.format(c[0][1])).place(x=150, y=140)
    tk.Label(window, text='客户类型：').place(x=70, y=180)
    tk.Label(window, text='{}'.format(c[0][0])).place(x=150, y=180)
    #返回
    def back():
        window.withdraw()
        user_main()    
    btn_back = tk.Button(window, text='返回',width = 20, command=back)
    btn_back.place(x=120, y=240)
    window.mainloop()
    
#维护个人信息
def change_pwd():
    print("change_pwd")
    window = tk.Tk()
    window.title('TreeFrog Bank - Personal Infor Maintenance Page')
    window.geometry('420x330')
    l = tk.Label(window, 
        text='个人信息维护',
        font=('方正粗黑宋简体', 20),
        width=15, height=2)
    l.place(x=50,y=20)
    cursor = conn.cursor()
    SQL = """select customer_pwd
             from customers
             where customer_id = {};
          """.format(user_id)
    cursor.execute(SQL)
    conn.commit()
    c = cursor.fetchall()
    pwd = c[0][0]
    
    tk.Label(window, text='原密码: ').place(x=50, y= 120)
    entry_pwd = tk.Entry(window)
    entry_pwd.place(x=160,y=120)
    tk.Label(window, text='新密码: ').place(x=50, y= 160)
    entry_newpwd = tk.Entry(window)
    entry_newpwd.place(x=160,y=160)
    tk.Label(window, text='确认密码: ').place(x=50, y= 200)   
    entry_confirmpwd = tk.Entry(window)
    entry_confirmpwd.place(x=160,y=200)


    #修改密码
    def change_pwd_done():
        print("change_pwd_done")
        if(entry_pwd.get() == ""):
            tk.messagebox.showinfo(title="输入错误", message="请输入密码")
        elif(entry_newpwd.get() == ""):
            tk.messagebox.showinfo(title="输入错误", message="请输入新密码")
        elif(entry_confirmpwd.get() == ""):
            tk.messagebox.showinfo(title="输入错误", message="请确认密码")
        elif(entry_newpwd.get() != entry_confirmpwd.get()):
            tk.messagebox.showinfo(title="输入错误", message="两次密码输入不一致")
        elif(pwd != eval(entry_pwd.get())):
            tk.messagebox.showinfo(title="输入错误", message="密码错误")
    
        else:
            cursor = conn.cursor()
            SQL = """update customers
                     set customer_pwd = {}
                     where customer_id = {}
                  """.format(eval(entry_newpwd.get()),user_id)
            cursor.execute(SQL)
            conn.commit()
            window.withdraw()
            user_main()
            
    btn_change_pwd_done = tk.Button(window, text='修改密码',width = 20, command=change_pwd_done)
    btn_change_pwd_done.place(x=120, y=240)
    
    #返回
    def back():
        window.withdraw()
        user_main()    
    btn_back = tk.Button(window, text='返回',width = 20, command=back)
    btn_back.place(x=120, y=280)
    window.mainloop()
    
initial()
