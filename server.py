from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes, DecodingMethods
import json # these are the configuration data of your watsonx_api, project_id, and your model_id

# Load configuration from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Set up the API key and project ID for IBM Watson 
watsonx_API = config['watsonx_API']
project_id = config['project_id']
model_idx = config['model_id']
resource_location_url = config['resource_location_url']

generate_params = {
    GenParams.MAX_NEW_TOKENS: 250
}

model = Model(
    model_id = model_idx,  # Updated model ID # you can also specify like: ModelTypes.LLAMA_2_70B_CHAT
    params = generate_params,
    credentials={
        "apikey": watsonx_API,
        "url": resource_location_url
    },
    project_id= project_id
    )

q = "What is generative AI?"
generated_response = model.generate(prompt=q)
print(generated_response['results'][0]['generated_text'])