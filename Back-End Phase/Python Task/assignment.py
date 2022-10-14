import mysql.connector

cnx = mysql.connector.connect(user='root', password='123456789aA@',
                              host='127.0.0.1',
                              )
cursor = cnx.cursor()
cursor.execute("DROP DATABASE schoolPython")
cursor.execute("CREATE DATABASE schoolPython")

cursor.execute("USE schoolPython")
cursor.execute("create table student ("
               "studentID int,"
               "FirstName varchar(15),"
               "Age int,"
               "fatherID int,"
               "constraint studentID primary key (studentID)"
               ");")
cursor.execute("INSERT INTO student (studentID,FirstName,Age,fatherID) "
               " VALUES (1, 'saeed', 22, 1);")
cursor.execute("INSERT INTO student (studentID,FirstName,Age,fatherID) "
               " VALUES (2, 'Yasser', 43, 2);")
cursor.execute("INSERT INTO student (studentID,FirstName,Age,fatherID) "
               " VALUES (3, 'Maha', 21, 1);")
cursor.execute("INSERT INTO student (studentID,FirstName,Age,fatherID) "
               " VALUES (4, 'Ali', 23, 3);")
cursor.execute("create table courses ("
               "CourseID int,"
               "grade int,"
               "code varchar(10),"
               "constraint courseId primary key (courseID)"
               ");")

cursor.execute("INSERT INTO courses (CourseID,grade,code) "
               " VALUES (1, 100, 'EME 2');")

cursor.execute("INSERT INTO courses (CourseID,grade,code) "
               " VALUES (2, 60, 'EME 4');")

cursor.execute("create table pivotCoursesStudent("
               "courseID int,"
               "studentID int,"
               "constraint courseID foreign key (courseID) references courses(courseID),"
               "constraint studentID foreign key (studentID) references student(studentID),"
               "constraint courseStudent unique(studentID,courseID)"
               ");")

cursor.execute("INSERT INTO pivotCoursesStudent (CourseID,studentID) "
               " VALUES (1, 1);")

cursor.execute("INSERT INTO pivotCoursesStudent (CourseID,studentID) "
               " VALUES (1,2);")
cursor.execute("INSERT INTO pivotCoursesStudent (CourseID,studentID) "
               " VALUES (1,3);")
cursor.execute("INSERT INTO pivotCoursesStudent (CourseID,studentID) "
               " VALUES (2,2);")
cursor.execute("INSERT INTO pivotCoursesStudent (CourseID,studentID) "
               " VALUES (2,3);")


cursor.execute("create table fathers("
               "FatherID int,"
               "FirstName varchar(15),"
               "LastName varchar(15),"
               "adress varchar(15),"

               "constraint FatherID primary key(FatherID)"
               ");")

cursor.execute("INSERT INTO fathers (FatherId,FirstName,LastName,adress) "
               " VALUES (1, 'mazen', 'ahmed', '6 octobar');")
cursor.execute("INSERT INTO fathers (FatherId,FirstName,LastName,adress) "
               " VALUES (2, 'morad', 'ali', 'giza');")
cursor.execute("INSERT INTO fathers (FatherId,FirstName,LastName,adress) "
               " VALUES (3, 'nabil', 'mohamed', 'zamalek');")

cursor.execute("alter table student"
               " ADD constraint fatherID foreign key (fatherID) references fathers(fatherID)")

cursor.execute("create table universityids("
               "studentID int,"
               "universityID int,"
               "constraint universityID primary key(universityID),"
               "constraint studentIDD foreign key (studentID) references student(studentID)"
               ");")
cursor.execute("INSERT INTO universityids (studentID,universityID) "
               " VALUES (1,18010);")
cursor.execute("INSERT INTO universityids (studentID,universityID) "
               " VALUES (2,18011);")
cursor.execute("INSERT INTO universityids (studentID,universityID) "
               " VALUES (3,18012);")

########MANY-TO_MANY################
cursor.execute("select student.FirstName , courses.code from student "
               "inner join pivotcoursesstudent  on pivotcoursesstudent.studentID =student.studentID "
               "inner join courses  on  pivotcoursesstudent.courseID =courses.courseID")
#############ONE-TO-ONE##################
cursor.execute("select student.FirstName , universityids.universityID as collegeID  from student "
               "inner join universityids on student.studentID=universityids.studentID ")
#############ONE-TO-MANY#################
cursor.execute("select student.FirstName as student , fathers.FirstName as hisFather from student "
               "inner join fathers  on student.fatherID =fathers.fatherID")

# select student.FirstName , courses.code from student
# inner join pivotcoursesstudent  on pivotcoursesstudent.studentID =student.studentID
# inner join courses  on  pivotcoursesstudent.courseID =courses.courseID

# select student.FirstName , universityids.universityID as collegeID from student
# inner join universityids on student.studentID=universityids.studentID


# select student.FirstName as student , fathers.FirstName as hisFather from student
# inner join fathers  on student.fatherID =fathers.fatherID


cnx.close()
