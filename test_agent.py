from agent.agent_ppt import PPTGenieAgent

# Creating agent instance
agent = PPTGenieAgent()

# Test input 
topic = input("Enter topic: ")

# Running the agent
result = agent.run(topic)

print(result)