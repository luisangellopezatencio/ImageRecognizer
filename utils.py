import io
import datetime
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import json

# model
model = models.densenet121(weights='IMAGENET1K_V1')
model.eval()

#imageNet classes
imagenet_class_index = json.load(open('./static/imagenet_class_index.json'))

#Extraido de la documentacion de pytorch https://pytorch.org/tutorials/intermediate/flask_rest_api_tutorial.html
def transform_image(image_bytes):
    my_transforms = transforms.Compose([transforms.Resize(255),
                                        transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                            [0.485, 0.456, 0.406],
                                            [0.229, 0.224, 0.225])])
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)


def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    return imagenet_class_index[predicted_idx]

def get_result(image_file):
    start_time = datetime.datetime.now()
    image_byte = image_file.file.read()
    class_id, class_name = get_prediction(image_bytes=image_byte)
    end_time = datetime.datetime.now()

    time_diff = (end_time-start_time)
    execution_time = f'{round(time_diff.total_seconds() * 1000)} ms'
    result = {
        "inference_time": execution_time,
        "predictions": {
            "class_id": class_id,
            "class_name": class_name
        }
            }
    return result