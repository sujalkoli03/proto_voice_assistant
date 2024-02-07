import os
import openai
from key import apikey
openai.api_key = apikey

resp = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "generate email for resignation"
    },
    {
      "role": "assistant",
      "content": "Subject: Resignation Letter\n\nDear [Recipient's Name],\n\nI hope this email finds you well. It is with mixed emotions that I write to you today to formally tender my resignation from my position at [Company Name]. After careful consideration, I have made the difficult decision to pursue new opportunities and hence, resign from my current role.\n\nI want to express my gratitude for the invaluable experiences and growth opportunities that I have had during my time at [Company Name]. I truly appreciate the trust and support"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(resp)