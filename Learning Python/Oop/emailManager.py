#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
Created on 2014年7月25日

@author: zhaoyb
@license: granted by zhaoyb 20140725
@deprecated: This is a python demo for manage a email information.
'''
import os
import sys
import cPickle as p

class Person:
    '''
    person POJO
    '''
    def __init__(self, name,email):
        '''
        initialize person data
        '''
        self.name = name
        self.email = email
    
def create():
        '''
        Create a person data in persons
        '''
        global Persons
        try:
            name = raw_input("Please input name:")
            while Persons.has_key(name):
                name = raw_input("This name has already exist, please input new name:")
        except EOFError:
            print '\nEOF Error'
            sys.exit()
        email = raw_input("Please input Email:")
        Persons[name] = email
        save()
        print ""
def delete():
    """Search person by name and delete"""
    global Persons
    try:
        name = raw_input("Please input the person's name you want to delete:")
    except EOFError:
        print '\nEOF Error'
        sys.exit()
    if Persons.has_key(name):
        del Persons[name]
        save()
    else:
        print "No one called",name,"!\n"

def modify():
    """Search person by name and modify email"""
    global Persons
    try:
        name = raw_input("Please input the person's name you want to modify:")
        if Persons.has_key(name):
            del Persons[name]
            email = raw_input("Please input new email:")
            Persons[name] = email
            save()
        else:
            print "No one called",name,"!\n"
    except EOFError:
        print '\nEOF Error'
        sys.exit()

def save():
    """Save Persons to file"""
    global Persons
    File = 'person.dat'
    f = file(File, 'w')
    p.dump(Persons, f)
    f.close()
    print "Operation Done!\n"

def read():
    """Read person from file"""
    global Persons
    File = 'person.dat'
    if os.path.exists(File):
        f = file(File)
        Persons = p.load(f)
        f.close()
    else:
        File = 'person.dat'
        f = file(File, 'w')
        f.close()

def display():
    """Display all persons in the dictionary"""
    global Persons
    for name, email in Persons.items():
        print "        ",name,email
    print ""

def search():
    """Search person by name"""
    global Persons
    try:
        name = raw_input("Please input the person's name you want to search:")
    except EOFError:
        print '\nEOF Error'
        sys.exit()
    if Persons.has_key(name):
        print "        ",name,Persons[name],"\n"
    else:
        print "No one called",name,"!\n"

def menu():
    """Display a menu to choose operation"""
    choose = "0"
    while True:
        #i = os.system("cls")
        print'''1----Create
2----Delete
3----Modify
4----Search
5----Display
6----Exit'''
        try:
            choose = int(raw_input("Please choose an item(1-6):"))
        except EOFError:
            print '\nEOF Error'
            sys.exit()
        if choose == 1:
            create()
        elif choose == 2:
            delete()
        elif choose == 3:
            modify()
        elif choose == 4:
            search()
        elif choose == 5:
            display()
        elif choose == 6:
            print "Thanks for using!"
            sys.exit()
        else:
            print ""
            
if __name__ == "__main__":
    Persons = {}
    read()
    menu()