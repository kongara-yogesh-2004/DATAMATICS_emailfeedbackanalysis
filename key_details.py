def geminis(email: str):

    import google.generativeai as genai
    import ast
    genai.configure(api_key='')
    model = genai.GenerativeModel('gemini-1.5-flash')

    fields= ['<Customer-Name>', '<Order-ID>', '<Feedback-Category>']
    response = model.generate_content(f'Extract the following details from customer email: Customer Name: Identify the name from the salutation, signature, or email body. Order ID: Extract if mentioned, otherwise mark as N/A. Feedback Category: Classify as Product, Service, or Delivery based on the content. Return the output in this format only: {fields}  email: {email}')
    formatted_output = f'{response.text}\n'
    return ast.literal_eval(formatted_output)
