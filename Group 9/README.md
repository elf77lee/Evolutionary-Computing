System requirements:
python 3.7.0
DEAP 1.3.1

Specialist_DE_random.py-> DE/rand
Specialist_DE_best.py  -> DE/best
baseline               -> standard GA

The experiment data will be created in the experiments_data folder.
Foldernames are like i_enemy_[j]_round_k, where i represents the index of EA. 0:baseline 1:EA1 2:EA2. And j is from 1 to 3, corresponeds to the three enemies in EvoMan.

Speciallist_DE_test.py computes statistics for gain boxplot, relying the data inexperiments_data.

Run the four python files simply like:
python Specialist_DE_random.py
