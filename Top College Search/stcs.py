
# coding: utf-8

# In[1]:


import mysql.connector as con
import pandas as pd

database=con.connect(host="localhost",user="root",passwd="root")
cursor=database.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS institution")
database=con.connect(host="localhost",user="root",passwd="root",database="institution")


# In[2]:


from sqlalchemy import create_engine
engine=create_engine('mysql+mysqlconnector://root:root@localhost:3306/institution', echo = False)
connection =engine.raw_connection()
cursor = connection.cursor(buffered=True)


# In[3]:


def createTable():
    overall=str("CREATE TABLE IF NOT EXISTS `overall`(         `institute_id` varchar(255) NOT NULL PRIMARY KEY,              `name_of_institution` char(255),                   `city` char(100),                        `state` char(100),                             `score` float,                                  `ranking` int(10))")
    architecture=str("CREATE TABLE IF NOT EXISTS `architecture`(         `institute_id` varchar(255) NOT NULL PRIMARY KEY,              `name_of_institution` char(255),                   `city` char(100),                        `state` char(100),                             `score` float,                                  `ranking` int(10))")
    management=str("CREATE TABLE IF NOT EXISTS `management`(         `institute_id` varchar(255) NOT NULL PRIMARY KEY,              `name_of_institution` char(255),                   `city` char(100),                        `state` char(100),                             `score` float,                                  `ranking` int(10))")
    medical=str("CREATE TABLE IF NOT EXISTS `medical`(         `institute_id` varchar(255) NOT NULL PRIMARY KEY,              `name_of_institution` char(255),                   `city` char(100),                        `state` char(100),                             `score` float,                                  `ranking` int(10))")
    dental=str("CREATE TABLE IF NOT EXISTS `dental`(         `institute_id` varchar(255) NOT NULL PRIMARY KEY,              `name_of_institution` char(255),                   `city` char(100),                        `state` char(100),                             `score` float,                                  `ranking` int(10))")
    engineering=("CREATE TABLE IF NOT EXISTS `engineering`(         `institute_id` varchar(255) NOT NULL PRIMARY KEY,              `name_of_institution` char(255),                   `city` char(100),                        `state` char(100),                             `score` float,                                  `ranking` int(10))")
    research=("CREATE TABLE IF NOT EXISTS `research`(         `institute_id` varchar(255) NOT NULL PRIMARY KEY,              `name_of_institution` char(255),                   `city` char(100),                        `state` char(100),                             `score` float,                                  `ranking` int(10))")
    pharmacy=("CREATE TABLE IF NOT EXISTS pharmacy(         institute_id varchar(255) NOT NULL PRIMARY KEY,              name_of_institution char(255),                   city char(100),                        state char(100),                             score float,                                  ranking int(10))")
    law=str("CREATE TABLE IF NOT EXISTS `law` (         `institute_id` varchar(255) NOT NULL PRIMARY KEY,              `name_of_institution` char(255),                   `city` char(100),                        `state` char(100),                             `score` float,                                  `ranking` int(10))")
    college=str("CREATE TABLE IF NOT EXISTS `college` (         `institute_id` varchar(255) NOT NULL PRIMARY KEY,              `name_of_institution` char(255),                   `city` char(100),                        `state` char(100),                             `score` float,                                  `ranking` int(10))")
    university=str("CREATE TABLE IF NOT EXISTS `university` (         `institute_id` varchar(255) NOT NULL PRIMARY KEY,              `name_of_institution` char(255),                   `city` char(100),                        `state` char(100),                             `score` float,                                  `ranking` int(10))")


    cursor=database.cursor()
    cursor.execute(overall)
    cursor.execute(law)
    cursor.execute(research)
    cursor.execute(pharmacy)
    cursor.execute(university)
    cursor.execute(medical)
    cursor.execute(architecture)
    cursor.execute(dental)
    cursor.execute(college)
    cursor.execute(engineering)
    cursor.execute(management)
    database.commit()


# In[4]:


import sqlalchemy 
df=pd.read_excel('overall.xlsx')
df.to_sql("overall",engine,if_exists='replace',index=False)
df=pd.read_excel('management.xlsx')
df.to_sql("management",engine,if_exists='replace',index=False)
df=pd.read_excel('law.xlsx')
df.to_sql("law",engine,if_exists='replace',index=False)
df=pd.read_excel('research.xlsx')
df.to_sql("research",engine,if_exists='replace',index=False)
df=pd.read_excel('pharmacy.xlsx')
df.to_sql("pharmacy",engine,if_exists='replace',index=False)
df=pd.read_excel('university.xlsx')
df.to_sql("university",engine,if_exists='replace',index=False)
df=pd.read_excel('medical.xlsx')
df.to_sql("medical",engine,if_exists='replace',index=False)
df=pd.read_excel('architecture.xlsx')
df.to_sql("architecture",engine,if_exists='replace',index=False)
df=pd.read_excel('dental.xlsx')
df.to_sql("dental",engine,if_exists='replace',index=False)
df=pd.read_excel('college.xlsx')
df.to_sql("college",engine,if_exists='replace',index=False)
df=pd.read_excel('engineering.xlsx')
df.to_sql("engineering",engine,if_exists='replace',index=False)


# In[5]:


def runQuery(query):
    cursor=database.cursor(buffered=True)
    cursor.execute(query)
    data=cursor.fetchall()   
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("\nFollowing Institute Satisfy Required Parameter:\n")
    print("_________________________________________________")
    for i in data:
        for k,j in enumerate(i):
           if k==0:
                print("ID: ",j)
           elif k==1:
                print("Name: ",j)
           elif k==2:
                print("City: ",j)
           elif k==3:
                print("State: ",j)
           elif k==4:
                print("Score: ",j)
           else:
                print("Rank: ",j)
        print("\n")
        print("_________________________________________________")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n End Of Search Results.")


# In[6]:


def SearchByInstituteName(x):
    print("You Are Searching By The Institute Name: ")
    print("Select From The Following Search Type:-")
    print("1.Complete name Search\n2.Letter Wise Search\n")
    ch=int(input("Enter The Choice: "))
    if ch==1:
        name=input("Enter The Complete Name Of Institution: ")
        query=str("select * from {} where `name_of_institution`=LOWER('{}') order by ranking").format(x,name)
        runQuery(query)
    elif ch==2:
        char=input("Enter The Initial Letter Of The Institution: ")
        query=str("select * from {} where name_of_institution LIKE '{}%' order by ranking").format(x,char)
        runQuery(query)
    else:
        print("Wrong Choice! Choose From The Choices Available.")
    


# In[7]:


def SearchByInstituteId(x):
     print("You Are Searching By The Institute Id: ")
     id=input("Enter The Institute Id: ")
     query=str("select * from {} where 'institute_id'=LOWER('{}')").format(x,id)
     runQuery(query)


# In[8]:


def SearchByCity(x):
     print("You Are Searching By City: ")
     city=input("Enter The Name of City: ")
     query=str("select * from {} where `city`=LOWER('{}')").format(x,city)
     runQuery(query)


# In[9]:


def SearchByState(x):
     print("You Are Searching By State: ")
     city=input("Enter The Name of State: ")
     query=str("select * from {} where `state` like lower('{}')").format(x,city)
     runQuery(query)


# In[10]:


def SearchByScore(x):
     print("You Are Searching By The Institute Score: ")
     print("Select From The Following Search Type:-")
     print("1.Institute with Score Greater Than Required\n2.Institute with Score Less Than Required\n3.Institute with Score Between Required")
     ch=int(input("Enter The Choice: "))
     if ch==1:
          scr=float(input("Enter The Score Value(>): "))
          query=str("select * from {} where score>={} order by score").format(x,scr)
          runQuery(query)
     elif ch==2:
          scr=float(input("Enter The Score Value(<): "))
          query=str("select * from {} where score<={} order by score").format(x,scr)
          runQuery(query)
     elif ch==3:
          Low=float(input("Enter The Lowest Score Value: "))
          High=float(input("Enter The Highest Score Value: "))
          query=str("select * from {} where score between {} and {} order by score").format(x,Low,High)
          runQuery(query)
     else:
          print("Wrong Choice! Choose From The Choices Available.")


# In[11]:


def SearchByRank(x):
     print("You Are Searching By The Institute Rank: ")
     print("Select From The Following Search Type:-")
     print("1.Institute with Rank Greater Than Required\n2.Institute with Rank Less Than Required\n3.Institute with Rank Between Required")
     ch=int(input("Enter The Choice: "))
     if ch==1:
          rnk=int(input("Enter The Score Value(>): "))
          query=str("select * from {} where ranking>={} order by ranking").format(x,rnk)
          runQuery(query)
     elif ch==2:
          rnk=int(input("Enter The Rank Value(<): "))
          query=str("select * from {} where ranking<={} order by ranking").format(x,rnk)
          runQuery(query)
     elif ch==3:
          Low=int(input("Enter The Lowest Rank Value: "))
          High=int(input("Enter The Highest Rank Value: "))
          query=str("select * from {} where ranking between {} and {} order by ranking").format(x,Low,High)
          runQuery(query)
     else:
          print("Wrong Choice! Choose From The Choices Available.")


# In[12]:


def Overall():
     #import sqlalchemy 
     #df=pd.read_excel('overall.xlsx')
     #df.to_sql("overall",engine,if_exists='replace',index=False)
         #dtype={'institute_id': sqlalchemy.types.VARCHAR(length=100), 
                #'name_of_institution':  sqlalchemy.types.VARCHAR(length=255),
                #'city': sqlalchemy.types.VARCHAR(length=20),
                #'state': sqlalchemy.types.VARCHAR(length=20),
                #'score': sqlalchemy.types.Float(precision=2,asdecimal=True),
                #'rank':sqlalchemy.types.INTEGER()})

     while True:
          print("Overall College Search")
          print("Select from The Following Type Of Searches Available")
          print("1.Search by Institute Name\n2.Search Institute ID\n3.Search by City\n4.Search By State\n5.Search By Institute Score\n6.Search By Institute Rank\n7.Exit")
          ch=int(input("Your Choice:"))
          
          if ch==1:
               SearchByInstituteName("overall")
          elif ch==2:
               SearchByInstituteId("overall")
          elif ch==3:
               SearchByCity("overall")
          elif ch==4:
               SearchByState("overall")
          elif ch==5:
               SearchByScore("overall")
          elif ch==6:
               SearchByRank("overall")
          elif ch==7:
               break
          else:
               print("Wrong Choice! Choose From The Choices Available.")
          


# In[13]:


def Management():
     ###import sqlalchemy 
     ##df=pd.read_excel('management.xlsx')
     #df.to_sql("management",engine,if_exists='replace',index=False)
         #dtype={'institute_id': sqlalchemy.types.VARCHAR(length=100), 
                #'name_of_institution':  sqlalchemy.types.VARCHAR(length=255),
                #'city': sqlalchemy.types.VARCHAR(length=20),
                #'state': sqlalchemy.types.VARCHAR(length=20),
                #'score': sqlalchemy.types.Float(precision=2,asdecimal=True),
                #'rank':sqlalchemy.types.INTEGER()})

     while True:
          print("Management College Search")
          print("Select from The Following Type Of Searches Available")
          print("1.Search by Institute Name\n2.Search Institute ID\n3.Search by City\n4.Search By State\n5.Search By Institute Score\n6.Search By Institute Rank\n7.Exit")
          ch=int(input("Your Choice:"))
          
          if ch==1:
               SearchByInstituteName("management")
          elif ch==2:
               SearchByInstituteId("management")
          elif ch==3:
               SearchByCity("management")
          elif ch==4:
               SearchByState("management")
          elif ch==5:
               SearchByScore("management")
          elif ch==6:
               SearchByRank("management")
          elif ch==7:
               break
          else:
               print("Wrong Choice! Choose From The Choices Available.")


# In[14]:


def Medical():
     ###import sqlalchemy 
     ##df=pd.read_excel('medical.xlsx')
     #df.to_sql("medical",engine,if_exists='replace',index=False)
         #dtype={'institute_id': sqlalchemy.types.VARCHAR(length=100), 
                #'name_of_institution':  sqlalchemy.types.VARCHAR(length=255),
                #'city': sqlalchemy.types.VARCHAR(length=20),
                #'state': sqlalchemy.types.VARCHAR(length=20),
                #'score': sqlalchemy.types.Float(precision=2,asdecimal=True),
                #'rank':sqlalchemy.types.INTEGER()})

     while True:
          print("Medical College Search")
          print("Select from The Following Type Of Searches Available")
          print("1.Search by Institute Name\n2.Search Institute ID\n3.Search by City\n4.Search By State\n5.Search By Institute Score\n6.Search By Institute Rank\n7.Exit")
          ch=int(input("Your Choice:"))
          
          if ch==1:
               SearchByInstituteName("medical")
          elif ch==2:
               SearchByInstituteId("medical")
          elif ch==3:
               SearchByCity("medical")
          elif ch==4:
               SearchByState("medical")
          elif ch==5:
               SearchByScore("medical")
          elif ch==6:
               SearchByRank("medical")
          elif ch==7:
               break
          else:
               print("Wrong Choice! Choose From The Choices Available.")


# In[15]:


def Dental():
     #import sqlalchemy 
     ##df=pd.read_excel('dental.xlsx')
     #df.to_sql("dental",engine,if_exists='replace',index=False)
         #dtype={'institute_id': sqlalchemy.types.VARCHAR(length=100), 
                #'name_of_institution':  sqlalchemy.types.VARCHAR(length=255),
                #'city': sqlalchemy.types.VARCHAR(length=20),
                #'state': sqlalchemy.types.VARCHAR(length=20),
                #'score': sqlalchemy.types.Float(precision=2,asdecimal=True),
                #'rank':sqlalchemy.types.INTEGER()})

     while True:
          print("Dental College Search")
          print("Select from The Following Type Of Searches Available")
          print("1.Search by Institute Name\n2.Search Institute ID\n3.Search by City\n4.Search By State\n5.Search By Institute Score\n6.Search By Institute Rank\n7.Exit")
          ch=int(input("Your Choice:"))
          
          if ch==1:
               SearchByInstituteName("dental")
          elif ch==2:
               SearchByInstituteId("dental")
          elif ch==3:
               SearchByCity("dental")
          elif ch==4:
               SearchByState("dental")
          elif ch==5:
               SearchByScore("dental")
          elif ch==6:
               SearchByRank("dental")
          elif ch==7:
               break
          else:
               print("Wrong Choice! Choose From The Choices Available.")


# In[16]:


def Pharmacy():
     #import sqlalchemy 
     #df=pd.read_excel('pharmacy.xlsx')
     #df.to_sql("pharmacy",engine,if_exists='replace',index=False)
         #dtype={'institute_id': sqlalchemy.types.VARCHAR(length=100), 
                #'name_of_institution':  sqlalchemy.types.VARCHAR(length=255),
                #'city': sqlalchemy.types.VARCHAR(length=20),
                #'state': sqlalchemy.types.VARCHAR(length=20),
                #'score': sqlalchemy.types.Float(precision=2,asdecimal=True),
                #'rank':sqlalchemy.types.INTEGER()})

     while True:
          print("Pharmacy College Search")
          print("Select from The Following Type Of Searches Available")
          print("1.Search by Institute Name\n2.Search Institute ID\n3.Search by City\n4.Search By State\n5.Search By Institute Score\n6.Search By Institute Rank\n7.Exit")
          ch=int(input("Your Choice:"))
          
          if ch==1:
               SearchByInstituteName("pharmacy")
          elif ch==2:
               SearchByInstituteId("pharmacy")
          elif ch==3:
               SearchByCity("pharmacy")
          elif ch==4:
               SearchByState("pharmacy")
          elif ch==5:
               SearchByScore("pharmacy")
          elif ch==6:
               SearchByRank("pharmacy")
          elif ch==7:
               break
          else:
               print("Wrong Choice! Choose From The Choices Available.")


# In[17]:


def Law():
     #import sqlalchemy 
     #df=pd.read_excel('law.xlsx')
     #df.to_sql("law",engine,if_exists='replace',index=False)
         #dtype={'institute_id': sqlalchemy.types.VARCHAR(length=100), 
                #'name_of_institution':  sqlalchemy.types.VARCHAR(length=255),
                #'city': sqlalchemy.types.VARCHAR(length=20),
                #'state': sqlalchemy.types.VARCHAR(length=20),
                #'score': sqlalchemy.types.Float(precision=2,asdecimal=True),
                #'rank':sqlalchemy.types.INTEGER()})

     while True:
          print("Law College Search")
          print("Select from The Following Type Of Searches Available")
          print("1.Search by Institute Name\n2.Search Institute ID\n3.Search by City\n4.Search By State\n5.Search By Institute Score\n6.Search By Institute Rank\n7.Exit")
          ch=int(input("Your Choice:"))
          
          if ch==1:
               SearchByInstituteName("law")
          elif ch==2:
               SearchByInstituteId("law")
          elif ch==3:
               SearchByCity("law")
          elif ch==4:
               SearchByState("law")
          elif ch==5:
               SearchByScore("law")
          elif ch==6:
               SearchByRank("law")
          elif ch==7:
               break
          else:
               print("Wrong Choice! Choose From The Choices Available.")


# In[18]:


def Research():
     #import sqlalchemy 
     #df=pd.read_excel('research.xlsx')
     #df.to_sql("research",engine,if_exists='replace',index=False)
         #dtype={'institute_id': sqlalchemy.types.VARCHAR(length=100), 
                #'name_of_institution':  sqlalchemy.types.VARCHAR(length=255),
                #'city': sqlalchemy.types.VARCHAR(length=20),
                #'state': sqlalchemy.types.VARCHAR(length=20),
                #'score': sqlalchemy.types.Float(precision=2,asdecimal=True),
                #'rank':sqlalchemy.types.INTEGER()})

     while True:
          print("Research College Search")
          print("Select from The Following Type Of Searches Available")
          print("1.Search by Institute Name\n2.Search Institute ID\n3.Search by City\n4.Search By State\n5.Search By Institute Score\n6.Search By Institute Rank\n7.Exit")
          ch=int(input("Your Choice:"))
          
          if ch==1:
               SearchByInstituteName("research")
          elif ch==2:
               SearchByInstituteId("research")
          elif ch==3:
               SearchByCity("research")
          elif ch==4:
               SearchByState("research")
          elif ch==5:
               SearchByScore("research")
          elif ch==6:
               SearchByRank("research")
          elif ch==7:
               break
          else:
               print("Wrong Choice! Choose From The Choices Available.")


# In[19]:


def Engineering():
     #import sqlalchemy 
     #df=pd.read_excel('engineering.xlsx')
     #df.to_sql("engineering",engine,if_exists='replace',index=False)
         #dtype={'institute_id': sqlalchemy.types.VARCHAR(length=100), 
                #'name_of_institution':  sqlalchemy.types.VARCHAR(length=255),
                #'city': sqlalchemy.types.VARCHAR(length=20),
                #'state': sqlalchemy.types.VARCHAR(length=20),
                #'score': sqlalchemy.types.Float(precision=2,asdecimal=True),
                #'rank':sqlalchemy.types.INTEGER()})

     while True:
          print("Engineering College Search")
          print("Select from The Following Type Of Searches Available")
          print("1.Search by Institute Name\n2.Search Institute ID\n3.Search by City\n4.Search By State\n5.Search By Institute Score\n6.Search By Institute Rank\n7.Exit")
          ch=int(input("Your Choice:"))
          
          if ch==1:
               SearchByInstituteName("engineering")
          elif ch==2:
               SearchByInstituteId("engineering")
          elif ch==3:
               SearchByCity("engineering")
          elif ch==4:
               SearchByState("engineering")
          elif ch==5:
               SearchByScore("engineering")
          elif ch==6:
               SearchByRank("engineering")
          elif ch==7:
               break
          else:
               print("Wrong Choice! Choose From The Choices Available.")


# In[20]:


def University():
     #import sqlalchemy 
     #df=pd.read_excel('university.xlsx')
     #df.to_sql("university",engine,if_exists='replace',index=False)
         ##dtype={'institute_id': sqlalchemy.types.VARCHAR(length=100), 
          #      #'name_of_institution':  sqlalchemy.types.VARCHAR(length=255),
           #     #'city': sqlalchemy.types.VARCHAR(length=20),
            #    #'state': sqlalchemy.types.VARCHAR(length=20),
             #   #'score': sqlalchemy.types.Float(precision=2,asdecimal=True),
              #  #'rank':sqlalchemy.types.INTEGER()})

     while True:
          print("University College Search")
          print("Select from The Following Type Of Searches Available")
          print("1.Search by Institute Name\n2.Search Institute ID\n3.Search by City\n4.Search By State\n5.Search By Institute Score\n6.Search By Institute Rank\n7.Exit")
          ch=int(input("Your Choice:"))
          
          if ch==1:
               SearchByInstituteName("university")
          elif ch==2:
               SearchByInstituteId("university")
          elif ch==3:
               SearchByCity("university")
          elif ch==4:
               SearchByState("university")
          elif ch==5:
               SearchByScore("university")
          elif ch==6:
               SearchByRank("university")
          elif ch==7:
               break
          else:
               print("Wrong Choice! Choose From The Choices Available.")


# In[21]:


def College():
     #import sqlalchemy 
     #df=pd.read_excel('college.xlsx')
     #df.to_sql("college",engine,if_exists='replace',index=False)
         #dtype={'institute_id': sqlalchemy.types.VARCHAR(length=100), 
                #'name_of_institution':  sqlalchemy.types.VARCHAR(length=255),
                #'city': sqlalchemy.types.VARCHAR(length=20),
                #'state': sqlalchemy.types.VARCHAR(length=20),
                #'score': sqlalchemy.types.Float(precision=2,asdecimal=True),
                #'rank':sqlalchemy.types.INTEGER()})

     while True:
          print("College College Search")
          print("Select from The Following Type Of Searches Available")
          print("1.Search by Institute Name\n2.Search Institute ID\n3.Search by City\n4.Search By State\n5.Search By Institute Score\n6.Search By Institute Rank\n7.Exit")
          ch=int(input("Your Choice:"))
          
          if ch==1:
               SearchByInstituteName("college")
          elif ch==2:
               SearchByInstituteId("college")
          elif ch==3:
               SearchByCity("college")
          elif ch==4:
               SearchByState("college")
          elif ch==5:
               SearchByScore("college")
          elif ch==6:
               SearchByRank("college")
          elif ch==7:
               break
          else:
               print("Wrong Choice! Choose From The Choices Available.")


# In[22]:


def Architecture():
     #import sqlalchemy 
     #df=pd.read_excel('architecture.xlsx')
     #df.to_sql("architecture",engine,if_exists='replace',index=False)
         #dtype={'institute_id': sqlalchemy.types.VARCHAR(length=100), 
                #'name_of_institution':  sqlalchemy.types.VARCHAR(length=255),
                #'city': sqlalchemy.types.VARCHAR(length=20),
                #'state': sqlalchemy.types.VARCHAR(length=20),
                #'score': sqlalchemy.types.Float(precision=2,asdecimal=True),
                #'rank':sqlalchemy.types.INTEGER()})

     while True:
          print("Architecture College Search")
          print("Select from The Following Type Of Searches Available")
          print("1.Search by Institute Name\n2.Search Institute ID\n3.Search by City\n4.Search By State\n5.Search By Institute Score\n6.Search By Institute Rank\n7.Exit")
          ch=int(input("Your Choice:"))
          
          if ch==1:
               SearchByInstituteName("architecture")
          elif ch==2:
               SearchByInstituteId("architecture")
          elif ch==3:
               SearchByCity("architecture")
          elif ch==4:
               SearchByState("architecture")
          elif ch==5:
               SearchByScore("architecture")
          elif ch==6:
               SearchByRank("architecture")
          elif ch==7:
               break
          else:
               print("Wrong Choice! Choose From The Choices Available.")


# In[23]:


#main menu switch
while True:
     print("Main Menu")
     print("Select To Search From Following College Categories")
     print("\t1.Overall\n\t2.University\n\t3.Engineering\n\t4.Architecture\n\t5.Management\n\t6.Medical\n\t7.Dental\n\t8.Pharmacy\n\t9.Law\n\t10.Research\n\t11.College\n\t12.Exit")
     
    
     ch1=int(input("Your Choice : "))

     if ch1==1:
          Overall()
     elif ch1==2:
          University()
     elif ch1==3:
          Engineering()
     elif ch1==4:
          Architecture()
     elif ch1==5:
          Management()
     elif ch1==6:
          Medical()
     elif ch1==7:
          Dental()
     elif ch1==8:
          Pharmacy()
     elif ch1==9:
          Law()
     elif ch1==10:
          Research()
     elif ch1==11:
          College()
     elif ch1==12:
          break
     else:
          print("Wrong Choice! Choose From The Choices Available.")


# In[24]:


#query=str("select e.institute_id,e.name_of_institution,e.ranking from engineering as e INNER JOIN law as a ON e.name_of_institution=a.name_of_institution ORDER BY e.ranking desc")
#database.close()


# In[25]:


database.close()
#drop schema manually if retry transaction

