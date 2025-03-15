import streamlit as st

st.title("Streamlit with Nginx Reverse Proxy")
st.write("This app is being served through Nginx at a custom URL path!")

# Add some example content
st.header("Sample Interactive Elements")
slider_value = st.slider("Select a value", 0, 100, 50)
st.write(f"You selected: {slider_value}")

if st.button("Click me!"):
    st.success("Button clicked!")
