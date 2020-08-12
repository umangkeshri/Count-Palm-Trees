# Count-Palm-Trees

![CI](https://github.com/umangkeshri/Count-Palm-Trees/workflows/CI/badge.svg)

OpenCV implementation of watershed algorithm for drawing segemnts in images and counting the number of Palm trees.


## Running Application

1. Execute below command:

    `docker run -p 8360:8360 umangkeshri/count_trees`

2. Test with cURL:
    * Get number of trees in image:
    
            ```shell
            curl --location --request POST '0.0.0.0:8360/countPalmTrees' \
            --header 'Content-Type: application/json' \
            --form 'file=@{path/to/image/file}'
            ```
    
    * Get image with tagged locations:
    
            ```shell
            curl --location --request POST '0.0.0.0:8360/countPalmTrees' \
            --header 'Content-Type: application/json' \
            --form 'file=@{path/to/image/file}' \
            --form 'image={yes/no}'
            ```
