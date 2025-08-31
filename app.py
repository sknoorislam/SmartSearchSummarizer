import streamlit as st
from search_engine import Engine
from llm_engine import LLMEngine

st.title("AI Search Engine By Noor")
st.write("This is a simple AI-powered search engine that uses a language model to generate responses based on user queries.")



# Input box
query = st.text_input("Enter your question:", placeholder="e.g., What is your mind?", icon="🔍")
all_results_dump = []


st.set_page_config(page_title="AI Search Engine By Noor", layout="wide")

# -- layout --
left_column, right_column = st.columns([2,1])


with left_column:
    if query:
        st.subheader("🔽 Search Results")
        engine = Engine(query)
        answer = engine.generate_response()
        print(answer)

        try:
            if answer['code'] == 200:
                search_reasults = answer['data']['webPages']['value']

                for res in search_reasults:
                    st.write(res['name'])
                    st.write(res['snippet'])
                    st.caption(res['url'])
                    st.markdown("")
                    all_results_dump.append(res['summary'])


        except KeyError:
            st.write("No results found.")

        

with right_column:
    if query:
        st.subheader("📖 Overview")
        st.write(f"### Summary for: {query}")
        llm_engine = LLMEngine()
        # Create prompt
        prompt = "Summarize the following chunks into a concise overview:\n\n" + "\n".join(all_results_dump)
        overview = llm_engine.generate_overview_by_chunk(prompt)
        st.write(overview)
    
# st.write("Add dump data")
# st.write(all_results_dump)