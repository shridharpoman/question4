
import os
GPU_ID = "0"

#####################  PATHS  ######################################
imagenet_dir = "/content/drive/MyDrive/images/"
imagenet_wind_dir = os.path.join(imagenet_dir,"training/")
external_images_dir =  os.path.join(imagenet_dir,"test/")

project_dir = "/content/ssfmri2im/"
images_npz = os.path.join(project_dir,"data/images_112.npz")
kamitani_data_format = True
kamitani_data_mat = '/content/drive/MyDrive/question4/Subject3.mat'
caffenet_models_weights = '/content/drive/MyDrive/question4/imagenet-caffe-ref.mat'
results  = os.path.join(project_dir,"results/")


encoder_weights = os.path.join(project_dir,"models/encoder.hdf5")
retrain_encoder = False
decoder_weights = None

encoder_tenosrboard_logs = None
decoder_tenosrboard_logs = None


#####################  pretrained mat conv net weights (alexnet)  ######################################

DOWNLOAD_LINK = 'http://www.vlfeat.org/matconvnet/models/imagenet-caffe-ref.mat'
FILENAME = 'imagenet-caffe-ref.mat'
EXPECTED_BYTES = 228031200

##################### PARAMS ######################################

image_size = 112