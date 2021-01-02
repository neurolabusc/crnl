#!/usr/bin/env python3
import re
import sys
import os

if __name__ == '__main__':
    """
    test decompression speed and accuracy of files in folder indir
    
    Parameters
    ----------
    indir : str
        folder with uncompressed files to test (default, './corpus')     
        
    """
    indir = './'
    if len(sys.argv) > 1:
        indir = sys.argv[1]    
    os.chdir(indir)
    fin = open("drupal.txt", "rt")
    #output file to write the result to
    fout = open("index.rst", "wt")
    #for each line in the input file
    for line in fin:
        #read replace the string and write to output file
        line = line.replace('<li>', '\n - ')
        line = line.replace('</li>', '')
        line = line.replace('<strong>', '**')
        line = line.replace('</strong>', '** ')
        line = line.replace('<b>', '**')
        line = line.replace('</b>', '**')
        line = line.replace('<span>', '')
        line = line.replace('</span>', '')
        line = line.replace('<ul>', '')
        line = line.replace('<h2>', '\n')
        line = line.replace('</h2>', '\n-------------------------------------------\n')
        line = line.replace('<h3>', '\n')
        line = line.replace('</h3>', '\n-------------------------------------------\n')     
        line = line.replace('<p>', '\n')
        line = line.replace('</p>', '\n')
        line = line.replace('</ul>', '\n')
        line = line.replace('<ol>', '\n')
        line = line.replace('</ol>', '\n')
        line = line.replace('<br>', '\n')
        line = line.replace('</br>', '')
        line = line.replace('<br />', '\n - ')
        line = line.replace('</div>', '')
        line = line.replace('<h1>', '')
        line = line.replace('</h1>', '')
        line = line.replace('&nbsp;', '')
        line = (re.sub(r'<div.*?>', '', line))
        line = (re.sub(r'<h2.*?>', '', line)) 
        line = (re.sub(r'<p class=.*?>', '', line))
        line = (re.sub(r'\[\[.*?\]\]', '', line))
        #txts = re.findall(r'\">??([^\'"a>]+)', line) #// >PWI page.</a>
        #links = re.findall(r'href=[\'"]?([^\'" >]+)', line) #//<a href="
        #links = re.findall(r'href=[\'"]?([^\'" >]+)', line) #//<a href="
        #links = re.findall(r"href(.*?)\<\/a\>", line) #//<a href="
        links = re.findall(r"\<a href\=\"(.*?)\<\/a\>", line) #//<a href="
        for link in links:
            #print(link)
            #http://www.ge.com">home
            # -> http://www.ge.com
            url = link[:link.find('">')]
            nam = link[link.find('">')+2:]
            sphx = ' `'+nam+' <'+url+'>`_ '
            #print(sphx)
            #rep = '<a href="'+link+'</a>'
            rep = '<a href="'+link+'</a>'
            print(rep + ' -> ' + sphx)
            line = (re.sub(rep, sphx, line))
            #line = (re.sub(r'"(.*)"', '\u201c\\1\u201d', '"Quoted String"')'“Quoted String”' 
        fout.write(line)

    fin.close()
    fout.close()