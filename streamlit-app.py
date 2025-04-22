import streamlit as st

# Sidebar input
st.sidebar.title("🎈 Customize")
name = st.sidebar.text_input("Enter your name", "Stranger")

# Main content
st.title("👋 Hi there!")
st.write(f"Nice to meet you, **{name}**!")

# Button with conditional message
if st.button("Click me!"):
    st.success("Boom! You clicked it 🎉")
    st.balloons()
else:
    st.info("Click the button when you're ready!")

# Just for fun
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
