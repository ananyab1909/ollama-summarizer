import click
import os
import requests
import json

@click.command()
@click.option('-t', type=str, help='Input text file')
@click.argument('sentence', nargs=-1, required=False)

def main(t,sentence):
    content, source = read_input(t,sentence)
    if content and source:
        summary = generate_summary(content)
        if source == 'text' :
            click.echo(f".Summary of {source} pasted.")
            print(summary)
        else :
            click.echo(f".Summary of {source}.")
            print(summary)
    else :
        print("No input provided")

def read_input(t, sentence):
    inputSource = None
    inputContent = None
    if t:
        if os.path.exists(t):
            with open(t, 'r') as f:
                inputContent = f.read()
            inputSource = t
        else:
            click.echo(f"Error: File '{t}' not found")
            return None, None
    elif sentence:
        sentence = ' '.join(sentence)
        inputSource = 'text'
        inputContent = sentence
    else:
        click.echo("Error: No input provided")

    return inputContent,inputSource


def generate_summary(content):
    url = "http://localhost:11434/api/chat"
    data = {
            "model": "qwen2:0.5b", 
            "messages": [
                {
                "role": "user",
                "content": f"Summarize the following text : {content}"
                },
            ],
            "stream" : True  
    }

    response = requests.post(url, json=data , stream=True)
    if (response.status_code == 200):

        message_text = ''
        error_count = 0

        for line in response.iter_lines():
            try:
                obj = json.loads(line)
                if 'message' in obj and 'content' in obj['message']:
                    message_text += obj['message']['content'] + ' '
                else:
                    print("Skipping line: missing 'message' or 'content' key")
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                error_count += 1
            except KeyError as e:
                print(f"Missing key: {e}")
                error_count += 1
            except Exception as e:
                print(f"Unexpected error: {e}")
                error_count += 1

        if (error_count > 0) :
            print(f"Check. Too many errors ({error_count}) recorded.")
        
    return message_text

if __name__ == "__main__":
    main()

            




