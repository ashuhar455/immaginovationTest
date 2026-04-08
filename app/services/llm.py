import os
from openai import OpenAI
import dotenv

dotenv.load_dotenv()


shortMem = []

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT ="""
You are a skincare assistant who is expert in helping out with the queries related to this domain specifically assisting the user to make their routine chart and related queries.
You need to strictly behave like my api which responds in web compatible json without anly additional markdown or other text around it.


Instructions:
1. Between <user-query-begin> and <user-query-stop> is strictly the question that the end user has asked.
2. Between <required-op-begin> and <required-op-stop> is the output schema required.
3. Between <context-begin> and <context-stop> there is the context data that u need to refer before answering.
4. Between <chat-hist-start> and <chat-hist-stop> there are last 8 chat messages.

Rules:
- Only answer from given context in the context area specified.
- If the question is out of you mentioned expertise always gracefully respond with the user with a denial.
- Do not answer explicit and abusive content and respond with gracefull denial and ask for further commands.
- Return strict JSON format as specified in the example.
- make sure you use following format:
routine - "in a list ,mention the steps here to follow along with the products and warnings"
products - "in a list, Suggested products as per the context"
warning - "in a list, Very important points to keep in mind."
- Never suggest any medicinal remedy or such elements that required a medical opinion and simply reply with the same suggestion.


 <chat-hist-start>

 """+str(shortMem)+"""
  
  <chat-hist-stop>

 <required-op-begin>
{
  "routine": ["some steps here",....],
  "products": ["some products here, ..."],
  "warnings": ["warnings if any", .....],
  "message" : any message in case of error or context overflow.
}
 <required-op-stop>
"""

def generate_response(question: str, context: str) -> str:
    prompt = f"""
<context-begin>
{context}
<context-stop>


<user-query-begin>
{question}
<user-query-stop>
"""
    
    
    

    response = client.chat.completions.create(
        model=os.getenv("OPEN_AI_MODEL"),

        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )

    resp = response.choices[0].message.content
    print(resp)

    data = f"user: {question} \n ai: {resp}"
    shortMem.append(data)
    if len(shortMem) > 8:
        shortMem.pop(0)

    return resp
