import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
# Session State is a way to share variables
# between reruns, for each user session. In addition
# to the ability to store and persist state,
# Streamlit also exposes the ability to manipulate
# state using Callbacks.
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity.")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo , key="new_todo")
