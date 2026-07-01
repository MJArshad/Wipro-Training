#!/usr/bin/env python3
"""
Personal Research Assistant Agent

Demonstrates LangChain's ReAct (Reason + Act) pattern with:
- Web search capability
- Calculator tool
- Citation tracking
- Claude API integration
"""

import os
import json
from typing import Any
from dotenv import load_dotenv

from langchain_anthropic import ChatAnthropic
from langchain_core.tools import tool
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Load environment variables
load_dotenv()

# ============================================================================
# TOOLS DEFINITION
# ============================================================================

@tool
def web_search(query: str) -> str:
    """Search the web for information about a topic.

    Args:
        query: The search query string

    Returns:
        Search results with sources
    """
    try:
        from duckduckgo_search import DDGS

        ddgs = DDGS()
        results = ddgs.text(query, max_results=3)

        formatted_results = []
        for i, result in enumerate(results, 1):
            formatted_results.append(
                f"[{i}] {result['title']}\n"
                f"URL: {result['href']}\n"
                f"Summary: {result['body'][:200]}...\n"
            )

        return "\n".join(formatted_results) if formatted_results else "No results found."
    except ImportError:
        return "Web search temporarily unavailable. Please use local knowledge."


@tool
def calculator(expression: str) -> str:
    """Perform mathematical calculations.

    Args:
        expression: A valid Python mathematical expression

    Returns:
        The calculated result
    """
    try:
        result = eval(expression, {"__builtins__": {}})
        return f"Result: {result}"
    except Exception as e:
        return f"Calculation error: {str(e)}"


@tool
def retrieve_local_context(topic: str) -> str:
    """Retrieve information from local knowledge base.

    Args:
        topic: The topic to retrieve information about

    Returns:
        Relevant local context
    """
    knowledge_base = {
        "python": "Python is a high-level, interpreted programming language known for simplicity and readability.",
        "langchain": "LangChain is a framework for developing applications powered by large language models.",
        "agents": "Agents are LLMs that can reason about tasks and use tools to accomplish goals.",
    }

    topic_lower = topic.lower()
    for key, value in knowledge_base.items():
        if key in topic_lower:
            return value
    return f"No local context available for '{topic}'."


# ============================================================================
# AGENT SETUP
# ============================================================================

def create_research_agent():
    """Create and return a configured research agent."""

    # Initialize LLM
    llm = ChatAnthropic(
        model="global.anthropic.claude-haiku-4-5-20251001-v1:0",
        temperature=0.7,
        base_url="https://llmgw-wp.tekstac.com",
        api_key=os.getenv("ANTHROPIC_API_KEY")
    )

    # Define tools
    tools = [web_search, calculator, retrieve_local_context]

    # Create system prompt
    system_prompt = """You are a helpful research assistant. Your goal is to answer user questions by:

1. Breaking down the question into sub-tasks
2. Using available tools when appropriate (web search for current info, calculator for math, local context for general knowledge)
3. Synthesizing information from multiple sources
4. Providing citations and sources where relevant
5. Being honest about what you don't know

When using web_search, cite the sources. Always explain your reasoning before taking action.
Format final answers clearly with key findings and their sources."""

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder("chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ])

    # Create agent
    agent = create_tool_calling_agent(llm, tools, prompt)

    # Create executor with verbose output
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        max_iterations=10,
        early_stopping_method="force"
    )

    return agent_executor


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Run interactive research agent sessions."""

    print("=" * 70)
    print("Personal Research Assistant Agent")
    print("=" * 70)
    print("\nType 'quit' to exit\n")

    agent = create_research_agent()

    # Example queries
    queries = [
        "What is Claude 3.5 Sonnet and how does it differ from GPT-4?",
        "Calculate the compound interest on $1000 at 5% annual rate for 3 years",
        "What is LangChain and what problem does it solve?",
    ]

    for query in queries:
        print(f"\n{'='*70}")
        print(f"Query: {query}")
        print('='*70)

        try:
            response = agent.invoke({"input": query})
            output = response['output']

            # Extract text from response (handles both string and list formats)
            if isinstance(output, list) and len(output) > 0:
                if isinstance(output[0], dict) and 'text' in output[0]:
                    text_output = output[0]['text']
                else:
                    text_output = str(output[0])
            else:
                text_output = str(output)

            print(f"\nAgent Response:\n{text_output}")
        except Exception as e:
            print(f"Error: {e}")

        print()


if __name__ == "__main__":
    main()
