# Count-Palm-Trees

![CI](https://github.com/umangkeshri/Count-Palm-Trees/workflows/CI/badge.svg)

OpenCV implementation of watershed algorithm for drawing segemnts in images and counting the number of Palm trees.


## Running Application

1. Execute below command:

    `docker run -p 8360:8360 umangkeshri/count_trees`

2. Test with cURL:

    `curl --location --request POST '0.0.0.0:8360/countPalmTrees' --form 'image=@{path/to/image/file}'`
