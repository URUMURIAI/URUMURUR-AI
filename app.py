import streamlit as st

st.set_page_config(
    page_title="URUMURI AI",
    page_icon="💡"
)

st.title("💡 URUMURI AI")
st.write("Murakaza neza kuri URUMURI AI, umufasha wawe w'ikoranabuhanga.")

st.subheader("Ni iki nakugirira?")

question = st.text_area(
    "Andika ikibazo cyangwa icyo ushaka ko URUMURI AI igufasha:"
)

if st.button("Baza URUMURI AI"):
    if question.strip():
        st.success("URUMURI AI yakiriye ikibazo cyawe!")
        st.write("Ikibazo cyawe ni:")
        st.write(question)
    else:
        st.warning("Banza wandike ikibazo cyawe.")
