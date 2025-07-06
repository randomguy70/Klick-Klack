from datetime import datetime

import extract_data
import train

#### Running this file compiles your data, extracts features, trains your digraph and trigraph models, and saves the models.
#### To predict the typist of a random sample, run predict.py

starttime = datetime.now()
extract_data.run('./Raw_Data/', './Extracted_Data/')
print(f"Delta Time: {datetime.now() - starttime}")

starttime = datetime.now()
train.full_train()
print(f"Delta Time: {datetime.now() - starttime}")