# ollama-summarizer
A simple command line input text summarizer made using the Qwen2 0.5B model.

## Highlights
1. A simple and fast text summarizer.
2. Summaries generated through Qwen2 0.5B model in Ollama accessed through the Ollama API.
3. Supports command line input of both texts and text files as parameters.
4. Suited only for Linux

NOTE: The text file __must__ be in the same directory as of the script. 

## Getting Started
1. `$ git clone https://github.com/ananyab1909/ollama-summariser.git` - clone this project to your computer
2. `$ cd ollama-summarizer` - go inside the project directory.
3. `pip install click` to install click library.
4. `pip install requests` to install the requests (only if not previously installed).    
5. `python3 summarise.py {text}` for texts.
6. `python3 summarise.py -t {textfile-name}` for text files.
7. Summarise and enjoy your journey.

NOTE: python3 is applicable for only Python 3.8 or above. Please enter according to your installed version

## Requirements
- Ollama must be installed on device.

## Method
- Ollama is supported on all operating systems.
- For __Linux__, execute `curl -fsSL https://ollama.com/install.sh | sh` in your terminal.
- After installing, execute `ollama --version` to check whether ollama is properly configured.
- For other platforms, please visit [Github](https://github.com/ollama/ollama/tree/main)

## API Configuration
- The API documentation is available at [Github](https://github.com/ollama/ollama/tree/main)
- The script is configured to send requests at [server](http://localhost:11434/api/chat)
- Please ensure that the server is properly running before executing the script.

## About Me
Hello, my name is Ananya Biswas. I am an Engineering Student at [Kalinga Institute of Industrial Technology](https://kiit.ac.in/). I enjoy making projects in my leisure time and this is one of them. Now that my this project is over, I am open-sourcing the project. Hope you like it!

Lastly, I would like to put it out there that I have worked on other projects that you may like. You can check them out at my [Github](https://github.com/ananyab1909/). Give it a whirl and let me know your thoughts.

## Socials
  - Portfolio : https://dub.sh/ananyabiswas
  - LinkedIn : https://linkedin.com/in/ananya-biswas-kiit/
  - Mastodon : https://mastodon.social/@captain_obvious/
  - Twitter : https://x.com/not_average_x/
  - Instagram : https://instagram.com/thegraffiti.mind/
  - Github : https://github.com/ananyab1909/

## Acknowledgements
- The Qwen-2 language model is developed by __Alibaba Cloud__ for text summarization capabilities.
- For more information, please visit [Ollama](https://ollama.com/)
