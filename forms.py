def submit_form(customer_name, order_id, feedback_category, sentiment_score):
    import http.client
    import urllib.parse
    form_url = 'docs.google.com'
    form_path = '/forms/u/0/d/e/1FAIpQLSfBuzFvWRlVVm9bVrxB-R5ZovEoSAw-Qq_CR7KdX_2Ua_6-jA/formResponse'
    
    form_data = {
        'entry.665770853': customer_name,
        'entry.430623167': order_id,
        'entry.1815337387': feedback_category,
        'entry.831206065': sentiment_score
    }
    encoded_data = urllib.parse.urlencode(form_data)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': str(len(encoded_data))
    }
    connection = http.client.HTTPSConnection(form_url)
    try:
        connection.request('POST', form_path, body=encoded_data, headers=headers)
        response = connection.getresponse()
        
        if response.status == 200:
            return 'Form submitted successfully.'
        else:
            return f'Failed to submit form. Status code: {response.status}, Response: {response.read().decode()}'
    
    finally:
        connection.close()
