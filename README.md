# RevAI - Let AI Review it First!

An AI code reviewing action that leaves its thoughts whenever someone opens a pull request on your repository. Let AI approve it, then just merge it!

<img src="media/banner.svg">

## Setup
You have to create a MindsDB account [here](https://cloud.mindsdb.com/login) and log into it. Then train a GPT model based on your desired prompt and share the credentials with RevAI so that it'll be able to comment on changes.

Once you've created the account, follow the steps here.

### Get an `API_KEY` from OpenAI
Create an account on [here](https://openai.com/) and generate a chatGPT access token. Copy that into your clipboard.

### Train the model
Navigate to your [dashboard](https://cloud.mindsdb.com/home) and create a new instance. Execute the following snippet in your instance editor.

> Replace your OpenAI token with `<YOUR-TOKEN>` and select one of the following prompt statements as `<PROMPT>`.

```sql
CREATE MODEL mindsdb.gpt_model
PREDICT response
USING
engine = 'openai',
api_key = '<YOUR-TOKEN>',
model_name = 'gpt-3.5-turbo', -- you can also use 'text-davinci-003' or 'gpt-3.5-turbo'
prompt_template = '<PROMPT>'; 
```

#### Prompt #1
```
Some text..
```

#### Prompt #2
```
Some text..
```

## Usage
```yml
example usage..
```

## License
Check out [MIT License](LICENSE) terms.
