# Recipe Modificaion

Script for Semiteq ICP200E recipe modification

![](http://semiteq.ru/images/cms/catalog/ste-icp200ef-open.jpg)

This script adjusts old files to fit the new recipe requirements.

---

## Usage

To run the script specific flag should be used such as `recipy_modify your/path/to.file [flag]`. You may provide more than one file.

No flag (parsing will run by default)

The script will replace the existing "Время" column with two new ones, labled "Время в начале" and "Время в конце". It will then fill both columns with data from the previous "Время" fields.
    
This is done so that process times can be changed depending on the completion of steps.
    
`-o, --output`

With this flag, you can provide a custom output directory. If no flag provided then the input directory will be used by default.

`-v, --version`

Will show you the version.
