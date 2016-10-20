#!/usr/bin/env python
#coding:utf-8

__authon__ = "Harvey.Wang"

def copy_file(read_file_name, write_file_name, operation_type = 'a+'):
    try:
        print("Copy file start...")
        with open(read_file_name) as readfile, open(write_file_name,operation_type) as writefile:
            for line in readfile.readlines():
                writefile.write(line)

        print("Write done")
    except Exception:
        print("Error...")

if __name__ == "__main__":
    read_file_name = input("Plese input file name by read: ")
    write_file_name = input("Plese input file name by write: ")
    operation_type = input("Please input write type(w:rewrite, a:append: ")
    
    print(operation_type.strip())
    
    copy_file(read_file_name, write_file_name, operation_type)
