def gemini(email: str):

    import google.generativeai as genai
    genai.configure(api_key='')
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content('summarize the following email, only give the output of the summary with all the main insights being considered'+email)
    return response.text
