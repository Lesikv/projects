#!/usr/bin/env python 
#coding: utf8

import argparse

def parser():
    parser = argparse.ArgumentParser(description = 'Inpur a list of strings')
    parser.add_argument('--first')
    parser.add_argument('--second')
    return parser.parse_args()

#def strcomp(first,second):
def strcomp(*strings):
    #print(first)
    first = strings[0]
    second = strings[1]
    #print(second)
    if first == second:
        return 1
    else:
        if len(first) > len(second):
            return 2
        if second == 'learn':
            return 3

def main():
    options = parser()

    print(strcomp('abc','learn'))


if __name__ == '__main__':                                                                                                                                                                   
    main() 
