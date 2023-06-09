import streamlit as st
from PIL import Image as i

st.write("HI I am using Streamlit!!!!")

st.title("This is a title.....")
st.subheader("This is a subheader")
st.success("Success")
 
# success
st.info("Information")
 
# success
st.warning("Warning")
 
# success
st.error("Error")


img = i.open("g.jpg")
 
# display image using streamlit
# width is used to set the width of an image

st.image(img,width=500)

a=st.checkbox("java")
b=st.checkbox("C")
if st.checkbox("Python"):
    st.write("CONGRATS....")

v=st.radio("Select who U are??? ",('Male','Female'))
st.write("u have selected "+v)

hobby = st.selectbox("Hobbies: ",['Dancing', 'Reading', 'Sports'])
 
# print the selected hobby
st.write("Your hobby is: ", hobby)


# multi select box

# first argument takes the box title
# second argument takes the options to show
hobbies = st.multiselect("Hobbies: ",
						['Dancing', 'Reading', 'Sports'])

# write the selected options
st.write("You selected", len(hobbies), 'hobbies')



response=st.button("I am Neha")
if response:
    st.write("U are neha")

name = st.text_input("Enter Your name", "Type Here ...")
 
st.write("U are "+name)


# first argument takes the title of the slider
# second argument takes the starting of the slider
# last argument takes the end number
level = st.slider("Select the level", 1, 100)
 
# print the level
# format() is used to print value
# of a variable at a specific position
st.text('Selected: {}'.format(level))








