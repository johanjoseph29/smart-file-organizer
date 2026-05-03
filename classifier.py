import os
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate

from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="gemma3:4b")

# Prompt template
prompt_template = PromptTemplate(
    input_variables=["filename"],
    template="""
You are an intelligent file organizer.

Classify the file into ONE category:
Study, movie, Code, Images, Docs, Others

Rules:
- Study → academic (OS, DBMS, notes)
- Bills → mp4 and other formats
- Code → programming files
- Images → photos, screenshots
- Docs → general documents

Respond ONLY with category name.

Filename: {filename}
"""
)


def classify_file(file_path):
    filename = os.path.basename(file_path)

    prompt = prompt_template.format(filename=filename)

    try:
        response = llm.invoke(prompt).strip()

        valid = ["Study", "movie", "Code", "Images", "Docs", "Others"]

        for v in valid:
            if v.lower() in response.lower():
                return v

    except Exception as e:
        print("⚠️ LLM error:", e)

    return "Others"