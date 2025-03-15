def personal_email(custname,orderid,fcat,newsenti,summary):
    template = f'''<p>Dear Team,</p>
    <p>The following feedback has been analyzed:</p>
    <ul>
    <li><b>Customer Name:</b> {custname}</li>
    <li><b>Order ID:</b> {orderid}</li>
    <li><b>Feedback Category:</b> {fcat}</li>
    <li><b>Sentiment Score:</b> {newsenti}</li>
    </ul>
    <p><b>Summary:</b> {summary}</p>
    <p>Regards,</p>
    <p>Feedback Automation System</p>
    '''
    return template
