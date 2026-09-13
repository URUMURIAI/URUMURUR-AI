import streamlit as st
st.set_page_config(
  page_icon="💡"
)
st.title("💡  URUMURI AI")
st.write("murakaza neza kuri URUMURI AI.")
 question=st.text_inpt("andika ikibazo cyawe:")
if question:
  st.write("URUMURI AI irimo gutegura igisubizo.
  st.write(f"Ikibazo wakibajije ni: {question}")
