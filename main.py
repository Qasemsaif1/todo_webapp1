import streamlit as st
import function as fc
import os

# Modules
categories = list(cat.strip() for cat in fc.get_todos("cat.txt"))
completed_dir = 'completed_tasks.txt'
fc.opendir(categories, completed_dir)


def add_todo():
    new_todo = st.session_state["new_todo"].title()+ "\n"
    if len(new_todo.strip()) > 0:
        todos_list.append(new_todo)
        fc.store_todos(todos_list, list_dir)
        st.session_state["new_todo"] =""


# Interface

st.title("To Do APP")
st.markdown("---")
st.markdown("""<style> .css-cio0dv.egzxvld1
{visibility: hidden;} </style> """, unsafe_allow_html=True)

## Side bar
### Add/Del categories
new_cat = st.sidebar.text_input("Add/Delete Category", placeholder="Write Here...", key="add_del_category").strip().title()
save_cat_button = st.sidebar.button("Save", key="save_cat")
del_cat_button = st.sidebar.button("Delete", key="del_cat")


if del_cat_button:
    if len(new_cat.strip()) > 1:
        if new_cat.strip() != categories[0] and new_cat.strip() in categories:
            categories.remove(new_cat)
            os.remove(f"{new_cat}.txt")
            categories = (cat.title() + "\n" for cat in categories)
            fc.store_todos(categories, "cat.txt")

            del st.session_state['add_del_category']
            st.session_state["add_del_category"] = ""
            st.experimental_rerun()

        if not new_cat.strip()  in categories:
            del st.session_state['add_del_category']
            st.session_state["add_del_category"] = ""
            st.experimental_rerun()

    else:
        del st.session_state['add_del_category']
        st.session_state["add_del_category"] = ""
        st.experimental_rerun()

if save_cat_button:
    if len(new_cat.strip()) > 1:
        if not os.path.exists(f'{new_cat}.txt'):
            categories.append(new_cat)
            categories = (cat.title() + "\n" for cat in categories)
            fc.store_todos(categories, "cat.txt")

            del st.session_state['add_del_category']
            st.session_state["add_del_category"] = ""
            st.experimental_rerun()
    else:
        del st.session_state['add_del_category']
        st.session_state["add_del_category"] = ""
        st.experimental_rerun()

##  View/Choose categories
st.sidebar.selectbox(label="Categories", options=(list(categories)), key="chosen_category")

list_dir = f'{st.session_state["chosen_category"]}.txt'
todos_list = fc.get_todos(list_dir)
completed = fc.get_todos(completed_dir)


### Show Completed Tasks
completed_bar = st.sidebar.selectbox("Completed Tasks", list(completed), key="complete")
delete_option = st.sidebar.button("Delete", key='delete')
save_option = st.sidebar.button("Save", key="save")


if delete_option:
    completed.remove(st.session_state['complete'])
    fc.store_todos(completed, completed_dir)
    del st.session_state['complete']
    st.experimental_rerun()

if save_option:
    todos_list.append(st.session_state['complete'])
    fc.store_todos(todos_list, list_dir)

    completed.remove(st.session_state['complete'])
    fc.store_todos(completed, completed_dir)
    del st.session_state['complete']
    st.experimental_rerun()


## Check boxes and input box
for index, todo in enumerate(todos_list):
    check_box = st.checkbox(todo, key=f'{todo}+{index}')
    if check_box:
        completed.append(todo)
        fc.store_todos(completed, 'Completed_tasks.txt')

        todos_list.pop(index) # this line will delete the to do checked in the list above.
        fc.store_todos(todos_list, list_dir)
        del st.session_state[f'{todo}+{index}'] # This will delete the to do form the session state dictionary
        st.experimental_rerun()



st.text_input(label="", placeholder="Write a task here....",
              key="new_todo", on_change=add_todo)

