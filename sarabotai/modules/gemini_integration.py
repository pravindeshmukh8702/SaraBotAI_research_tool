from openai import OpenAI
from config import Config

class OpenAIIntegration:
    def __init__(self, api_key=None):
        # Use provided API key or fallback to config
        api_key = api_key or Config.OPENAI_API_KEY
        if api_key:
            self.client = OpenAI(api_key=api_key)
        else:
            self.client = None
            raise ValueError("API key is required. Please configure it via the UI or environment variable.")
    
    def generate_response(self, prompt, context=None, temperature=0.7):
        try:
            if context:
                messages = [
                    {"role": "system", "content": "You are a helpful assistant that provides detailed answers based on the given context."},
                    {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{prompt}\n\nAnswer:"}
                ]
            else:
                messages = [
                    {"role": "user", "content": prompt}
                ]
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=temperature,
                max_tokens=2048
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def generate_summary(self, text):
        prompt = f"Please provide a comprehensive summary of the following content, highlighting key points and themes:\n\n{text}"
        return self.generate_response(prompt, temperature=0.3)