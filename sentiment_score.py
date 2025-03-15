def extract_score(json_string):
    import json
    mapping = {'LABEL_0': 'Negative',
               'LABEL_1': 'Neutral',
               'LABEL_2': 'Positive'}
    try:
        data = json.loads(json_string)
        label = data[0][0]['label']
        score = data[0][0]['score']
        return f'{mapping[label]}: {round(score * 100, 1)}%'
    except (json.JSONDecodeError, KeyError, IndexError) as e:
        return f'Error processing input: {e}'
