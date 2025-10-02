# import streamlit as st
# from langchain.agents import initialize_agent, Tool
# from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
# from langchain_community.tools import DuckDuckGoSearchRun
# from langchain_community.utilities.sql_database import SQLDatabase
# from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
# from langchain_groq import ChatGroq
# from dotenv import load_dotenv
# import os

# # Page configuration
# st.set_page_config(
#     page_title="Multi-Search Engine",
#     page_icon="🧠",
#     layout="wide"
# )

# # Load environment variables
# load_dotenv()

# # Sidebar - Configuration
# with st.sidebar:
#     st.header("⚙️ Configuration")
    
#     groq_api_key = st.text_input(
#         "Groq API Key",
#         type="password",
#         value=os.getenv("GROQ_API_KEY", ""),
#         help="Enter your Groq API key"
#     )
    
#     if groq_api_key:
#         os.environ["GROQ_API_KEY"] = groq_api_key

# # Main header
# st.title("🧠 Multi-Search-Engine With Langchain")
# st.markdown("Choose a tool and ask your question:")

# # Tool selection tabs
# tab1, tab2, tab3 = st.tabs(["🌐 DuckDuckGo Search", "📚 Wikipedia", "🗄️ SQL Database"])

# # Initialize LLM
# def get_llm():
#     if not groq_api_key:
#         st.error("Please enter your Groq API key in the sidebar")
#         return None
#     return ChatGroq(
#         groq_api_key=groq_api_key,
#         model="llama-3.1-8b-instant"
#     )

# # Tab 1: DuckDuckGo Search
# with tab1:
#     st.subheader("🌐 Ask using DuckDuckGo Search")
#     st.markdown("Enter your query for DuckDuckGo")
    
#     ddg_query = st.text_input(
#         "Your question:",
#         key="ddg_input",
#         placeholder="e.g., What are the latest top ranking movies of 2025?"
#     )
    
#     if st.button("Search", key="ddg_search"):
#         if not groq_api_key:
#             st.error("⚠️ Please configure your Groq API key in the sidebar")
#         elif ddg_query:
#             with st.spinner("Searching..."):
#                 try:
#                     llm = get_llm()
#                     search = DuckDuckGoSearchRun()
#                     search_tool = Tool(
#                         name="DuckDuckGo Search",
#                         func=search.run,
#                         description="Use this tool to perform web searches using DuckDuckGo"
#                     )
                    
#                     agent = initialize_agent(
#                         tools=[search_tool],
#                         llm=llm,
#                         agent_type="zero-shot-react-description",
#                         verbose=True,
#                         max_iterations=5,
#                         max_execution_time=60,
#                         early_stopping_method="generate",
#                         handle_parsing_errors=True
#                     )
                    
#                     response = agent.run(ddg_query)
                    
#                     st.success("✅ Search Complete!")
#                     st.markdown("### Response:")
#                     st.write(response)
                    
#                 except Exception as e:
#                     st.error(f"❌ Error: {str(e)}")
#         else:
#             st.warning("⚠️ Please enter a query")

# # Tab 2: Wikipedia Search
# with tab2:
#     st.subheader("📚 Ask using Wikipedia")
#     st.markdown("Enter your query for Wikipedia")
    
#     wiki_query = st.text_input(
#         "Your question:",
#         key="wiki_input",
#         placeholder="e.g., Tell me about Elon Musk"
#     )
    
#     if st.button("Search", key="wiki_search"):
#         if not groq_api_key:
#             st.error("⚠️ Please configure your Groq API key in the sidebar")
#         elif wiki_query:
#             with st.spinner("Searching Wikipedia..."):
#                 try:
#                     llm = get_llm()
#                     wiki = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=800)
                    
#                     wiki_search_tool = Tool(
#                         name="Wikipedia Search",
#                         func=wiki.run,
#                         description="Use this tool to search Wikipedia for concise information."
#                     )
                    
#                     agent = initialize_agent(
#                         tools=[wiki_search_tool],
#                         llm=llm,
#                         agent_type="zero-shot-react-description",
#                         verbose=True,
#                         max_iterations=5,
#                         max_execution_time=60,
#                         early_stopping_method="generate",
#                         handle_parsing_errors=True
#                     )
                    
#                     response = agent.run(wiki_query)
                    
#                     st.success("✅ Search Complete!")
#                     st.markdown("### Response:")
#                     st.write(response)
                    
#                 except Exception as e:
#                     st.error(f"❌ Error: {str(e)}")
#         else:
#             st.warning("⚠️ Please enter a query")

# # Tab 3: SQL Database
# with tab3:
#     st.subheader("🗄️ Ask using SQL Database")
#     st.markdown("Query your database using natural language")
    
#     # Database file upload or path
#     db_path = st.text_input(
#         "Database Path:",
#         value="example_new.db",
#         help="Enter the path to your SQLite database file"
#     )
    
#     sql_query = st.text_input(
#         "Your question:",
#         key="sql_input",
#         placeholder="e.g., How many units of product Laptop are in stock?"
#     )
    
#     if st.button("Query", key="sql_search"):
#         if not groq_api_key:
#             st.error("⚠️ Please configure your Groq API key in the sidebar")
#         elif sql_query:
#             with st.spinner("Querying database..."):
#                 try:
#                     llm = get_llm()
#                     db = SQLDatabase.from_uri(f"sqlite:///{db_path}")
                    
#                     toolkit = SQLDatabaseToolkit(db=db, llm=llm)
#                     tools = toolkit.get_tools()
                    
#                     agent = initialize_agent(
#                         tools=tools,
#                         llm=llm,
#                         agent_type="zero-shot-react-description",
#                         verbose=True,
#                         max_iterations=10,
#                         max_execution_time=120,
#                         early_stopping_method="generate",
#                         handle_parsing_errors=True
#                     )
                    
#                     response = agent.run(sql_query)
                    
#                     st.success("✅ Query Complete!")
#                     st.markdown("### Response:")
#                     st.write(response)
                    
#                 except Exception as e:
#                     st.error(f"❌ Error: {str(e)}")
#         else:
#             st.warning("⚠️ Please enter a query")

# # Footer
# st.markdown("---")
# st.markdown(
#     "<div style='text-align: center; color: gray;'>"
#     "Built with Streamlit & LangChain | Powered by Groq"
#     "</div>",
#     unsafe_allow_html=True
# )








import streamlit as st
from langchain.agents import initialize_agent, Tool, AgentExecutor
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

# Page configuration
st.set_page_config(
    page_title="Multi-Search Engine",
    page_icon="🧠",
    layout="wide"
)

# Load environment variables
load_dotenv()

# Sidebar - Configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    groq_api_key = st.text_input(
        "Groq API Key",
        type="password",
        value=os.getenv("GROQ_API_KEY", ""),
        help="Enter your Groq API key"
    )
    
    if groq_api_key:
        os.environ["GROQ_API_KEY"] = groq_api_key
    
    st.markdown("---")
    st.markdown("### 💡 Tips")
    st.info("""
    **DuckDuckGo**: Best for recent news, current events
    
    **Wikipedia**: Best for historical facts, biographies, general knowledge
    
    **SQL Database**: Query your data in natural language
    """)

# Main header
st.title("🧠 Multi-Search-Engine With Langchain")
st.markdown("Choose a tool and ask your question:")

# Initialize LLM
def get_llm():
    if not groq_api_key:
        st.error("Please enter your Groq API key in the sidebar")
        return None
    return ChatGroq(
        groq_api_key=groq_api_key,
        model="llama-3.1-8b-instant",
        temperature=0
    )

# Tool selection tabs
tab1, tab2, tab3 = st.tabs(["🌐 DuckDuckGo Search", "📚 Wikipedia", "🗄️ SQL Database"])

# Tab 1: DuckDuckGo Search
with tab1:
    st.subheader("🌐 Ask using DuckDuckGo Search")
    st.markdown("*Perfect for: Recent news, current events, latest information*")
    
    ddg_query = st.text_input(
        "Your question:",
        key="ddg_input",
        placeholder="e.g., What are the latest top ranking movies of 2025?"
    )
    
    if st.button("Search", key="ddg_search", type="primary"):
        if not groq_api_key:
            st.error("⚠️ Please configure your Groq API key in the sidebar")
        elif ddg_query:
            with st.spinner("🔍 Searching the web..."):
                try:
                    llm = get_llm()
                    search = DuckDuckGoSearchRun()
                    search_tool = Tool(
                        name="DuckDuckGo_Search",
                        func=search.run,
                        description="Useful for finding current information, recent news, and real-time data from the web."
                    )
                    
                    # Create agent with better configuration
                    agent = initialize_agent(
                        tools=[search_tool],
                        llm=llm,
                        agent_type="zero-shot-react-description",
                        verbose=False,  # Set to False for cleaner output in Streamlit
                        max_iterations=3,
                        max_execution_time=30,
                        early_stopping_method="generate",
                        handle_parsing_errors=True
                    )
                    
                    # Add error handling for the agent run
                    try:
                        response = agent.run(ddg_query)
                        st.success("✅ Search Complete!")
                        st.markdown("### 📄 Response:")
                        st.write(response)
                    except Exception as agent_error:
                        st.warning("⚠️ Agent encountered an issue. Using direct search...")
                        # Fallback to direct search
                        direct_result = search.run(ddg_query)
                        st.success("✅ Direct Search Result:")
                        st.write(direct_result)
                    
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
                    st.info("💡 Try rephrasing your question or make it more specific.")
        else:
            st.warning("⚠️ Please enter a query")

# Tab 2: Wikipedia Search
with tab2:
    st.subheader("📚 Ask using Wikipedia")
    st.markdown("*Perfect for: Historical facts, biographies, general knowledge*")
    
    wiki_query = st.text_input(
        "Your question:",
        key="wiki_input",
        placeholder="e.g., Who is Elon Musk? or History of artificial intelligence"
    )
    
    col1, col2 = st.columns([1, 4])
    with col1:
        search_wiki = st.button("Search", key="wiki_search", type="primary")
    
    if search_wiki:
        if not groq_api_key:
            st.error("⚠️ Please configure your Groq API key in the sidebar")
        elif wiki_query:
            # Check if query is about recent events
            recent_keywords = ["2024", "2025", "latest", "recent", "today", "current", "news"]
            if any(keyword in wiki_query.lower() for keyword in recent_keywords):
                st.warning("⚠️ Wikipedia may not have information about very recent events. Consider using DuckDuckGo Search for latest information.")
            
            with st.spinner("📖 Searching Wikipedia..."):
                try:
                    llm = get_llm()
                    wiki = WikipediaAPIWrapper(
                        top_k_results=2,
                        doc_content_chars_max=1000
                    )
                    
                    # Try direct Wikipedia search first
                    try:
                        wiki_result = wiki.run(wiki_query)
                        
                        # Use LLM to summarize the result
                        summary_prompt = f"""Based on this Wikipedia information, answer the question: {wiki_query}

Wikipedia Information:
{wiki_result}

Provide a clear, concise answer:"""
                        
                        response = llm.predict(summary_prompt)
                        
                        st.success("✅ Search Complete!")
                        st.markdown("### 📄 Response:")
                        st.write(response)
                        
                        with st.expander("📚 View Full Wikipedia Content"):
                            st.write(wiki_result)
                            
                    except Exception as wiki_error:
                        st.error(f"❌ Wikipedia Search Failed: {str(wiki_error)}")
                        st.info("💡 Try:\n- Using more common terms\n- Checking spelling\n- Using DuckDuckGo for recent topics")
                    
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        else:
            st.warning("⚠️ Please enter a query")

# Tab 3: SQL Database
with tab3:
    st.subheader("🗄️ Ask using SQL Database")
    st.markdown("*Query your database using natural language*")
    
    # Database file upload or path
    db_path = st.text_input(
        "Database Path:",
        value="example_new.db",
        help="Enter the path to your SQLite database file"
    )
    
    # Show database info
    if os.path.exists(db_path):
        try:
            db = SQLDatabase.from_uri(f"sqlite:///{db_path}")
            st.success(f"✅ Connected to database: {db_path}")
            
            with st.expander("📊 View Database Schema"):
                st.code(db.get_table_info())
        except:
            st.warning(f"⚠️ Cannot read database: {db_path}")
    else:
        st.warning(f"⚠️ Database file not found: {db_path}")
    
    sql_query = st.text_input(
        "Your question:",
        key="sql_input",
        placeholder="e.g., How many laptops are in stock? or Show all products"
    )
    
    if st.button("Query", key="sql_search", type="primary"):
        if not groq_api_key:
            st.error("⚠️ Please configure your Groq API key in the sidebar")
        elif sql_query:
            if not os.path.exists(db_path):
                st.error(f"❌ Database file not found: {db_path}")
            else:
                with st.spinner("🔍 Querying database..."):
                    try:
                        llm = get_llm()
                        db = SQLDatabase.from_uri(f"sqlite:///{db_path}")
                        
                        toolkit = SQLDatabaseToolkit(db=db, llm=llm)
                        tools = toolkit.get_tools()
                        
                        agent = initialize_agent(
                            tools=tools,
                            llm=llm,
                            agent_type="zero-shot-react-description",
                            verbose=False,
                            max_iterations=5,
                            max_execution_time=30,
                            early_stopping_method="generate",
                            handle_parsing_errors=True
                        )
                        
                        try:
                            response = agent.run(sql_query)
                            st.success("✅ Query Complete!")
                            st.markdown("### 📄 Response:")
                            st.write(response)
                        except Exception as agent_error:
                            st.error(f"❌ Agent Error: {str(agent_error)}")
                            st.info("💡 Try simplifying your question or check if the table/column names exist in the database.")
                        
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
        else:
            st.warning("⚠️ Please enter a query")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "Built with Streamlit & LangChain | Powered by Groq"
    "</div>",
    unsafe_allow_html=True
)