#!/usr/bin/env python3
import setup
import openai
from lib import bcolors

partialSentence=input("Enter part of a sentence to complete:\n")

result=openai.Completion.create(
    prompt=partialSentence,
    engine="davinci")

print("Full Result")
print(result)

print("\n\nCompletion")
print(f"{bcolors.OKCYAN}{partialSentence}{bcolors.OKGREEN}{result.choices[0].text}{bcolors.ENDC}")