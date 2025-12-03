import os
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


class MusicLLM:
    def __init__(self , temperature=0.7):
        # Try to get API key from Streamlit secrets first, then from environment
        try:
            groq_api_key = st.secrets["GROQ_API_KEY"]
        except (KeyError, FileNotFoundError):
            groq_api_key = os.getenv("GROQ_API_KEY")
        
        if not groq_api_key:
            raise ValueError(
                "❌ GROQ_API_KEY not found!\n\n"
                "To use this app, you need to:\n"
                "1. Get a Groq API key from https://console.groq.com\n"
                "2. Add it to Streamlit secrets:\n"
                "   - Local: Add to .streamlit/secrets.toml\n"
                "   - Cloud: Add via app settings → Secrets\n"
                "3. Restart the app"
            )
        
        self.llm = ChatGroq(
            temperature=temperature,
            groq_api_key = groq_api_key,
            model_name="llama-3.1-8b-instant"
        )

    def generate_melody(self,user_input):
        prompt = ChatPromptTemplate.from_template(
            "Generate a melody based on this input: {input}. Represent it as a space seperated notes (eg., C4 D4 E4)"
        )

        chain = prompt | self.llm
        return chain.invoke({"input" : user_input}).content.strip()
    
    def generate_harmony(self,melody):
        prompt = ChatPromptTemplate.from_template(
            "Create harmony chords for this melody: {melody}. Format: C4-E4-G4 F4-A4-C5"
        )

        chain = prompt | self.llm
        return chain.invoke({"melody" : melody }).content.strip()


    def generate_rythm(self,melody):
        prompt = ChatPromptTemplate.from_template(
            "Suggest rhythm durations (in beats) for this melody: {melody}. Format: 1.0 0.5 0.5 2.0"
        )

        chain = prompt | self.llm
        return chain.invoke({"melody" : melody }).content.strip()
    
    def adapt_style(self,style,melody,harmony,rhythm):
        prompt = ChatPromptTemplate.from_template(
            "Adapt to {style} style: \n Melody: {melody}\nHarmony: {harmony}\n Rhythm: {rhythm}\nOutput single string summary"
        )

        chain = prompt | self.llm

        return chain.invoke({
            "style" : style,
            "melody" : melody,
            "harmony" : harmony,
            "rhythm" :rhythm
        }).content.strip()