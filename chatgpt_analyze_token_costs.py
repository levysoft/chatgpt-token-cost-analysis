import json
import pandas as pd
from datetime import datetime
import tiktoken

# Prices per token
cost_per_million_input_tokens = 5.00
cost_per_million_output_tokens = 15.00

# Load the JSON file with exception handling
try:
    with open('chat_export.json', 'r') as file:
        chat_data = json.load(file)
    print("JSON file successfully loaded.")
except Exception as e:
    print(f"Error loading JSON file: {e}")
    raise

# Function to extract messages from nested data
def extract_messages(data):
    messages = []
    for conversation in data:
        for mapping_key in conversation['mapping']:
            message_data = conversation['mapping'][mapping_key]['message']
            if message_data and 'content' in message_data and 'parts' in message_data['content']:
                parts = message_data['content']['parts']
                # Ensure each part is a string
                content = " ".join([str(part) for part in parts])
                timestamp = message_data.get('create_time')
                if timestamp:
                    messages.append({
                        'timestamp': datetime.utcfromtimestamp(timestamp),
                        'content': content,
                        'role': message_data['author']['role']
                    })
    return messages

# Extract messages
messages = extract_messages(chat_data)
print(f"Number of messages extracted: {len(messages)}")

# Convert data to DataFrame
df = pd.DataFrame(messages)
print("Data converted to DataFrame.")

# Function to calculate tokens
def calculate_tokens(text):
    encoding = tiktoken.get_encoding("cl100k_base")  # Use a supported encoding
    tokens = encoding.encode(text)
    return len(tokens)

# Apply the function to each message
df['token_count'] = df['content'].apply(calculate_tokens)
print("Token calculation completed.")

# Separate costs for input and output
df['input_tokens'] = df.apply(lambda row: row['token_count'] if row['role'] == 'user' else 0, axis=1)
df['output_tokens'] = df.apply(lambda row: row['token_count'] if row['role'] == 'assistant' else 0, axis=1)
df['input_cost'] = df['input_tokens'] * (cost_per_million_input_tokens / 1_000_000)
df['output_cost'] = df['output_tokens'] * (cost_per_million_output_tokens / 1_000_000)

# Calculate total costs
df['cost'] = df['input_cost'] + df['output_cost']
print("Cost calculation completed.")

# Calculate total input and output tokens
total_input_tokens = df['input_tokens'].sum()
total_output_tokens = df['output_tokens'].sum()
print(f"Total Input Tokens: {total_input_tokens}")
print(f"Total Output Tokens: {total_output_tokens}")

# Group by month
df['month'] = df['timestamp'].dt.to_period('M')
cost_per_month = df.groupby('month')[['input_cost', 'output_cost', 'input_tokens', 'output_tokens', 'cost']].sum().reset_index()

# Sort results in descending order to show the most recent months first.
# Using ascending=False will sort from most recent to oldest.
# If you want to sort from oldest to most recent, set ascending=True
# or simply comment out the following line.
cost_per_month = cost_per_month.sort_values(by='month', ascending=False)

# Calculate total cost
total_cost = df['cost'].sum()
print(f"Total cost: ${total_cost:.2f}")

# Show costs per month
print("Costs per month:")
print(cost_per_month)

# Save results to a CSV file
cost_per_month.to_csv('costs_per_month.csv', index=False)
print("Results saved to costs_per_month.csv")
