import mysql.connector
conn=mysql.connector.connect(host='localhost',password='mani123',user='root',database='counselling')
cur=conn.cursor()

def intro():
    print('-------------------------------------------------------------------------------------')
    print('                    WLECOME TO ENGINEERING CONSELLING FOR THE YEAR 2023-2024              ')
    print('''               "You have to dream before your dreams can come true."
                                                                     ---A.P.J.ABDUL KALAM''')
    print('-------------------------------------------------------------------------------------')
    print("ELIGIBLE STUDENT (CUT OFF) FOR ROUND 1: 200-160")
    print("ELIGIBLE STUDENT (CUT OFF) FOR ROUND 2: 159-120")
    print("Enter your student ID accordingly")
    l=["select max(student_id) from student_round_1","select max(student_id) from student_round_2"]
    for p in range(1,len(l)+1):
        cur.execute(l[p-1])
        d=cur.fetchall()
        for o in d:
            print(o,"<--round "+str(p))
    print("ACCORDING TO LAST STUDENT'S ID, ENTER YOURS!")

def data_round():
    global student_id,student_name
    student_id=input("Enter the student ID[(SRXX)(where X = Your Number, R = Round NO)]:")
    student_name=input("Enter the Student's Name:")

def storing_in_table():
    sql_query="insert into "+str(round_no)+" values('%s','%s',%s)"%(student_id,student_name,cut_off)
    print(sql_query)
    cur.execute(sql_query)

def fetching_the_data_stu(): 
    sql_query_sel="select * from "+str(round_no)+" where student_id=('%s')"%(student_id)
    cur.execute(sql_query_sel)
    data=cur.fetchall()
    data_stu=cur.fetchall()
    for i in data_stu:
        print("Student Detail:",i)

def display_the_data():
    print("The eligible colleges are:")
    sql_query_clg = '''
    SELECT
        '''+str(round_no)+'''.student_name,
        '''+str(clg_round)+'''.college_name,
        '''+str(round_no)+'''.cut_off
    FROM
        '''+str(round_no)+'''
    JOIN
        '''+str(clg_round)+'''
    ON
        '''+str(round_no)+'''.cut_off >='''+str(clg_round)+'''.cut_off
    AND student_id=('%s')
    '''%(student_id)
    cur.execute(sql_query_clg)
    data_clg=cur.fetchall()
    for j in data_clg:
        print(j)

def outcome():
    s="insert into college_selected_list values('%s','%s','%s','%s')"%(student_id,student_name,clg,crs)
    cur.execute(s)
    sql_outcome="select * from college_selected_list"
    cur.execute(sql_outcome)
    data_outcome=cur.fetchall()
    print(data_outcome[-1])
    print("          -----------Soon you will be contacted by the College---------           ")
    print("                             -------! ALL THE BEST !-----                             ")

def waiting():
    global crs
    wai=input("Would you prefer a moment for contemplation before confirming your choice of college? (Yes/No) :")
    if wai.lower()=='yes':
        print("Waiting Period List.....")
        sql_wait="insert into waiting_period values('%s','%s','%s')"%(student_id,student_name,round_no)
        cur.execute(sql_wait)
        sql_wait_1="select * from waiting_period"
        cur.execute(sql_wait_1)
        wait_tup=cur.fetchall()
        for k in wait_tup:
            print(k)
        print("You have been added \nKindly confirm it Soon....")
    elif wai.lower()=='no':
        print("Then you have choosen.....")
        crs=input("Enter the course name:")
        outcome()
    else:
        print('Wrong input')
        
def confirmation():
    global clg,crs
    conf=input("Did you confirm the college (yes/no):")
    if conf.lower()=='yes':
        clg=input("Enter the college from the above(short form):")
        lst_clg=['AU','CEG','SNSCT','SSNCE','PSGCT','TCE','CIT','KCT']
        for x in lst_clg:
            if clg.upper()==x:
                print("Courses in",x)
                sql_query_co="select * from courses"
                cur.execute(sql_query_co)
                course=cur.fetchall()
                for z in course:
                    print(z)
        confirm=input("Did you confirmed the course(yes/no):")
        if confirm.lower()=='yes':
            crs=input("Enter the course name:")
            outcome()
        elif confirm.lower()=='no':
            waiting()
        else:
            print('Wrong input')
    elif conf.lower()=='no':
        wai=input("Do you want sometime to think(yes/no):")
        if wai.lower()=='yes':
            print("Waiting period list.....")
            sql_wait="insert into waiting_period values('%s','%s','%s')"%(student_id,student_name,round_no)
            cur.execute(sql_wait)
            sql_wait_1="select * from waiting_period"
            cur.execute(sql_wait_1)
            wait_tup=cur.fetchall()
            for k in wait_tup:
                print(k)
            print("You have been added to Waiting List \nKindly confirm it Soon....")
    else:
        print("Wrong input")
        
def working():
    data_round()
    storing_in_table()
    fetching_the_data_stu()
    display_the_data()
    confirmation()
    
def main_prg():
    for i in range(1):
        intro()
        global round_no,clg_round,cut_off
        cut_off=int(input("Enter your Cut off:"))
        if 200>=cut_off>=160:
            print("You are at round 1")
            round_no="student_round_1"
            clg_round="college_round_1"
            working()
        elif 159>=cut_off>=120:
            print("You are at round 2")
            round_no="student_round_2"
            clg_round="college_round_2"
            working()
        elif 119>=cut_off:
            print("Wait for Round 3 to start!")
        else:
            print("Wrong input!")

main_prg()
conn.commit()
conn.close()



    

    
