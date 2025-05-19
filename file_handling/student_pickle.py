#storing student data into file

import student,pickle

stud=[student.student(10,'ram','ji'),student.student(11,'laxman',"jii"),student.student(12,'bharat','ji')]

with open('students.data','wb') as f:
    for s in stud:
        pickle.dump(s,f)

