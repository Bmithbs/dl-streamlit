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
avater_file = right_column.file_uploader('Upload your avatar', type=['png', 'jpg', 'jpeg'])
if not avater_file:
    left_column.image("images/musk.jpeg", caption="This is an example: Elon Musk")
else: 
    file_content = avater_file.getvalue()
    # 将字节流转化为文件对象
    file_obj = io.BytesIO(file_content)
    # 将文保存到本地
    with open(f"images/{avater_file.name}", 'wb') as f:
        f.write(file_content)
    left_column.image(f"images/{avater_file.name}", caption="Your avatar")

if avater_file: st.success("Uploaded successfully!")

st.divider()

header2 = "Second, Upload your memory materials"
st.header(header2)
st.write('Upload your memory materials, such as chat history, diaries, twitters, blogs etc. Now we only support txt files.')

memory_file = st.file_uploader('Upload your memory materials', type=['txt'], accept_multiple_files=True)

if memory_file: 
    st.success("Uploaded successfully!")

st.divider()
header3 = 'Third, digest your memory materials'
st.header(header3)

if st.button('Start to digist'):
    if memory_file:
        # digist 函数
        st.success("Digisted successfully!")

    else :
        st.warning("Please upload your memory materials first!")
st.divider()

with st.form("my_form"):
   st.write("Inside the form")
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form") 


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