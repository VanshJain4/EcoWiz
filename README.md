# EcoWiz

## Inspiration
The major inspiration for our team for this project came from observing that, even with proper garbage disposals, it is sometimes challenging to ensure correct segregation in the respective trash cans.

## What It Does
Our project utilizes two Computer Vision models (ResNet-50 CNN deep learning model and YoloV8) and integrates them to effectively classify garbage based on whether they are organic, trash, or recyclable. It creates a multimodal system where, via a camera, you can take a snapshot and then use YoloV8 to mark each object. After that, we use ResNet-50 to classify them as recyclable, compost, or plastic.

## Challenges We Faced
We faced several challenges, from navigating through a snowstorm to staying awake for more than 24 hours straight. However, we learned that there was no challenge that could stop us from having a memorable hackathon. On the technical side, Computer Vision and Frontend development were new fields for all of us, so we encountered issues like centring a div. In Computer Vision, we faced a problem where our model performed well on given images but poorly on real images from our camera. We theorized it could be due to many objects shown at a given time. We solved this problem via YoloV8 multiclass classification of objects in a given image. Then we used our model to classify every object.

## What We Learned
We learned a lot from this hackathon. We believe that we learned a great deal about teamwork and effective collaboration. As we delved into a domain where we had little to no experience, we gained insights into Computer Vision, different models, and when to implement them. We also learned the importance of a good dataset. Ultimately, we understood the saying that a model is a reflection of its dataset.

## Accomplishments We Are Proud Of
We are extremely proud that we stepped out of our comfort zones and explored a field unfamiliar to us, namely, Computer Vision. In doing so, we contributed to an eco-friendly future through our implemented solution. Additionally, we are proud to venture into uncharted territories of computer vision and learn from the experience. Lastly, we are extremely proud of our project as it implements our first multimodal system.

## Future of Eco Wiz
Talking about long-term ambitions, we at Eco Wiz strive for a more eco-friendly future. For that, we see that our technology has a future in the waste management industry. We believe that our multimodal system can be made more efficient when combating sea waste by training it on a similar dataset. We also think our multimodal system can be used to automate classification tasks in the waste management industry.

## Technologies Used
We primarily used the ResNet-50 CNN deep learning model for classifying garbage. Additionally, we leveraged the YoloV8 model to solve the problem of predicting multiple objects. This was done by taking a snapshot of the video and splitting every recognized object by the YoloV8 model into their own separate images. Then we used the ResNet-50 model to classify every given object. We used Python and Flask in the backend. In the frontend, we used JavaScript, HTML, CSS, React, and Vite.
