"""
title: Chat with YouTube OpenAI Pipeline
author: BrainDrive.ai
date: 2024-10-30
version: 1.1
license: MIT
description: A custom pipeline that performs YouTube video search, retrieves transcripts, generates transcript summaries, conducts Q&A over transcripts, and searches within transcript/video content.
requirements: pydantic==2.7.4, requests, youtube-search==2.1.2, youtube-transcript-api==0.6.2, pytube==15.0.0, langchain==0.3.3, langchain-community==0.3.2, langchain-openai==0.2.2, langchain-core==0.3.10, langchain-text-splitters==0.3.0
"""

import os
import requests
import json
from typing import List, Sequence
from pydantic import BaseModel, Field
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import BaseTool, tool

class YoutubeSearchInput(BaseModel):
    query: str = Field(description="Search query for YouTube videos.")

@tool("search_youtube", args_schema=YoutubeSearchInput, return_direct=False)
def search_youtube(query: str) -> str:
    """Search YouTube and return video URLs based on the query."""
    from youtube_search import YoutubeSearch
    results = YoutubeSearch(query, 10).to_json()
    data = json.loads(results)
    return str([
        "https://www.youtube.com" + video["url_suffix"]
        for video in data["videos"]
    ])

class YoutubeTranscriptInput(BaseModel):
    youtube_url: str = Field(description="A valid YouTube video URL.")

@tool("get_youtube_transcript", args_schema=YoutubeTranscriptInput, return_direct=False)
def get_youtube_transcript(youtube_url: str) -> str:
    """Retrieve transcripts from the provided YouTube video URL."""
    from langchain_community.document_loaders import YoutubeLoader
    loader = YoutubeLoader.from_youtube_url(
        youtube_url, add_video_info=False, language=["en"], translation="en"
    )
    return "\n\n".join(map(repr, loader.load()))

class Pipeline:
    class Valves(BaseModel):
        OPENAI_API_BASE_URL: str = "https://api.openai.com/v1"
        OPENAI_API_KEY: str = ""
        OPENAI_API_MODEL: str = "gpt-4o"
        OPENAI_API_TEMPERATURE: float = 0.7
        AGENT_SYSTEM_PROMPT: str = (
            "You are a smart assistant that searches for YouTube videos, retrieves their transcripts, "
            "analyzes them, and assists users with Q&A over video content."
        )

    def __init__(self):
        self.name = "Chat with YouTube"
        self.tools = None
        self.valves = self.Valves(
            OPENAI_API_KEY=os.getenv("OPENAI_API_KEY", "")
        )
        self.pipelines = self.get_openai_models()

    def get_openai_models(self):
        if self.valves.OPENAI_API_KEY:
            try:
                headers = {
                    "Authorization": f"Bearer {self.valves.OPENAI_API_KEY}",
                    "Content-Type": "application/json"
                }
                response = requests.get(
                    f"{self.valves.OPENAI_API_BASE_URL}/models", headers=headers
                )
                models = response.json()
                return [
                    {"id": model["id"], "name": model.get("name", model["id"])}
                    for model in models["data"] if "gpt" in model["id"]
                ]
            except Exception as e:
                print(f"Error: {e}")
                return [{"id": "error", "name": "Could not fetch models from OpenAI."}]
        else:
            return []

    def pipe(self, user_message: str, model_id: str, messages: List[dict], body: dict):
        try:
            model = ChatOpenAI(
                base_url=self.valves.OPENAI_API_BASE_URL,
                api_key=self.valves.OPENAI_API_KEY,
                model=self.valves.OPENAI_API_MODEL,
                temperature=self.valves.OPENAI_API_TEMPERATURE
            )
            tools: Sequence[BaseTool] = [search_youtube, get_youtube_transcript]
            prompt = ChatPromptTemplate.from_messages([
                ("system", self.valves.AGENT_SYSTEM_PROMPT),
                MessagesPlaceholder("chat_history"),
                ("user", "{input}"),
                MessagesPlaceholder("agent_scratchpad")
            ])
            agent = create_tool_calling_agent(model, tools, prompt)
            agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
            response = agent_executor.invoke({"input": user_message, "chat_history": messages})
            return response["output"]
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            raise
