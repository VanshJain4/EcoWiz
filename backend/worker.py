from ultralytics import YOLO
from PIL import Image
from fastai.vision.all import load_learner

import re, os, logging
#import pathlib
#temp = pathlib.PosixPath
#pathlib.PosixPath = pathlib.WindowsPath

resnet50_Model = load_learner('classifier/result-resnet50.pkl')
nonLivingObjects = [
    1,2,3,4,5,6,7,8,9,10,
    11,12,13,24,25,26,27,28,29,30,
    31,32,33,34,35,36,37,38,39,40,
    41,42,43,44,45,46,47,48,49,50,
    51,52,53,54,55,56,57,58,59,60,
    61,62,63,64,65,66,67,68,69,70,
    71,72,73,74,75,76,77,78,79
]

def truncate(num):
   return re.sub(r'^(\d+\.\d{,3})\d*$',r'\1',str(num))


def predictWaste(filename):
    response = []
    img = Image.open(filename)
    YOLOv8_model = YOLO('yolov8n.pt')  # pretrained YOLOv8n model
    results = YOLOv8_model(img)
    for result in results:
        detection_count = result.boxes.shape[0]
        for i in range(detection_count):
            cls = int(result.boxes.cls[i].item())
            name = result.names[cls]
            confidence = truncate(float(result.boxes.conf[i].item()))
            bounding_box = result.boxes.xyxy[i].cpu().numpy()
            
            if cls not in nonLivingObjects:
                continue
            
            newFile = f"{filename.split('.')[0]}-{len(response)}.{filename.split('.')[-1]}"
            img.crop(bounding_box).save(newFile)
            
            prediction = resnet50_Model.predict(newFile)
            num = int(prediction[1].numpy().tolist())
            prob = truncate(float(prediction[2].numpy()[num]))
            logging.debug('%s', f'Classified as {prediction[0]}, Class number {num} with probability {prob}')
            response.append(
                {
                    'object_name': name,
                    'object_confidence': confidence,
                    'waste_predicted': prediction[0], 
                    'waste_probability': prob
                }
            )
            os.remove(newFile)

    return response

if __name__ == '__main__':
    imagePath = 'zidane.jpg'
    print(predictWaste(imagePath))
