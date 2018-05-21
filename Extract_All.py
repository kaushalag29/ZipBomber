#!/usr/bin/env python
import os
import io
import zipfile
#Code Used From Stackoverflow
def extract(filename):
    z = zipfile.ZipFile(filename)
    for f in z.namelist():
        # get directory name from file
        dirname = os.path.splitext(f)[0]  
        # create new directory
        os.mkdir(dirname)  
        # read inner zip file into bytes buffer 
        content = io.BytesIO(z.read(f))
        zip_file = zipfile.ZipFile(content)
        for i in zip_file.namelist():
            zip_file.extract(i, dirname)
extract("Zipbomb.zip")


