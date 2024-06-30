# ChatGPT Token Cost Analysis

This repository contains a Python script for analyzing the costs associated with tokens generated from ChatGPT export chats. The script extracts messages from a JSON file, calculates the number of tokens used, and determines the costs for input and output tokens. Additionally, it groups the costs by month and saves the results in a CSV file.

## Requirements

- Python 3.x
- Python modules: `json`, `pandas`, `datetime`, `tiktoken`

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/levysoft/chatgpt-token-cost-analysis.git
    ```
2. Install the required packages:
    ```sh
    pip install pandas tiktoken
    ```

## Usage

1. Place your `conversations.json` file in the main directory of the project.
2. Run the script:
    ```sh
    python chatgpt_analyze_token_costs.py
    ```

## Script Description

### Global Variables

- `cost_per_million_input_tokens`: Cost per million input tokens (5.00 USD)
- `cost_per_million_output_tokens`: Cost per million output tokens (15.00 USD)

### JSON File Loading

The script loads the `conversations.json` file and handles any exceptions during loading.

### Message Extraction

The `extract_messages(data)` function extracts messages from the nested JSON data and converts them into a pandas DataFrame.

### Token Calculation

The `calculate_tokens(text)` function uses the `cl100k_base` encoding to calculate the number of tokens in each message.

### Cost Calculation

The script separates input and output tokens and calculates the associated costs.

The total chat costs are calculated using OpenAI API pricing for GPT-4 (https://openai.com/api/pricing/).

The costs are calculated separately for input tokens (user) and output tokens (assistant), using specific pricing for GPT-4.

### Output

The results are grouped by month and saved to a CSV file `costs_per_month.csv`.

## Example Output

```bash
JSON file successfully loaded.
Number of messages extracted: 13694
Data converted to DataFrame.
Token calculation completed.
Cost calculation completed.
Total Input Tokens: 823211
Total Output Tokens: 2281124
Total cost: $38.33
Costs per month:
      month  input_cost  output_cost  input_tokens  output_tokens      cost
17  2024-06    0.251990     2.453400         50398         163560  2.705390
16  2024-05    0.341110     3.739950         68222         249330  4.081060
15  2024-04    0.375340     2.554425         75068         170295  2.929765
14  2024-03    0.452200     3.057330         90440         203822  3.509530
13  2024-02    0.410050     4.956330         82010         330422  5.366380
12  2024-01    0.397070     2.669400         79414         177960  3.066470
11  2023-12    0.156830     1.096485         31366          73099  1.253315
10  2023-11    0.236500     2.278845         47300         151923  2.515345
9   2023-10    0.478100     2.457090         95620         163806  2.935190
8   2023-09    0.156665     1.502850         31333         100190  1.659515
7   2023-08    0.008925     0.276330          1785          18422  0.285255
6   2023-07    0.299655     0.931125         59931          62075  1.230780
5   2023-06    0.308550     2.195280         61710         146352  2.503830
4   2023-05    0.031720     0.388905          6344          25927  0.420625
3   2023-03    0.019850     0.423750          3970          28250  0.443600
2   2023-02    0.041680     0.254055          8336          16937  0.295735
1   2023-01    0.094950     1.419300         18990          94620  1.514250
0   2022-12    0.054870     1.562010         10974         104134  1.616880
```
## Web-Based Token Cost Analyzer

In addition to the Python script, I've created a single-page HTML + JavaScript application that allows anyone to analyze token costs locally. This HTML page does not use the `tiktoken` library, which is unavailable in JavaScript, but rather utilizes the `gpt-tokenizer` library.

### Why the HTML Page?

- **Accessibility**: This HTML page can be downloaded and run locally by anyone without needing to set up a Python environment.
- **Comprehensive Model Support**: Unlike the Python script, the HTML page includes support for multiple models with varying token costs, allowing for more flexible analysis.
- **Local Privacy**: The page ensures the privacy of your sensitive data because it works entirely locally. Your JSON file containing private chats is never uploaded to a remote server.

### Using the HTML Page

1. **Download the Page**: Click the download link on the page to save it for offline use.
2. **Select the Model**: Choose the appropriate model from the dropdown menu.
3. **Upload Your JSON File**: Select your `conversations.json` file to analyze.
4. **View Results**: The analysis results, including total and monthly costs, will be displayed directly on the page.

This web-based tool provides a more user-friendly and comprehensive way to analyze token costs for various models and use cases.

### Enhancing Privacy and Offline Functionality

To ensure the privacy of your data and provide functionality even when offline, the HTML page includes a mechanism to load the `GPTTokenizer_cl100k_base` encoder from a local source if the remote JavaScript file is not accessible. By default, the page attempts to load the tokenizer from the remote URL `https://unpkg.com/gpt-tokenizer`. If this remote file is not available, the script will then try to load a local version of the tokenizer (`cl100k_base.js`).

Here's a brief overview of how it works:

- The `checkGPTTokenizer` function first attempts to load the `GPTTokenizer_cl100k_base` encoder from the remote source.
- If the remote file is not accessible, it attempts to load the local `cl100k_base.js` file.
- If neither the remote nor local files are available, the script falls back to a rough approximation based on the number of words in the text. This fallback method, while not as precise, provides a useful estimate of token usage.

To use the local version of the tokenizer, make sure to download `cl100k_base.js` and place it in the same directory as the HTML file. This approach ensures that your data remains private and the functionality is available even without an internet connection.

This enhancement makes the tool more privacy-compliant and ensures that users can analyze their chat data under any network conditions.

### Screenshot

Here is a screenshot of the web page:

![Web Page Screenshot](screenshot1.jpg)

Make sure to download the page and use it offline for maximum privacy and security.

![Web Page Screenshot](screenshot2.jpg)

### How to Export Your ChatGPT History and Data

> To analyze your ChatGPT chat history with our tools, you first need to export your data from ChatGPT. Here’s how you can do it:
>
> 1. Sign in to ChatGPT.
> 2. In the top right corner of the page, click on your profile icon.
> 3. Click on **Settings**.
> 4. Go to the **Data Controls** menu.
> 5. Under **Export Data**, click **Export**.
> 6. In the confirmation screen, click **Confirm export**.
>
> You should receive an email with your data. Note that the link in the email expires after 24 hours. Click on **Download data export** to download a `.zip` file. This file includes your chat history in `chat.html` as well as other data associated with your account.
>
> In the `.zip` file, you will find both `chat.html` and `conversations.json`. The `conversations.json` file is the one required for processing with our tools.
> 
> This functionality is available on both Free and Plus plans. It is not available to users who are logged out.
>
> For more details you can visit the [How do I export my ChatGPT history and data?](https://help.openai.com/en/articles/7260999-how-do-i-export-my-chatgpt-history-and-data).
>
> If you follow these steps, you will have your chat data ready for analysis using our Python script or HTML page.


## Author

Antonio Troise

## License

This project is released under the MIT License. See the LICENSE file for more details.
