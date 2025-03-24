from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

#create app instance
app = FastAPI()

#CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

#find insult func
def findinsult(word):
    with open('insult.txt', 'r') as f: #opens insult.txt
        lines = f.readlines() #reads all of the lines
        for row in lines: #for each line attempts to match to phrase (word)
            if row.find(str(word)) != -1: # if they find the phrase then it returns its pos
                return lines.index(row)

@app.get("/")
async def root():
    #opens files and then puts the contents in a variable
    with open('insult.txt', 'r') as f:
        text = f.readlines()
        length = len(text) #gets length of file in lines
    
    insult = random.choice(text).strip("\n") #takes a random line from the file and strips of newlines
    return { #data the user wil receive
        "insult": insult,
        "insultpos": f'Insult {(findinsult(insult))+1} out of {length}' #uses the findinsult func to get the position of the insult 
        }
