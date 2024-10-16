import streamlit as st
from PIL import Image
st.title("Hello Gomycode ")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("Hello Gomycode")
st.markdown("### This is a markdown")
st.markdown("## This is a bigger markdown")
st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")
img = Image.open("FELV-cat.jpg")
st.image(img, width=200)
if st.checkbox("Show/Hide"):
    st.text("Showing the widget")
status = st.radio("Select Gender: ", ('Male', 'Female'))


if (status == 'Male'):

	st.success("Male")

else:

	st.success("Female")
	
# first argument takes the titleof the selectionbox

# second argument takes options :



hobby = st.selectbox("Hobbies: ",['Dancing', 'Reading', 'Sports'])
st.write("Your hobby is: ", hobby)
hobbies = st.multiselect("Hobbies: ",

						['Dancing', 'Reading', 'Sports'])

st.write("You selected", len(hobbies), 'hobbies')

if(st.button("About")):

	st.text("Welcome To Gomycode!!!")
name = st.text_input("Enter Your name","Your name")
if(st.button('Submit')):

	result = name.title()

	st.success(result)
level = st.slider("Select the level", 1, 5)
st.text('Selected: {}'.format(level))
