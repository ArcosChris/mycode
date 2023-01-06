#!/usr/bin/env python3


import shutil
import os

#changing user path when app runs
os.chdir('/home/student/mycode/')

#move file into ceph_storage dir
shutil.move('raynor.obj', 'ceph_storage/')

#ask user for input to change name of file
xname = input('What is the new name for kerrigan.obj? ')

#using mv to rename the file in the ceph_storage dir
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)





