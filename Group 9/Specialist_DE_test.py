# imports framework
import sys, os
import numpy as np
from deap import base
from deap import benchmarks
from deap import creator
import random
import array
from deap import tools
sys.path.insert(0, 'evoman') 
from environment import Environment
from demo_controller import player_controller
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.environ["SDL_VIDEODRIVER"] = "dummy"

hidden_units_num=10
chorosome_len = (20+1) * hidden_units_num + (hidden_units_num+1)*5

'''
enemy1: exp_enemy_[1]_round_0
enemy2: exp_enemy_[2]_round_0
enemy3: exp_enemy_[3]_round_6
'''

enemies=[1,2,3]
rounds=10
eas=[0,1,2]
for ea in eas:
    for enemy in enemies:
        for r in range(rounds):
            path='experiments_data/%d_enemy_[%d]_round_%d' % (ea,enemy,r)
            if(os.path.exists(path+"/test.txt")):
                os.remove(path+"/test.txt")
            for repeat in range(5):
                env = Environment(experiment_name=path,
                      enemies=[enemy],
                    playermode="ai",
                    player_controller=player_controller(10),
                    enemymode="static",
                    level=2,
                    # randomini='yes',
                    speed="fastest")
                file_aux=open(path+'/best.txt')
                weights=file_aux.readlines()
                file_aux.close()
                inputs=np.array(list(map(lambda y: float(y),weights)))
                f,p,e,t=env.play(pcont=inputs)
                file_aux  = open(path+'/test.txt','a')
                file_aux.write('\n'+str(f)+'\t'+str(p)+'\t'+str(e)+'\t'+str(t))
                file_aux.close()
