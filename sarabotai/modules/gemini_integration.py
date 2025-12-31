import google.generativeai as genai
from config import Config

class GeminiIntegration:
    def __init__(self, api_key=None):
        # Use provided API key or fallback to config
        api_key = api_key or Config.GEMINI_API_KEY
        if api_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-1.5-pro-latest')
        else:
            self.model = None
            raise ValueError("API key is required. Please configure it via the UI or environment variable.")
    
    def generate_response(self, prompt, context=None, temperature=0.7):
        try:
            if context:
                prompt = f"Context:\n{context}\n\nQuestion:\n{prompt}\n\nAnswer:"
            
            response = self.model.generate_content(
                prompt,
                generation_config={
                    "temperature": temperature,
                    "top_p": 0.95,
                    "top_k": 40,
                    "max_output_tokens": 2048,
                }
            )
            return response.text
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def generate_summary(self, text):
        prompt = f"Please provide a comprehensive summary of the following content, highlighting key points and themes:\n\n{text}"
        return self.generate_response(prompt, temperature=0.3)