import json

def get_context(model, question, field_check):

    
    output = model.generate_content(prompt_extract_entities.format(answer_example_1 = answer_example_1, answer_example_2 = answer_example_2, answer_example_3 = answer_example_3, answer_example_4 = answer_example_4, question = question),
                                            generation_config=generation_config, safety_settings={
                    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
            })
    
    response_text = output.text.replace("```", "").replace("json", "").replace('\n', '')
    query = json.loads(response_text)
    
    for key in query.keys():
        if key in field_check:
            field_check.remove(key)
    return query, field_check