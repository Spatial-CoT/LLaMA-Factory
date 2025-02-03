import json
import random

# Read the original JSON file
with open('data/all_qa_sharegpt_0203.json', 'r') as f:
    data = json.load(f)

# Randomly sample 25% of entries
sampled_data = random.sample(data, k=int(len(data) * 0.25))

# Write sampled data to new JSON file
output_file = 'data/all_qa_sharegpt_0203_25percent.json'
with open(output_file, 'w') as f:
    json.dump(sampled_data, f, indent=2)

print(f"Original dataset size: {len(data)}")
print(f"Sampled dataset size: {len(sampled_data)}")
print(f"Saved to {output_file}")
