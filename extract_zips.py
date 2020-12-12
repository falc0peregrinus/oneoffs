# Extracts all zip files in a specified directory.
# If a zip file has already been extracted, the program will overwrite the old extracted file with
# a newly-extracted file.
    
import os
from zipfile import ZipFile
from zipfile import BadZipFile
        
if __name__ == '__main__':
    # Define the path for the directory using a raw string.
    pathName = r"*****"
    
    # Count the number of extracted files so that the info can be displayed after extractions are complete.
    # If a file cannot be extracted, it will be skipped and counted as notExtracted instead.
    numExtracted = 0
    numNotExtracted = 0
    
    # Set a flag that becomes True when a BadZipFile exception is thrown.
    # This allows correct counting of files that were extracted.
    exceptionRaised = False
    
    # Get the contents of the designated directory, in this case pathName as defined above
    with os.scandir(pathName) as contents:
        for file in contents:
            
            # If the file is a zip file as determined by file type, then extract the file
            if file.is_file() and file.name.endswith(".zip"):
                try: #Catch a BadZipFile exception
                    with ZipFile(pathName+"\\"+file.name, "r") as zipObj:
                        zipObj.extractall(pathName)
                except BadZipFile as e:
                    exceptionRaised = True
                    numNotExtracted+=1 #Increment count of files not extracted
                    print("Could not extract file: ",file.name," {}".format(e))
                    
                if(exceptionRaised is False):
                    # Increment count of extracted files only if no exception was raised
                    numExtracted+=1

                    # Then indicate that the file has been extracted
                    print("Extracted: ",file.name)

                #Reset exception flag
                exceptionRaised = False
    
    # After all zip files have been touched, print the number of files extracted and the number not extracted.
    print("\nZip files extracted: ",numExtracted)
    print("Not extracted: ",numNotExtracted)