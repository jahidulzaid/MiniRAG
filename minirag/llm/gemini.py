import google.generativeai as genai
import os
import asyncio

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

async def gemini_complete(prompt, system_prompt=None, history_messages=[], **kwargs):
    model = genai.GenerativeModel("gemini-pro")

    loop = asyncio.get_running_loop()

    def _run():
        chat = model.start_chat()
        return chat.send_message(prompt).text

    return await loop.run_in_executor(None, _run)

#ls