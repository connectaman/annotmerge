# importing libraries
import os
import time
import shutil
import logging

# creating a new log file
logger = logging.getLogger()
logging.basicConfig(filename='output.log')
logger.setLevel(logging.INFO)
# Place the dataset Folders inside the dataset folder

logging.info("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
logging.info('                                         TASK STARTED                                               ')
logging.info("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
def merge(dataset_dir='dataset/'):
    """
    @Author : Aman Ulla
     
    """
    dataset_base_dir = dataset_dir
    start_time = time.time()
    logging.info('Reading the dataset folder')
    print('Reading the dataset folder')
    try:
        folders = os.listdir(dataset_dir)
    except:
        raise Exception('Directory Not Found')
    end_time = time.time()
    logging.info(f'Time Taken to Read dataset folder {end_time-start_time} seconds')
    # Check if no folders present in dataset folder
    if len(folders) == 0:
        print('No Folders Found in DataSet Folder')
        logging.error('No Folders Found in DataSet Folder')
        # Throw Error if no folder present in the dataset folder
        raise Exception('The Dataset Directory is Empty')
    # Checking if one folder present
    elif len(folders) == 1:
        print('Only 1 Folder Found in the Dataset Directory')
        logging.error('Only 1 Folder Found in the Dataset Directory')
        # Throw error since we cannot merge one folder
        raise Exception('Found 1 Directory, You need minimum two folders to merge.')
    elif len(folders) >= 2:
        print(f'Found Folders in Dataset, Folder Names are {folders}')
        logging.info(f'Found Folders in Dataset, Folder Names are {folders}')
        # Creating New Director named OUTPUT to place the merged file
        try:
            print('Created Output Folder named "OUTPUT"')
            print('Structure of OUTPUT Folder : --Output/Annotations --Output/ImageSets --Output/ImageSets/Action --Output/ImageSets/Layout --Output/ImageSets/Main --Output/JPEGImages')
            logging.info('Created Output Folder named "OUTPUT"')
            logging.info('Structure of OUTPUT Folder : --Output/Annotations --Output/ImageSets --Output/ImageSets/Action --Output/ImageSets/Layout --Output/ImageSets/Main --Output/JPEGImages')
            os.makedirs('output')
            os.makedirs('output/Annotations')
            os.makedirs('output/ImageSets')
            os.makedirs('output/ImageSets/Action')
            os.makedirs('output/ImageSets/Layout')
            os.makedirs('output/ImageSets/Main')
            os.makedirs('output/JPEGImages')
        except OSError:
            pass
        # Iterate Over every Folder and read the contents and move it to the merged Folder
        for i,folder in enumerate(folders):
            print(f'Reading Folder Number {i+1} and Name {folder}')  
            logging.info('---------------------------------------------------------------------------------------------')
            logging.info(f'Reading Folder Number {i+1} and Name {folder}')  
            # Read the annotation xml file in a list
            folder_annotation_files = os.listdir(os.path.join(dataset_base_dir+folder,'Annotations'))
            print(f'Number of Annotation Files in {folder} is {len(folder_annotation_files)}')
            logging.info(f'Number of Annotation Files in {folder} is {len(folder_annotation_files)}')
            # If no annotation file present then throw error
            if len(folder_annotation_files) == 0:
                print(f'No Files Present in --Dataset/{folder}/Annotations')
                logging.warning(f'No Files Present in --Dataset/{folder}/Annotations')
            # If annotation file present then copy the annotations xml files
            elif len(folder_annotation_files) >= 1:
                start_time = time.time()
                # Copying the Images from JPEGImages folder
                print(f'Copying Content from --dataset/{folder}/JPEGImages to --output/JPEGImages')
                logging.info(f'Copying Content from --dataset/{folder}/JPEGImages to --output/JPEGImages')
                print(f'Number of Images in --dataset/{folder}/JPEGImages')
                logging.info(f'Number of Images in --dataset/{folder}/JPEGImages')
                for im in os.listdir("{0}/JPEGImages".format(f'dataset/{folder}')):
                    logging.info("Processing JPEG: {0} from {1}".format(im,folder))
                    path = "dataset/{0}/JPEGImages/{1}".format(folder,im)
                    target = "output/JPEGImages/{0}".format(im)
                    shutil.copyfile(path, target)
                end_time = time.time()
                print(f'Copying Content from --dataset/{folder}/JPEGImages to --output/JPEGImages Completed')
                logging.info(f'Copying Content from --dataset/{folder}/JPEGImages to --output/JPEGImages Completed')
                print(f'Time Taken to Copy Content from --dataset/{folder}/JPEGImages to --output/JPEGImages is {end_time-start_time}')
                logging.info(f'Time Taken to Copy Content from --dataset/{folder}/JPEGImages to --output/JPEGImages is {end_time-start_time}')
                # Getting image copied to the Output folder
                copied_len = os.listdir('output/JPEGImages')
                print(f'Total Image Files in --output/JPEGImages : {len(copied_len)}')
                logging.info(f'Total Image Files in --output/JPEGImages : {len(copied_len)}')
                # Copying Annotation Files
                print(f'Copying Content from --dataset/{folder}/Annotations to --output/Annotations')
                logging.info(f'Copying Content from --dataset/{folder}/Annotations to --output/Annotations')
                src = os.path.join(dataset_base_dir ,os.path.join(folder,'Annotations'))
                dsc = os.path.join('output','Annotations')
                start_time = time.time()
                for file in folder_annotation_files:
                    logging.info('Copying file {0} from --dataset/{1} to --output/Annotations'.format(file,folder))
                    with open(os.path.join(src,file), 'r') as f: 
                        data = f.read()
                    with open(os.path.join(dsc,file),'w') as f:
                        f.write(data)
                f.close()
                end_time = time.time()
                print(f'Time taken to Copy Content from --dataset/{folder}/Annotations to --output/Annotations : {end_time-start_time}')
                logging.info(f'Time taken to Copy Content from --dataset/{folder}/Annotations to --output/Annotations : {end_time-start_time}')
                copied_annotations_file = os.listdir(dsc)
                print(f'Total Annotations Files in --output/Annotations : {len(copied_annotations_file)}')
                logging.info(f'Total Annotations Files in --output/Annotations : {len(copied_annotations_file)}')
                # Copying Action Folder files
                print('Copying Content from --dataset/{0}/ImageSets/Action to --output/ImageSets/Action'.format(folder))
                logging.info('Copying Content from --dataset/{0}/ImageSets/Action to --output/ImageSets/Action'.format(folder))
                start_time = time.time()
                src = os.path.join(os.path.join(os.path.join('dataset',folder),'ImageSets'),'Action')
                dsc = os.path.join(os.path.join('output','ImageSets'),'Action')
                action_default_file = os.path.join(src,'default.txt')
                with open(action_default_file,'r') as f:
                    data = f.read()
                with open(dsc+'\\default.txt','a') as f:
                    f.write(data)
                f.close()
                end_time = time.time()
                print(f'Time taken to Copy Content from --dataset/{folder}/ImageSets/Action to --output/ImageSets/Action : {end_time-start_time}')
                logging.info(f'Time taken to Copy Content from --dataset/{folder}/ImageSets/Action to --output/ImageSets/Action : {end_time-start_time}')
                # Reading Layout Folder
                print('Copying Content from --dataset/{0}/ImageSets/Layout to --output/ImageSets/Layout'.format(folder))
                logging.info('Copying Content from --dataset/{0}/ImageSets/Layout to --output/ImageSets/Layout'.format(folder))
                start_time = time.time()
                src = os.path.join(os.path.join(os.path.join('dataset',folder),'ImageSets'),'Layout')
                dsc = os.path.join(os.path.join('output','ImageSets'),'Layout')
                layout_default_file = os.path.join(src,'default.txt')
                with open(layout_default_file,'r') as f:
                    data = f.read()
                with open(dsc+'\\default.txt','a') as f:
                    f.write(data)
                f.close()
                end_time = time.time()
                print(f'Time taken to Copy Content from --dataset/{folder}/ImageSets/Layout to --output/ImageSets/Layout : {end_time-start_time}')
                logging.info(f'Time taken to Copy Content from --dataset/{folder}/ImageSets/Layout to --output/ImageSets/Layout : {end_time-start_time}')
                # Reading Main Folder
                print('Copying Content from --dataset/{0}/ImageSets/Main to --output/ImageSets/Main'.format(folder))
                logging.info('Copying Content from --dataset/{0}/ImageSets/Main to --output/ImageSets/Main'.format(folder))
                start_time = time.time()
                src = os.path.join(os.path.join(os.path.join('dataset',folder),'ImageSets'),'Main')
                dsc = os.path.join(os.path.join('output','ImageSets'),'Main')
                layout_default_file = os.path.join(src,'default.txt')
                with open(layout_default_file,'r') as f:
                    data = f.read()
                with open(dsc+'\\default.txt','a') as f:
                    f.write(data)
                f.close()
                end_time = time.time()
                print(f'Time taken to Copy Content from --dataset/{folder}/ImageSets/Main to --output/ImageSets/Main : {end_time-start_time}')
                logging.info(f'Time taken to Copy Content from --dataset/{folder}/ImageSets/Main to --output/ImageSets/Main : {end_time-start_time}')
                # Reading LabelMap
                print('Copying Content from --dataset/{0}/LabelMap to --output/LabelMap'.format(folder))
                logging.info('Copying Content from --dataset/{0}/LabelMap to --output/LabelMap'.format(folder))
                start_time = time.time()
                src =  os.path.join('dataset',folder)
                labelmap_file = os.path.join(src,'labelmap.txt')
                with open(labelmap_file,'r') as f:
                    data = f.read()
                with open('output'+'\\labelmap.txt','w') as f:
                    f.write(data)
                f.close()
                end_time = time.time()
                print(f'Time taken to Copy Content from --dataset/{folder}/LabelMap to --output/LabelMap : {end_time-start_time}')
                logging.info(f'Time taken to Copy Content from --dataset/{folder}/LabelMapto --output/LabelMap : {end_time-start_time}')

                logging.info("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                logging.info('                                         TASK COMPLETE                                              ')
                logging.info("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
