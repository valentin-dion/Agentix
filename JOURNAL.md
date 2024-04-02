* [ ] create Entities
* [ ] Turn Conv and Message into Entities
* [ ] Use Conv and Message as FSL
* [ ] create Endpoints
* [ ] create shell engine for front stuff
* [ ] create a front app
* [ ] python3 run serve
* [ ] Le front des endpoints on va juste itérer sur les Endpoints, leur URL est une propriété fichier
* [ ] store flags in conv file (optionnal)



_______________________________

# Entities
Entity.all
Entity['Conversation'].doc|mock

on veut transformer un prompt de base pour un debugger en des spe front/endpoint


```
system:You're Specificator, a smart AGI that rewrites user prompts to include specs for components and Endpoints.
Components are Nuxt

You always reason out loud, step².
You self reflect 2 times with ```1,```2 and ```3
Your role is to spec Components and Endpoints, telling them exactly what the should be doing

__-__

system:

# Context
## Entities
`Conversation`: eg:[{role:"flags","should_infer:true,locked:false"},{role:"system",content:"you're an assistant"},{role:"user",content:"can you help"},{role:"assistant",content:"sure"}

# Prompt
I want a debbuger for conversations, whenever in code I do `conv = Func['debug_conv'](conv)` it should save the conversation in the file prompts/_debug.conv with the flag "locked" to true. Then gather the conv with from_file and while the flag is not to false, it should sleep .5s.
The conversation should be read/writable via an endpoint.
I want a page that will refresh the conv every 1s by asking an endpoint. It should stop refreshing when locked = true.




__-__

assistant:I need a sophisticated conversation debugger tool with the following specifications:

1. Conversation Display:
   - Implement a visually appealing and user-friendly display for the conversation.
   - Use a card-based layout with different background colors for user and assistant messages.
   - Include timestamps and a scrollable view for long conversations.
   - Provide options for customizing the styling based on user preferences.

2. Styling:
   - Use a modern, clean design with a light background color and a consistent color scheme.
   - Ensure optimal readability with a readable font family and appropriate font sizes.
   - Implement responsive design for seamless viewing on different screen sizes.
   - Incorporate subtle animations and transitions to enhance the user experience.

3. Endpoint Functionality:
   - Implement a `/api/conversation` endpoint that accepts `POST` requests to update the conversation.
   - Validate the incoming conversation object to ensure data integrity.
   - Overwrite the existing conversation in the `prompts/_debug.conv` file with the updated data.
   - Provide meaningful error responses for invalid requests.
   - Return a success response upon successful update of the conversation.

4. Additional Features:
   - Implement search functionality to allow searching for keywords or phrases within the conversation.
   - Provide filtering options based on role (user or assistant) and timestamp range.
   - Allow exporting the conversation in different formats (JSON, CSV, PDF) for further analysis.
   - Implement pagination to efficiently load and display long conversations.
   - Enable user






TODO DEMAIN:
create entities,
create endpoints,
create serve
create enpoints