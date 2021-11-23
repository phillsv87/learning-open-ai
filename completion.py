#!/usr/bin/env python3
import setup
import openai

print(openai.Completion.create(prompt="I'm on my way to Las Vegas and I'm going to",engine="davinci"))
