import torch
from transformers import BertTokenizer, BertForSequenceClassification

# Define the pre-trained BERT model and tokenizer
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=2)

# Define the input text (replace with your preprocessed text)
input_text = "before the motor accident claims tribunal at pune macp no 3732022 smt pratima sagar deshpande and others  applicants vs bajaj allianz gic ltd and ors  opponent no 2 written statement  reply filed on behalf of opponent no 2 i e bajaj allianz g i c ltd preliminary facts  the address of the above opponent no 2 ie bajaj allianz general insurance co ltd for the purpose of service of all notices process etc is 1st floor commer zone samrat ashok path jail road yerwada pune 411006 all the material allegations made in the above petition are false and the petition is not maintainable either on facts or in law against this opponent hence the petition is liable to be dismissed in limini with costs against this opponent this opponent no 2 does not admit and denies all the allegations made in the petition and the applicants are put to strict proof of all the allegations except those which are specifically admitted hereunder this opponent no 2 admits that the interest of opponent no 1 ie balaji transport co part bhushan l wadhwani in vehicle tata lpg gas tanker bearing nl01n9124 was covered at the material time under the policy of insurance issued by this opponent subject to the terms conditions exceptions and limitations thereof and the confirmation"

# Tokenize the input text and convert it into a tensor
inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)

# Make the prediction
with torch.no_grad():
    outputs = model(**inputs)

# Get the predicted class and probabilities
predicted_class = torch.argmax(outputs.logits, dim=1).item()
probability = torch.softmax(outputs.logits, dim=1)[0][predicted_class].item()

# Map the class index to the corresponding label
labels = ["Not Important", "Important"]
predicted_label = labels[predicted_class]

# Print the result
print("Predicted Label:", predicted_label)
print("Confidence:", probability)
