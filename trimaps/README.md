# Fixed trimaps
Several .PNG files inside the `annotations/trimaps` folder, also known as mask files, appear to only contain values of 2. We replace them by three-digit masks, similar to the rest of the annotations dataset. Due to the complexitiy of manually producing them, we run inference on their correpsonding images using a trained Mask-RCNN model.

In order to identify them, it's important to set `faces_only` to `False` when running the `create_pet_tf_record.py` script. So far the following have been recorded

```
Egyptian_Mau_162
Egyptian_Mau_165
Egyptian_Mau_196
leonberger_18
miniature_pinscher_14
saint_bernard_15
saint_bernard_108
```
