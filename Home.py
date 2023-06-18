import streamlit as st
from streamlit_chat import message
from st_pages import Page, show_pages, add_page_title, Section
import io
st.title("Create Your Digital Life !")



# show_pages(
#     [
#         Page("Home.py", "Home"), 
#         Section(name="Digital Lifes"),
#         Page("pages/Trump.py",'Trump')
#     ]
# )



header1 = "First, you should upload your avatar"
st.header(header1)
left_column, right_column = st.columns(2)
uploaded_file = right_column.file_uploader('Upload your avatar', type=['png', 'jpg', 'jpeg'])
if not uploaded_file:
    left_column.image("images/musk.jpeg", caption="This is an example: Elon Musk")
else: 
    file_content = uploaded_file.getvalue()
    # 将字节流转化为文件对象
    file_obj = io.BytesIO(file_content)
    # 将文保存到本地
    with open(f"images/{uploaded_file.name}", 'wb') as f:
        f.write(file_content)
    left_column.image(f"images/{uploaded_file.name}", caption="Your avatar")

if uploaded_file: st.success("Uploaded successfully!")




# message("My message") 
# message("Hello bot!", is_user=True)  # align's the message to the rightstrr

# name = st.text_input("Start Chat!")

# hello = st.button("Say hello")

# from streamlit_option_menu import option_menu

# # 1. as sidebar menu
# with st.sidebar:
#     selected = option_menu("Main Menu", ["Home", 'Settings'], 
#         icons=['house', 'gear'], menu_icon="cast", default_index=1)
#     selected

# # 2. horizontal menu
# selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
#     icons=['house', 'cloud-upload', "list-task", 'gear'], 
#     menu_icon="cast", default_index=0, orientation="horizontal")
# selected2

# # 3. CSS style definitions
# selected3 = option_menu(None, ["Home", "Upload",  "Tasks", 'Settings'], 
#     icons=['house', 'cloud-upload', "list-task", 'gear'], 
#     menu_icon="cast", default_index=0, orientation="horizontal",
#     styles={
#         "container": {"padding": "0!important", "background-color": "#fafafa"},
#         "icon": {"color": "orange", "font-size": "25px"}, 
#         "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
#         "nav-link-selected": {"background-color": "green"},
#     }
# )

# # 4. Manual Item Selection
# if st.session_state.get('switch_button', False):
#     st.session_state['menu_option'] = (st.session_state.get('menu_option',0) + 1) % 4
#     manual_select = st.session_state['menu_option']
# else:
#     manual_select = None
    
# selected4 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
#     icons=['house', 'cloud-upload', "list-task", 'gear'], 
#     orientation="horizontal", manual_select=manual_select, key='menu_4')
# st.button(f"Move to Next {st.session_state.get('menu_option',1)}", key='switch_button')
# selected4

# # 5. Add on_change callback
# def on_change(key):
#     selection = st.session_state[key]
#     st.write(f"Selection changed to {selection}")
    
# selected5 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'],
#                         icons=['house', 'cloud-upload', "list-task", 'gear'],
#                         on_change=on_change, key='menu_5', orientation="horizontal")
# selected5