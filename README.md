# simple QA chat with IBM Watsonx.ai

# requirments
- python
- IBM Cloud Account ( project-id & API- key ) 

# Steps
- clone the project : 'git clone '
- create an environment variable : 'python -m venv your_env_name' ( windows ) or 'python3 -m venv your_env_name'
- Activate your environment variable : 'your_env_name/Scripts/activate' (windows) or 'source your_env_name/bin/activate'(linux )
- install requirement variable : 'pip install ibm-watson-machine-learning'
- sign up and sign in to ibm-cloud : 'https://cloud.ibm.com/'
- on the top navbar click dropdown button go to :  Manage > Access (IAM) > API keys
- create your api key.
- In the search bar go to 'watsonx' service then select 'get started' watsonx.AI
- select a region login , click 'here'
- to create a project go to project> view all project > New project
- go to the project you have just created then select manage tab
- in general section you will find your project-id.
- finally go to 'services & integrations' > associate service > New service > select watson machine learning type
- add the created service
- go to the code and create config.json file
- create a json file for watsonx_api, project_id, model_id, resource_location_url.
- The model_id are models that are available based on your selected service for free service you can choose "meta-llama/llama-2-13b-chat" model.
-  for resource_location_url on the top of navbar copy the regon code, update the value region_code, https://your_region_code.ibm.com.
-  run the project : 'python server.py '(windows ) or 'python3 server.py'
-  you can test the project by updating your question

# Screenshot
