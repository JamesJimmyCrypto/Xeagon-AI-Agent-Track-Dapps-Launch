import os
import requests
import getpass

# Set up environment variables for the CDP toolkit
# Replace these with your actual credentials
if not os.getenv("CDP_API_KEY_NAME"):
    os.environ["CDP_API_KEY_NAME"] = getpass.getpass("CDP_API_KEY_NAME")
if not os.getenv("CDP_API_KEY_PRIVATE_KEY"):
    os.environ["CDP_API_KEY_PRIVATE_KEY"] = getpass.getpass("CDP_API_KEY_PRIVATE_KEY: ")

# Optional: Set network (defaults to base-sepolia)
os.environ["NETWORK_ID"] = "base-sepolia"  # or "base-mainnet"

# Set up OpenAI API key for LLM (Replace with your actual key)
os.environ["OPENAI_API_KEY"] = ""

########################################
# CDP Toolkit initialization
########################################
from cdp_langchain.agent_toolkits import CdpToolkit
from cdp_langchain.utils import CdpAgentkitWrapper

# Initialize CDP wrapper
cdp = CdpAgentkitWrapper()

# Create toolkit from wrapper
cdp_toolkit = CdpToolkit.from_cdp_agentkit_wrapper(cdp)
cdp_tools = cdp_toolkit.get_tools()

########################################
# Additional Tools and LLM Setup
########################################
from langchain_community.document_loaders import RSSFeedLoader
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.tools import tool
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

llm = ChatOpenAI(temperature=1, model="gpt-4o-mini")


def generate_gemini(system, messages):
    import google.generativeai as genai
    from google.generativeai.types import HarmCategory, HarmBlockThreshold

    safe = {
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    }
    GOOGLE_API_KEY = ""  # Replace with your actual Google PaLM key
    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro-002",
        system_instruction=system,
        safety_settings=safe,
    )

    response = model.generate_content(
        messages, generation_config=genai.types.GenerationConfig(temperature=1)
    )
    return response.text


@tool
def reddit_search(session_id: str, query: str):
    """
    This function is used to search for a query on Reddit.
    """
    try:
        url = "https://reddit3.p.rapidapi.com/v1/reddit/search"

        querystring = {
            "search": query,
            "filter": "posts",
            "timeFilter": "month",
            "sortType": "relevance",
        }

        headers = {
            "x-rapidapi-key": "",  # Replace with your RapidAPI key for Reddit
            "x-rapidapi-host": "reddit3.p.rapidapi.com",
        }

        response = requests.get(url, headers=headers, params=querystring)

        if response.status_code == 200:
            response = response.json()
            extracted_data = []
            for post in response["body"]:
                title = post.get("title", "No title provided")
                selftext = post.get("selftext", "No text provided")
                url = post.get("url", "No URL provided")
                selftext_html = post.get("selftext_html", "No HTML provided")

                extracted_post = {
                    "title": title,
                    "selftext": selftext,
                    "selftext_html": selftext_html,
                }
                extracted_data.append(extracted_post)

            res = generate_gemini(
                f"You are insights extractor and you are tasked to understand raw data and output the given query: {query}",
                [
                    f"Here is the Raw data from sources that fetched for the query {query}, use below information to answer\n\n<data>{str(extracted_data)}<data> output all the good insights that are useful to answer the query"
                ],
            )

            return res

        return "No data found"

    except Exception as e:
        return f"Error while searching on reddit: {e}"


@tool
def twitter(session_id: str, topic: str):
    """
    This function is used to search a topic on Twitter.
    """
    try:
        url = "https://twitter-api47.p.rapidapi.com/v2/search"

        querystring = {"query": topic, "type": "Latest"}
        headers = {
            "x-rapidapi-key": "",  # Replace with your RapidAPI key for Twitter
            "x-rapidapi-host": "twitter-api47.p.rapidapi.com",
        }

        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            response = response.json()
            extracted_data = []
            for tweet in response["tweets"]:

                legacy = tweet.get("legacy", {})
                full_text = legacy.get("full_text", "")
                urls = legacy.get("entities", {}).get("urls", [])
                user_id = legacy.get("user_id_str", "")
                conv_id = legacy.get("conversation_id_str", "")
                twitter_post_url = f"https://x.com/{user_id}/status/{conv_id}"

                link = urls[0].get("expanded_url") if urls else ""

                extracted_data.append(
                    {
                        "text": full_text,
                        "link": link,
                        "twitter_post_url": twitter_post_url,
                    }
                )
            res = generate_gemini(
                f"You are insights extractor and you are tasked to understand raw data and output the given query: {topic}",
                [
                    f"Here is the Raw data from sources that fetched for the query {topic}, use below information to answer\n\n<data>{str(extracted_data)}<data> output all the good insights that are useful to answer the query"
                ],
            )

            return res

        return "No data found"

    except Exception as e:
        return f"Error while searching on twitter: {e}"


@tool
def rss_listener(session_id: str):
    urls = [
        "https://www.coindesk.com/arc/outboundfeeds/rss",
    ]
    loader = RSSFeedLoader(urls=urls)
    data = loader.load()
    out = generate_gemini(
        [
            "Analyze data and help me understand if there are any potential BUY/SELL events for any of the altcoins"
        ],
        data[0].page_content,
    )
    return out

all_tools = cdp_tools + [reddit_search, twitter, rss_listener]

# Initialize the agent with all tools
agent_executor = create_react_agent(llm, all_tools)

example_query = "Send 0.005 ETH to john2879.base.eth"
events = agent_executor.stream(
    {"messages": [("user", example_query)]},
    stream_mode="values",
)

for event in events:
    # Print agent response as it streams
    event["messages"][-1].pretty_print()
