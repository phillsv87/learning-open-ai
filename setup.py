#!/usr/bin/env python3
import os
import openai
openai.organization = "org-U9kOBHRtp1lojwsorpPz7lr6"
openai.api_key = os.getenv("OPENAI_API_KEY")

print("Setup complete")