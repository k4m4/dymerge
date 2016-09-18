#!/usr/bin/env python
# dymerge.py

"""
Copyright (C) 2016 Nikolaos Kamarinakis (nikolaskam{at}gmail{dot}com)
See License at nikolaskama.me (https://nikolaskama.me/dymergeproject)

 ____                                                    
/\  _`\           /'\_/`\                               
\ \ \/\ \  __  __/\      \     __   _ __    __      __   
 \ \ \ \ \/\ \/\ \ \ \__\ \  /'__`\/\` __\/'_ `\  /'__`\ 
  \ \ \_\ \ \ \_\ \ \ \_/\ \/\  __/\ \ \//\ \_\ \/\  __/ 
   \ \____/\/`____ \ \_\\ \_\ \____\\ \_\\ \____ \ \____\
    \/___/  `/___/  \/_/ \/_/\/____/ \/_/ \/____\ \/____/
               /\___/                       /\____/      
               \/__/  Made with <3 by k4m4  \_/__/
"""

import sys, os, optparse, time, zipfile, tarfile, bz2, gzip, imp, StringIO
from time import sleep
from termcolor import colored

def displayLogo():
    logo = []
    print info
    try:
        path = 'txt/logo.txt'
        with open(path, 'r') as myFile:
            lines = myFile.readlines()
            for line in lines:
                logo.append(line.rstrip('\n'))
        for line in logo:
            print line

    # some people just don't like seeing logos in their clis...
    except IOError: # (Ignored) Error --> "No Such (logo.txt) File"
        return       

def flushPrint(msg, error=False, ext=False):
    if ext:
        msg, msg_e = msg.split(' --> ')
        msg += ' --> '
        
    if fast:
        if error:
            sys.stdout.write(colored('\n[-] ', 'red'))
            sys.stdout.write(colored(msg, 'red'))
            if ext:
                sys.stdout.write(colored(msg_e, 'red', attrs = ['bold']))
        else:
            sys.stdout.write(colored('\n[+] ', 'green'))
            sys.stdout.write(colored(msg, 'green'))
            if ext:
                sys.stdout.write(colored(msg_e, 'green', attrs = ['bold']))
    else:
        if error:
            sys.stdout.write(colored('\n[-] ', 'red'))
            for char in msg:
                sleep(0.03)
                sys.stdout.write(colored(char, 'red'))
                sys.stdout.flush()
            if ext:
                for char in msg_e:
                    sleep(0.03)
                    sys.stdout.write(colored(char, 'red', attrs = ['bold']))
                    sys.stdout.flush()
        else:
            sys.stdout.write(colored('\n[+] ', 'green'))
            for char in msg:
                sleep(0.03)
                sys.stdout.write(colored(char, 'green'))
                sys.stdout.flush()
            if ext:
                for char in msg_e:
                    sleep(0.03)
                    sys.stdout.write(colored(char, 'green', attrs = ['bold']))
                    sys.stdout.flush()

def delayEffect():
    if fast:
        return
    else:
        time.sleep(.5)

def appendListGenerator(option, opt, value, parser):
    setattr(parser.values, option.dest, value.split(','))

def readFiles():
    if len(argv) > 1:
        flushPrint("Reading Dictionaries")
        delayEffect()
        flushPrint("Merging Dictionaries")
    else:
        flushPrint("Reading Dictionary")
    for i in range(len(argv)):
        try:
            with open(argv[i], 'r') as myFile:
                if os.path.getsize(argv[i]) > 0:
                    lines = myFile.readlines()
                    for line in lines:
                        wordList.append(line.rstrip('\n'))
                else: # Error --> "File (dict.) is empty"
                    delayEffect()
                    flushPrint("Dictionary Is Empty --> Please Enter A Valid File", True, True)
                    flushPrint("System Exit\n", True)
                    raise SystemExit

            # Error --> "File (dict.) is compressed"
            commonFormats = open('txt/archive_formats.txt').read().split('\n')
            for archiveFormat in commonFormats:
                if archiveFormat == '': # just in case you've been playing around...
                    return
                if (argv[i]).endswith(archiveFormat):
                    print(archiveFormat)
                    print('yes')
                    delayEffect()
                    flushPrint("Invalid Dictionary File Format --> Please Enter A Valid File", True, True)
                    flushPrint("System Exit\n", True)
                    raise SystemExit
                
        except IOError: # Error --> "No such (dict.) file"
            delayEffect()
            flushPrint("Dictionary(ies) Not Found --> Please Enter A Valid Path", True, True)
            flushPrint("System Exit\n", True)
            raise SystemExit

def includeValues():
    flushPrint("Including Prompted Values")
    for value in include_values:
        wordList.append(value)

def makeUnique():
    global wordList
    
    flushPrint("Removing All Duplicates")
    # wordList = list(set(wordList)) --> This Messes Up The Order
    seen = set()
    seen_add = seen.add
    wordList = [i for i in wordList if not (i in seen or seen_add(i))]

def sortList():
    global wordList
    
    flushPrint("Sorting Dictionary Alphabetically")
    wordList = sorted(wordList)

def reverseList():
    global wordList
    
    flushPrint("Reversing Dictionary Items")
    wordList = list(reversed(wordList))

def uniqueOutFile(fName, fType):
    global dicFile
    global zipFile
    global compress
    global outFile
    
    if compress:
        checkFile = zipFile
        fType += '.' + zipType
    else:
        checkFile = dicFile
    if os.path.exists(checkFile):
        fList = list(fName)
        exists = True
        fName += '-{}'
        i = 1
        while exists:
            tempFile = (str(fName)+'.'+str(fType))
            tempFile = tempFile.format(i)
            if os.path.exists(tempFile):
                i += 1
            else:
                outFile = tempFile
                exists = False
    else:
        outFile = checkFile

def zipIt():
    global wordList
    global dicFile
    global zipFile
    global zipType
    global dicFileIn

    flushPrint("Zipping File")
    wordListStr = '\n'.join(wordList)
    
    if zipType == 'zip':
        with zipfile.ZipFile('%s' % (outFile), 'w', zipfile.ZIP_DEFLATED) as zf:
            try:
                zf.writestr(dicFileIn, wordListStr)
             finally:
                zf.close()
    elif zipType == 'tar' or zipType == 'tar.bz2' or zipType == 'tar.gz':
        if zipType == 'tar':
            mode = 'w'
        elif zipType == 'tar.bz2':
            mode = 'w:bz2'
        else:
            mode = 'w:gz'
        with tarfile.open('%s' % (outFile), '%s' % (mode), ) as zf:
            try:
                zfInfo = tarfile.TarInfo('%s' % (dicFileIn))
                zfInfo.size = len(wordListStr)
                zf.addfile(zfInfo, StringIO.StringIO(wordListStr))
             finally:
                zf.close()
    elif zipType == 'gz':
        with gzip.GzipFile('%s' % (outFile), 'w', compresslevel = 9) as zf:
            try:
                zf.writelines(wordListStr)
            finally:
                zf.close()
    elif zipType == 'bz2':
        with bz2.BZ2File('%s' % (outFile), 'w', compresslevel = 9) as zf:
            try:
                zf.writelines(wordListStr)
             finally:
                zf.close()

def taskComplete():
    global wordList
    global dicFile
    global zipType
    global zipFile
    global outFile
    global compress
    global dicFileIn
    
    dicFile = output_file
    dList = dicFile.split('/')
    dicFileIn = dList[len(dList)-1]

    dList2 = dicFileIn.split('.')
    if len(dList2[0]) < 1:
        dList2[0] = 'dymerged'
        dicFileIn = '.'.join(dList2)
        dList[len(dList)-1] = dicFileIn
        dicFile = '/'.join(dList)

    zipType = zip_type
    
    compress = False

    # to compress or to !compress
    if zipType != 'txt':
        compress = True
        
    f = dicFile.split('.')
    fName = f[0]
    # check if file format was inputed
    if len(f) > 1:
        fType = f[1]
    else:
        fName = dicFile
        fType = 'txt'
    
    # convert format into legit extension
    if zipType == 'bzip2':
        zipType = 'bz2'
    elif zipType == 'gzip':
        zipType = 'gz'
    elif zipType == 'bz2tar':
        zipType = 'tar.bz2'
    elif zipType == 'gztar':
        zipType = 'tar.gz'

    dicFile = (str(fName) + '.' + str(fType))
    zipFile = (str(dicFile) + '.' + str(zipType))

    uniqueOutFile(fName, fType)

    if not compress:
        try:
            with open(outFile, 'w+') as myFile:
                for word in wordList:
                    myFile.write(str(word)+'\n')
        except IOError: # Error --> "Invalid Output File Path"
            delayEffect()
            flushPrint("Invalid Path To Out File Given --> Please Enter a Valid Path", True, True)
            flushPrint("System Exit\n", True)
            raise SystemExit
    else:
        # validate compression file type
        formats = ['zip', 'bz2', 'gz', 'tar', 'tar.bz2', 'tar.gz']
        if zipType in formats:
            delayEffect()
            zipIt()
        else:
            delayEffect()
            flushPrint("Invalid Zip Format --> Please Enter A Valid Zip Format", True, True)
            flushPrint("Choose from --> 'zip', 'bz2', 'gz', 'tar', 'bz2tar', 'gztar'", True, True)
            flushPrint("System Exit\n", True)
            raise SystemExit

    flushPrint("Task Successfully Complete")
    delayEffect()
    saved = "Final Dictionary Saved As --> " + str(outFile)
    flushPrint(saved, False, True)
    print "\nComp/tional Time Elapsed:", (time.clock() - start)

def globalizeValues(o, i, z, s, u, r, f, a):
    global output_file
    global include_values
    global zip_type
    global sort
    global unique
    global reverse
    global fast
    global argv

    output_file = o
    include_values = i
    zip_type = z
    sort = s
    unique = u
    reverse = r
    fast = f
    argv = a

def main():

    global start
    global info
    global wordList

    start = time.clock()

    optparse.OptionParser.format_epilog = lambda self, formatter: self.epilog

    version = open('doc/VERSION').read().replace('\n','')
    info = 'DyMerge ' + version + ' Nikolaos Kamarinakis (nikolaskama.me)'
    
    examples = ('\nExamples:\n'+
                '  python dymerge.py /usr/share/wordlists/rockyou.txt /lists/cewl.txt -s -u\n' +
                '  python dymerge.py /lists/cewl.txt /lists/awlg.txt -s -u -i and,this\n' +
                '  python dymerge.py ~/fsocity.dic -u -r -o ~/clean.txt\n' +
                '  python dymerge.py /dicts/crunch.txt /dicts/john.txt -u -f -z bz2\n')
    
    parser = optparse.OptionParser(epilog=examples,
                                   usage='python %prog {dictionaries} [options]',
                                   prog='dymerge.py', version=('DyMerge ' + version))
    
    parser.add_option('-o', '--output', action='store', default='dymerged.txt',
                      dest='output_file', help='output filename')

    parser.add_option('-i', '--include', action='callback',
                      callback=appendListGenerator, type='string',
                      dest='include_values', help='include specified values in dictionary')

    parser.add_option('-z', '--zip', action='store', default='txt',
                      dest='zip_type', help='zip file with specified archive format')

    parser.add_option('-s', '--sort', action='store_true', default=False,
                      dest='sort', help='sort output alphabetically')

    parser.add_option('-u', '--unique', action='store_true', default=False,
                      dest='unique', help='remove dictionary duplicates')

    parser.add_option('-r', '--reverse', action='store_true', default=False,
                      dest='reverse', help='reverse dictionary items')

    parser.add_option('-f', '--fast', action='store_true', default=False,
                      dest='fast', help='finish task asap')

    (options, argv) = parser.parse_args()

    """
    print 'ARGV      :', sys.argv[1:]
    print 'OUTPUT    :', options.output_file
    print 'INCLUDE   :', options.include_values
    print 'ZIP       :', options.zip_type
    print 'SORT      :', options.sort
    print 'UNIQUE    :', options.unique
    print 'REVERSE   :', options.reverse
    print 'FAST      :', options.fast
    print 'DICTS     :', argv
    """
    output_file = options.output_file
    include_values = options.include_values
    zip_type = options.zip_type
    sort = options.sort
    unique = options.unique
    reverse = options.reverse
    fast = options.fast

    globalizeValues(options.output_file, options.include_values, \
                    options.zip_type, options.sort, options.unique, \
                    options.reverse, options.fast, argv)

    wordList = []

    displayLogo()

    argLen = len(sys.argv[1:])
    dicLen = len(argv)
    if argLen > 1 and dicLen > 0:

        flushPrint("Starting Dictionary Merge Task")

        readFiles()
        delayEffect()

        if include_values != None:
            includeValues()    
        delayEffect()

        if unique:
           makeUnique()
        delayEffect()

        if sort:
            sortList()
        delayEffect()

        if reverse:
            reverseList()
        delayEffect()

        taskComplete()
    
    elif argLen > 0 and dicLen < 1:
        flushPrint("No Dictionaries To Merge --> Use '-h' For Usage Help", True, True)
        flushPrint("System Exit\n", True)
    elif argLen > 0 and dicLen > 0 and dicLen < 2:
        flushPrint("No Options Selected --> Use '-h' For Usage Help", True, True)
        flushPrint("System Exit\n", True)
    else:
        flushPrint("Use '-h' Or '--help' For Usage Options")
        flushPrint("Run 'man' Command To View Man Page\n")

if __name__ == '__main__':
    main()
