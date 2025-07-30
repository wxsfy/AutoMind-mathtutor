import streamlit as st
import openai

# Load the API key from Streamlit Cloud secrets
api_key = st.secrets["OPENAI_API_KEY"]
openai.api_key = api_key  # Set globally

# Streamlit UI
st.set_page_config(page_title="MathBot", page_icon="🧠")
st.title("🧠 MathBot")
st.write("Ask me any math question, and I’ll explain it step-by-step.")

# Input
question = st.text_input("Type your math question here:")

if question:
	with st.spinner("Thinking..."):
		try:
			response = openai.ChatCompletion.create(
				model="gpt-3.5-turbo",
				messages=[
					{"role": "system", "content": "You are a helpful math tutor. Always explain answers step-by-step in simple terms."},
					{"role": "user", "content": question}
				],
				max_tokens=300
			)

			answer = response.choices[0].message.content.strip()
			st.success("✅ MathBot says:")
			st.write(answer)

		except Exception as e:
			st.error(f"❌ Error: {e}")
