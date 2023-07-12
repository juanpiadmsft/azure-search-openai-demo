import tiktoken

MODELS_2_TOKEN_LIMITS = {
  "gpt-35-turbo" : 4000,
  "gpt-3.5-turbo" : 4000,
  "gpt-35-turbo-16k" : 16000,
  "gpt-3.5-turbo-16k" : 16000,
  "gpt-4" : 8100,
  "gpt-4-32k" : 32000
}

AOAI_2_OAI = {
  "gpt-35-turbo" : "gpt-3.5-turbo",
  "gpt-35-turbo-16k" : "gpt-3.5-turbo-16k"
}

def get_token_limit(modelid: str) -> int:
  if modelid not in MODELS_2_TOKEN_LIMITS:
    raise ValueError("Expected Model Gpt-35-turbo and above")
  return MODELS_2_TOKEN_LIMITS.get(modelid)

def num_tokens_from_messages(message: dict[str,str], model: str) -> int:
        """
        Calculate the number of tokens required to encode a message.
        Args:
            message (dict): The message to encode, represented as a dictionary.
            model (str): The name of the model to use for encoding.
        Returns:
            int: The total number of tokens required to encode the message.
        Example:
            message = {'role': 'user', 'content': 'Hello, how are you?'}
            model = 'gpt-3.5-turbo'
            num_tokens_from_messages(message, model)
            output: 11
        """
        encoding = tiktoken.encoding_for_model(get_oai_chatmodel_tiktok(model))
        num_tokens = 2  # For "role" and "content" keys
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
        return num_tokens

def get_oai_chatmodel_tiktok(aoaimodel: str) -> str:
    if aoaimodel == "" or aoaimodel is None:
        raise ValueError("Expected AOAI chatGPT model name")
    
    return AOAI_2_OAI.get(aoaimodel)