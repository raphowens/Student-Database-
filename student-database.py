#Author: 766431

#File: Day5_Student_Database.py

def intro():

    Name='RAPHAEL OWENS'
    Matriculation_number=766431
    
    print(f'{Name}, {Matriculation_number}')

intro()


print("""
        **********************************************
                     STUDENT DATABASE
        **********************************************
        """)


class Student_Database:
    '''This class is the general overview of the student database. We
       give the database a name here
    '''
    database_name=input('Enter database name: ')
    database_name=database_name.upper()
    print(f'{database_name} Database created')
    
    def __init__(self,first_name=None,last_name=None,mat_number=None):
        '''This is the constructor, where the student data which includes
           the first name, last name and mat number are passed as arguments.
        '''
        self.first_name=first_name
        self.last_name=last_name
        self.mat_number=mat_number
        self.student_list=[]

    def add_student_data(self):
        '''This method(function) is called when student data are added to the database,
           it asks for the number of students to be entered, and also names and mat n0
           of the students.
        '''
        num_of_students=int(input('No of students to be entered in database: '))
        n=num_of_students
        
        for i in range (1,n+1):
            self.first_name=input('Enter first name: ')

            self.last_name=input('Enter last name: ')
            self.mat_number=input('Enter mat number: ')
            ob=(self.last_name.capitalize() + ',',self.first_name.capitalize(),self.mat_number)
            self.student_list.append(ob)

        print(f'{Student_Database.database_name} Database created with {len(self.student_list)} student record(s)')

    def display_student_data(self):
        '''This method displays the student data'''
        
        print(f'{Student_Database.database_name} Database has {len(self.student_list)} student(s) records')
        for data in self.student_list:
            #print(f'{data[0]}, {data[1]}\t {data[2]}')
            print(f'{data[0]:10s} {data[1]:10s} {data[2]:20s}')
            
                       

    def free_database(self):
        '''This method deletes the student data'''
        
        confirm = int(input('ARE YOU SURE TO DELETE? Type 1 to confirm!: '))
        if confirm==1:
             self.student_list = []       
             print(f'All records deleted from {Student_Database.database_name}!')
        else:
             print('Process cancelled ... nothing deleted')
             #print(self)

    def find_student_data(self):
        '''This method find a student using either a name or matriculation number'''
        find=(input('Enter name or number to search: '))
        search=find.capitalize()
       
        for tup in self.student_list:
            if search in tup:
                print(f'Student data found in {Student_Database.database_name} Database')
                print(f'{tup[0]:10s} {tup[1]:10s} {tup[2]:20s}')
                break
        if search not in tup:
            print('NOT FOUND')
            

    def sort_student_data(self):
        '''This method sort the student database either by the name or matriculation number'''

        sort_method=int(input('Select sort method, Name (1) or Matriculation number(2): '))
        
        if sort_method == 1:
            print(f'{Student_Database.database_name} Database sorted by Name')
            sort_name=(sorted(self.student_list, key=lambda mysort_name: mysort_name[0]))
            for bla in sort_name:
                print(f'{bla[0]:10s} {bla[1]:10s} {bla[2]:20s}')
                
                
        elif sort_method == 2:
            print(f'{Student_Database.database_name} Database sorted by Matriculation number')
            sort_number=(sorted(self.student_list, key=lambda mysort_number: mysort_number[2]))
            for bla in sort_number:
                print(f'{bla[0]:10s} {bla[1]:10s} {bla[2]:20s}')




    def selection(self):
        '''This method give a list of choice to be selected from and it executes when a particular choice is chosen'''

        
        print('[Choice 1: Add Students Data]')
        print('[Choice 2: Display Students Data]')
        print('[Choice 3: Find Student]')
        print('[Choice 4: Sort Student Data]')
        print('[Choice 5: Clear Student Data]')

        Choice = int(input('Enter a choice (1,2,3,4 or 5): '))

        if Choice == 1:
            Hda.add_student_data()
            Hda.run_again()
            
        elif Choice == 2:
            Hda.display_student_data()
            Hda.run_again()

        elif Choice == 3:
            Hda.find_student_data()
            Hda.run_again()

        elif Choice == 4:
            Hda.sort_student_data()
            Hda.run_again()

        elif Choice == 5:
            Hda.free_database()
            Hda.run_again()


    def run_again(self):
        '''This method ask the user if he/she wants to continue with other choices or exit the databse'''
        action=input('Do you want to continue yes/no: ').lower()
        #action=action.lower()
        if action == 'yes':
            Hda.selection()
        else:
            print('Database Concluded')

        
            
        
##    def __str__(self):
##        return (f'{Student_Database.database_name} Database has {len(self.student_list)} student records')

if __name__ == "__main__":
       
    Hda=Student_Database(first_name=None,last_name=None,mat_number=None)

    Hda.selection()


##Hda.add_student_data()
##
##Hda.display_student_data()
##
###Hda.free_database()
##
##Hda.find_student_data()
##
##Hda.sort_student_data()



input('...')
