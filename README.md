# ISL Sentence Normalization

This module converts Indian Sign Language (ISL) keyword sequences
into proper English sentences using a local Large Language Model (LLM).

## Problem Statement
Gesture recognition models produce ISL keywords, which are not
grammatically correct English sentences and are difficult to
translate directly into regional languages.

## Solution
A sentence normalization module is implemented using a local LLM
(Ollama with Mistral) to convert ISL keyword sequences into
meaningful English sentences while preserving the original meaning.

## System Flow
ISL Keywords → LLM-based Sentence Normalization → English Sentence

## Technologies Used
- Python
- Ollama (Local LLM Runtime)
- Mistral Language Model

## How to Run
1. Install Ollama from https://ollama.com
2. Pull the model:
3. ollama pull mistral
4. pip install ollama
