from supadata import Supadata, SupadataError
import os.path
from dotenv import load_dotenv


def auto(filename):
    pass

def manual(filename):
    links = None

    while links is None:
        try:
            links = int(input("Input number of links: "))
        except ValueError:
            print("Make sure to input a number")


    user_url = []
    for i in range(int(links)):
        temp = input("Paste the Instagram URL: ")
        user_url.append(temp)

    
    for j in user_url:
        print(j)
        temT = get_transcript(j)
        append_copy = open(filename, "a+")
        append_copy.seek(0)
        append_copy.write("\n"+j)
        append_copy.write("\n")
        append_copy.write(temT)
        append_copy.close()




def get_transcript(user_url):
    transcript = supadata.transcript(
        url=user_url,
        lang="en",  # Optional: preferred language
        text=True,  # Optional: return plain text instead of timestamped chunks
        mode="auto"  # Optional: "native", "auto", or "generate"
    )

    if hasattr(transcript, 'content'):
        return transcript.content
    else:
        # For async processing (large files)
        print(f"Processing started with job ID: {transcript.job_id}")
        # Poll for results using existing batch.get_batch_results method
    return "Error in transcript translation"


load_dotenv()

api_secret = os.getenv("API_KEY")
supadata = Supadata(api_key=api_secret)

flow = None
while flow != "input" and flow != "txt":
    flow = input("Enter the way you want to use this tool (txt or input): ")
    if (flow != "input" and flow != "txt"):
        print("Enter valid input (txt or input)")

filename = input("Input filename: ")
current_directory = os.getcwd()
while (os.path.exists(filename) == False):
    print("Try again, not valid file name.")
    filename = input("Input filename: ")

append_copy = open(filename, "a+")
append_copy.seek(0)
append_copy.write("\n")
append_copy.close()



if flow == "input":
    manual(filename)
elif flow == "txt":
    auto(filename)