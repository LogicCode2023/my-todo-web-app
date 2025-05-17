import streamlit as st
import funtions


todos = funtions.get_todos()


def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    if todo_local not in todos:
        todos.append(todo_local)
        funtions.write_todos(todos)

st.title("My To-do App")
st.subheader("This is my Todo App.")
st.write("This app in to increase you productivity")


for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{index}-{todo}")
    if checkbox:
        todos.pop(index)
        funtions.write_todos(todos)
        del st.session_state[f"{index}-{todo}"]
        st.rerun()

st.text_input(label="",placeholder="Enter a todo: ",
              on_change=add_todo, key='new_todo')











