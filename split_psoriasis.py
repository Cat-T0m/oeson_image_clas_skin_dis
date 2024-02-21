import os, shutil, random

# preparing the folder structure

split_percentage = 90

images_path = 'data2/Psoriasis/'
    

    
training_images_path = 'skind_training2/Psoriasis/'
validation_images_path = 'skind_validation2/Psoriasis/'
    
os.mkdir(training_images_path)
os.mkdir(validation_images_path)

files = []



for r, d, f in os.walk(images_path):
    for file in f:
        strip=file[0:len(file)]
        files.append(strip)

random.shuffle(files)

size = len(files)                   

split = int(split_percentage * size / 100)

print(files[split])
print("copying training data")
for i in range(split):
    image_file = files[i] 
    print(images_path)
    print(image_file)
    src_image = images_path + image_file
    shutil.copy(src_image, training_images_path) 
                         
    
print("copying validation data")
for i in range(split, size):
    f = files[i]
                         
    image_file = f
    src_image = images_path + image_file
    shutil.copy(src_image, validation_images_path) 
                         
    
    
print("finished")
