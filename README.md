# Production HR Policy Chatbot

```markdown
# Production HR Policy Chatbot

## Overview
An enterprise HR chatbot that answers employee questions directly from HR policy documents using Retrieval-Augmented Generation (RAG).

## Features
- HR document understanding
- Policy question answering
- Conversational memory
- PDF document retrieval
- Accurate context-based responses

## Tech Stack
- Python
- LangChain
- Ollama
- FAISS
- PyPDFLoader

## Problem Solved
Employees often spend time searching lengthy HR documents for answers. This chatbot provides instant answers from HR policies.

## Workflow
1. Load HR Policy PDFs
2. Split documents into chunks
3. Generate embeddings
4. Store vectors in FAISS
5. Retrieve relevant policies
6. Generate accurate responses

## Skills Demonstrated
- Enterprise AI Solutions
- HR Automation
- RAG Systems
- Document Intelligence
- Vector Search

## Installation

```bash
pip install langchain faiss-cpu pypdf
