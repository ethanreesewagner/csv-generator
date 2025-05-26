import google.generativeai as genai
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-2.0-flash')

def generate_csv(question):
    response = model.generate_content('''**Prompt Template:**
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
...
'''+"Right now, the user wants:"+question)
    print(response.text)
    file = open(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.csv', 'w')
    file.write(response.text.split("```")[1])
    print(f"{file.name}")
    return f"{file.name}"