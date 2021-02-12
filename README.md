#annotmerge

This Library helps in merging multiple Pascall VOC Annotation file into a single Annotation.

The Package contains a single function called merge. Which takes a single param: base_directory
you need to specity the folder name where your multiple annotation files are present and then a log 
is created and also output directory is created with merged files and folders

The Structure of folder
--dataset/
    -- annotation folder/
        --Annotations/
        --ImageSets
        --JPEGImages
        --labelmaps.txt
    -- annotation folder 2/
        --Annotations/
        --ImageSets
        --JPEGImages
        --labelmaps.txt
    -- ....
    -- ....
    -- annotation folder n/
        --Annotations/
        --ImageSets
        --JPEGImages
        --labelmaps.txt 

Output/Result

--output/
    --Annotations/
    --ImageSets
    --JPEGImages
    --labelmaps.txt
