import streamlit as st  
st.title("Hello everyone")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is a text")
st.markdown("# This is heading markdown") 
st.markdown("## This is a subheadling markdown") 
st.markdown("### This is a subsubheading markdown") 
st.markdown("""<ol> 
<li> THis is a the first element </li> 
<li> This is the second </li> 
<li> This is a the third </li> """,unsafe_allow_html=True)
categories = ["cat1","cat2","cat3","cat4"]
sub_categories = ["sub_cat1","sub_cat2","sub_cat3","sub_cat4"]
checkbox = st.checkbox("Show/hide")
if checkbox : 
    st.info("The checkbox is selected")
category = st.radio("Select category: ", categories)
st.text(f"the selected category is {category} ")

sub_category = st.selectbox("sub Categories",sub_categories)
st.text(f"the selected subcategory is : {sub_category}")
product_name = st.text_input("Select the product name","")
if product_name : 
    st.text(f"The product name is {product_name}")
number_slider = st.slider("Select the level",1,1000)
st.number_input("Select the number")
if st.button("Submit") : 
    if(product_name) : 
        st.success("Your form has been submitted!")
    else : 
        st.warning("The product name has to be set")

categories = {
    "Fruits": ["Apple", "Banana", "Orange", "Grapes"],
    "Vegetables": ["Carrot", "Broccoli", "Spinach", "Pepper"],
    "Dairy": ["Milk", "Cheese", "Yogurt"]
}

# Create the first dropdown for category
selected_category = st.selectbox("Select a category:", list(categories.keys()))

# Based on the selected category, create the second dropdown for subcategory
if selected_category:
    subcategories = categories[selected_category]
    selected_subcategory = st.selectbox("Select a subcategory:", subcategories)

# Display the selected category and subcategory
st.write(f"You selected category: {selected_category}")
st.write(f"You selected subcategory: {selected_subcategory}")
