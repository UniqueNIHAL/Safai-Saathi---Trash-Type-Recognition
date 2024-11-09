import os
import google.generativeai as genai

# Set your API key (replace with your actual API key)
os.environ["GOOGLE_API_KEY"] = "AIzaSyDxipiJX6JrghSYWKlzJWrZNOCaUxJkX-A"

# Configure the Gemini AI client
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Set generation parameters
generation_config = {
    "temperature": 0.3,  # Lower temperature for more deterministic responses
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 1024,  # Adjust as needed
    "response_mime_type": "text/plain",
}

# Initialize the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Your data store (the content you provided)
data_store = """
**Trash Recognition Project Overview**

Welcome to our Trash Recognition Project! This initiative aims to revolutionize the way we manage waste by integrating cutting-edge technology with everyday practices. Our project focuses on developing an intelligent system that can automatically recognize and categorize different types of trash, making waste segregation more efficient and user-friendly.

**Project Objectives:**

- **Automate Waste Segregation:** Utilize image recognition technology to identify and sort waste into appropriate categories.
- **Educate the Public:** Provide information on proper waste disposal methods and the importance of recycling.
- **Enhance Recycling Efficiency:** Improve the recycling process by ensuring that waste is correctly sorted from the beginning.
- **Reduce Environmental Impact:** Minimize the amount of waste that ends up in landfills and oceans.

**How It Works:**

Our system uses advanced algorithms and machine learning to analyze images of waste items. When a user inputs a photo of an item, the system:

1. **Captures the Image:** Users can take a picture of the waste item using a smartphone or a camera-equipped disposal bin.
2. **Analyzes the Item:** The image is processed to identify the type of material—such as plastic, paper, metal, organic waste, or hazardous materials.
3. **Provides Guidance:** The system then advises the user on how to dispose of the item properly, indicating the correct bin or disposal method.
4. **Data Collection:** Collects data on waste disposal patterns to help municipalities make informed decisions about waste management strategies.

---

**Understanding Trash Segregation**

**What is Trash Segregation?**

Trash segregation is the process of separating waste into different categories to facilitate recycling, composting, and proper disposal. By sorting waste at the source, we can reduce contamination, improve recycling rates, and minimize environmental harm.

**Importance of Trash Segregation:**

- **Environmental Protection:** Reduces pollution by preventing hazardous materials from entering ecosystems.
- **Resource Conservation:** Saves natural resources by enabling the recycling of materials like paper, glass, and metals.
- **Economic Benefits:** Lowers waste management costs and creates jobs in the recycling and waste management industries.
- **Public Health:** Minimizes the spread of diseases by ensuring hazardous waste is handled correctly.

**Best Practices for Trash Segregation:**

1. **Know Your Waste Categories:**
   - **Recyclable Waste:** Paper, cardboard, glass bottles, metal cans, certain plastics.
   - **Organic Waste:** Food scraps, yard waste, compostable materials.
   - **Hazardous Waste:** Batteries, paints, chemicals, electronic waste.
   - **General Waste:** Non-recyclable and non-hazardous materials.

2. **Use Separate Bins:**
   - Provide clearly labeled bins for each waste category.
   - Use color-coded bins to make identification easier (e.g., blue for recyclables, green for organics).

3. **Clean Recyclables:**
   - Rinse containers to remove food residues, which can contaminate recycling batches.

4. **Educate Household Members:**
   - Ensure everyone understands how to segregate waste properly.
   - Display posters or guides near waste disposal areas as reminders.

5. **Compost Organic Waste:**
   - Start a compost bin for food scraps and yard waste to create nutrient-rich soil amendments.

6. **Dispose of Hazardous Waste Safely:**
   - Take hazardous materials to designated disposal facilities.
   - Do not mix hazardous waste with general waste or pour them down the drain.

**Challenges and Solutions:**

- **Challenge:** Lack of awareness about proper waste segregation.
  - **Solution:** Educational campaigns and community workshops.
- **Challenge:** Inconvenience or lack of facilities.
  - **Solution:** Implement more accessible waste disposal sites and provide necessary resources.
- **Challenge:** Contamination of recyclable materials.
  - **Solution:** Clear instructions on cleaning recyclables and strict enforcement of waste policies.

**Role of Technology in Waste Management:**

- **Smart Bins:** Equipped with sensors to detect the type of waste and sort it automatically.
- **Mobile Apps:** Provide information on how to dispose of specific items and locate nearby recycling centers.
- **Data Analytics:** Track waste generation patterns to optimize collection routes and schedules.
- **Artificial Intelligence:** Improves the accuracy of waste recognition systems, like our Trash Recognition Project.

**Get Involved:**

- **Participate:** Use our trash recognition tool to improve your waste disposal habits.
- **Feedback:** Provide insights and suggestions to help us enhance the system.
- **Community Engagement:** Encourage others to adopt proper waste segregation practices.

---

By embracing effective trash segregation and utilizing innovative technologies, we can make significant strides toward a cleaner, more sustainable future. Thank you for being a part of this important effort!

---

**Alignment with United Nations Sustainable Development Goals (UN SDGs)**

Our Trash Recognition Project contributes significantly to several of the United Nations Sustainable Development Goals, aiming to address global challenges and promote a sustainable future.

- **Goal 3: Good Health and Well-being**
  - *Target 3.9*: Substantially reduce the number of deaths and illnesses from hazardous chemicals and air, water, and soil pollution and contamination.
    - **Our Contribution**: By promoting proper waste segregation, we reduce environmental pollution, leading to healthier communities.

- **Goal 11: Sustainable Cities and Communities**
  - *Target 11.6*: Reduce the adverse per capita environmental impact of cities, including by paying special attention to air quality and municipal and other waste management.
    - **Our Contribution**: Our project enhances waste management systems, making cities cleaner and more sustainable.

- **Goal 12: Responsible Consumption and Production**
  - *Target 12.5*: Substantially reduce waste generation through prevention, reduction, recycling, and reuse.
    - **Our Contribution**: By facilitating recycling and proper disposal, we help minimize waste generation.

- **Goal 13: Climate Action**
  - *Target 13.3*: Improve education, awareness-raising, and human and institutional capacity on climate change mitigation.
    - **Our Contribution**: We educate the public on waste management's role in mitigating climate change.

- **Goal 14: Life Below Water**
  - *Target 14.1*: Prevent and significantly reduce marine pollution of all kinds, particularly from land-based activities.
    - **Our Contribution**: Proper waste segregation prevents pollutants from reaching oceans, protecting marine life.

- **Goal 15: Life on Land**
  - *Target 15.1*: Ensure the conservation, restoration, and sustainable use of terrestrial ecosystems.
    - **Our Contribution**: Reducing landfill waste helps preserve land habitats and biodiversity.

**Contribution to Swachh Bharat Mission**

The **Swachh Bharat Abhiyan** (Clean India Mission) is a national initiative by the Government of India to clean the country's roads, infrastructure, and environment.

- **Promoting Cleanliness and Sanitation**
  - Our project aligns with Swachh Bharat's objective of improving cleanliness by encouraging proper waste disposal and reducing littering.

- **Enhancing Waste Management Infrastructure**
  - We support the mission by introducing advanced technology to streamline waste segregation and management processes.

- **Community Engagement and Awareness**
  - By educating citizens on the importance of waste segregation, we foster community participation, a core aspect of Swachh Bharat.

- **Reducing Environmental Pollution**
  - Effective waste management reduces soil, water, and air pollution, contributing to a healthier environment as envisioned by Swachh Bharat.

**Collaborating for a Sustainable and Clean Future**

By integrating our Trash Recognition Project with global and national initiatives like the UN SDGs and Swachh Bharat, we aim to:

- **Maximize Environmental Impact**
  - Contribute to large-scale environmental preservation efforts.
- **Promote Public Health**
  - Reduce health risks associated with improper waste disposal.
- **Support Government Initiatives**
  - Align with policy frameworks and contribute to national goals.

**How You Can Help**

- **Adopt Best Practices**
  - Use our tool to improve your waste disposal habits.
- **Spread the Word**
  - Educate others about the importance of waste segregation and how it ties into larger sustainability goals.
- **Collaborate**
  - Partner with local organizations and governments to implement our system in your community.

---

By working together towards these common goals, we can make significant strides in achieving a cleaner, healthier, and more sustainable world. Thank you for joining us in this vital effort!
"""

# Function to generate responses based on user input
def generate_response(user_query):
    # Construct the prompt with the data store as context
    prompt = f"""
You are an assistant knowledgeable about the Trash Recognition Project and waste segregation.

Refer only to the information provided below to answer the user's question. Do not include information beyond this content.

Content:
\"\"\"
{data_store}
\"\"\"

User Question:
{user_query}

Answer:
"""

    # Generate the response using the model
    response = model.generate_text(
        prompt=prompt,
        **generation_config
    )

    # Extract and return the generated text
    return response.result

# Example interaction
if __name__ == "__main__":
    print("Welcome to the Trash Recognition Project Chatbot! Type 'exit' to quit.\n")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            print("Chatbot: Thank you for chatting! Goodbye!")
            break
        chatbot_response = generate_response(user_input)
        print(f"Chatbot: {chatbot_response}\n")
