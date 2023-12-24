##################################################################################
import streamlit as st
import functions


lists = functions.get_lists()
st.set_page_config(layout="wide")
def add_todo():
    list = st.session_state["new_todo"]+ "\n"
    lists.append(list)
    functions.write_lists(lists)


st.title("Welcome to My App")
st.subheader("New Web Application")
st.write("This app make your Tasks<b>Easier...</b>",
         unsafe_allow_html = True)
st.text_input(label="job", placeholder="Enter your task here",
              on_change=add_todo, key='new_todo')

for index, list in enumerate(lists):
    checkbox = st.checkbox(list, key=list)
    if checkbox:
        lists.pop(index)
        functions.write_lists(lists)
        del st.session_state[list]
        st.experimental_rerun()




###st.session_state