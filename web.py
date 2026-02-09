import streamlit as st
import function

todos = function.get_todos()

def add_new_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    function.write_todos(todos)


st.title("my :rainbow[Todos] items")

if st.button("Send balloons!"):
    st.balloons()




st.sidebar.header("Todos")
x=st.slider("select a value")
st.write(x, "squared is", x * x)

for index, todo in enumerate(todos):
    checkbox=st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.rerun()



st.text_input(label="Happy tp enter",placeholder="Add to Todos ....",
              on_change=add_new_todo, key="new_todo")

