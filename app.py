import streamlit as st
import pandas as pd
from suggest import suggest

st.set_page_config(page_title="SHL Assessment Recommender", layout="wide")
st.title("🧠 SHL Assessment Recommender")
st.markdown("Enter a job description or natural language query to get SHL test recommendations.")

query = st.text_area("Paste your query or job description here:", height=200)

if st.button("Recommend Assessments"):
    if not query.strip():
        st.warning("Please enter a valid query.")
    else:
        with st.spinner("Analyzing and recommending assessments..."):
            results = suggest(query)
            if results:
                st.success(f"Found {len(results)} relevant assessments.")
                
                df_display = pd.DataFrame(results)
                df_display["Assessment Name"] = df_display.apply(
                    lambda row: f"[{row['Assessment Name']}]({row['URL']})", axis=1
                )
                df_display = df_display.drop(columns=["URL", "score"])  # Hide raw score if preferred
                st.markdown("### 📋 Recommended Assessments")
                st.write(df_display.to_markdown(index=False), unsafe_allow_html=True)

            else:
                st.warning("No relevant assessments found.")


st.markdown(
    """
    <hr style="margin-top: 100px;"/>
    <div style='text-align: center; font-size: 14px;'>
        Developed by <a href="https://www.github.com/yashmangal112" target="_blank">Yash Mangal</a> 🚀
    </div>
    """,
    unsafe_allow_html=True
)
