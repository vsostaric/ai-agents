## Running Llama 2 Locally

To run the Llama 2 language model locally using Ollama:

### Start the Ollama container:
bash
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama


### Pull and run the model

Replace CONTAINER_ID with the actual value.

bash
docker exec CONTAINER_ID ollama pull llama3.2
docker exec CONTAINER_ID ollama run llama3.2


Full list of available models: https://github.com/ollama/ollama

### Generate a prompt response

bash
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt": "Tell me the name of the lost dialogue of Plato",
  "stream": false
}'


Response:
json
{"model":"llama3.2","created_at":"2025-04-16T19:24:09.139966442Z","response":"One famous example of a lost dialogue of Plato is \"Philebus\". However, it's not entirely lost. The majority of the work has survived.\n\nA more complete example of a \"lost\" or fragmentary Plato dialogue that was once well-known but now mostly survives in fragments is \"Axiochus\", which contains a significant discussion about the virtues and vices of Athenian democracy","done":true,"done_reason":"stop","context":[128006,9125,128007,271,38766,1303,33025,2696,25,6790,220,2366,18,271,128009,128006,882,128007,271,41551,757,279,836,315,279,5675,21976,315,69161,128009,128006,78191,128007,271,4054,11495,3187,315,264,5675,21976,315,69161,374,330,3438,458,10551,3343,4452,11,433,596,539,11622,5675,13,578,8857,315,279,990,706,26968,382,32,810,4686,3187,315,264,330,55437,1,477,12569,661,69161,21976,430,574,3131,1664,22015,719,1457,10213,83417,304,35603,374,330,38942,822,331,355,498,902,5727,264,5199,10430,922,279,66627,323,348,1238,315,59652,1122,20095],"total_duration":2961408515,"load_duration":54020914,"prompt_eval_count":35,"prompt_eval_duration":243659275,"eval_count":79,"eval_duration":2662282092}


