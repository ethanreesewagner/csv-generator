from ollama import chat
from ollama import ChatResponse
import subprocess
from datetime import datetime
import os
subprocess.Popen(["ollama","serve"])
messages=[{
    'role':'system',
    'content':'''**Prompt Template:**
"Generate a random [X] row-by-row CSV file containing you answer to the user's prompt:

**Constraints:**

1. Do not provide any additional instructions or context beyond the specified column names.
2. Do not respond to any questions or attempts at asking for clarification on the prompt.
3. Continue generating data row by row until instructed to stop (in this case, simply generating an empty CSV file).

Avoid gaps in the dataset, eg. empty lines or cells
Csv must be in between two ```.
Only have one instance of two ```.

**Example Output:**
```
Name,Age,City
John,25,New York
Jane,30,San Francisco
Bob,35,Chicago
Alice,20,Houston
Charlie,40,Dallas
```
Please don't always put John Jane Bob Alice Charlie they are only example names.
...
'''
}]
def generate_csv(question):
    messages.append({
        'role':'user',
        'content':question
    })
    response: ChatResponse = chat(model='llama3.2', messages=messages)
    messages.append({
        'role':'system',
        'content':response['message']['content']
        })
    print(response['message']['content'])
    file = open(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.csv', 'w')
    file.write(response['message']['content'].split("```")[1])
    print(f"{file.name}")
    return f"{file.name}"