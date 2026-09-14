import streamlit as st
st.set_page_config(
  page_title="URUMURI AI",
  page_icon="💡"
)
st.title("💡 URUMURI AI")
st.write(mukaza nezakuri URUMURI AI_umufasha w'ikoranabunga mu kinyarwanda.")
st.subheader("Ni iki nakugirira?")
question=st.text_area(
  Andika ikibazo cyangwa icyo ushaka ko URUMURI AIigufashamo:"
)
if st.button("baza URUMURI AI"):
  if question:
    st.success("URUMURI AI yakiriye ikibazo cyawe!")
    st.write("Ikibazo cyawe ni:")
    st.write(question)
  else:
    st.warning("Bnza wandike ikibazo cyawe.")
