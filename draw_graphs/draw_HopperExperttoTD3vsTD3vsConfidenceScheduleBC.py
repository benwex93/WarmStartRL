import numpy as np
import os
from matplotlib import pyplot as plt
import copy
import seaborn as sns; sns.set()
from ConfidenceScheduleBC_metrics import print_metrics

class DrawGraphs:
	def __init__(self):
		pass
	def draw(self):

		results_dir='../results/'

		ExperttoTD3Hopper_evaluations_dir1 = results_dir + 'Hopper-v3_results/TD3_Hopper-v3_0_2021-12-27 15:34:57.8745772021-12-27 15:34:57.875023'
		ExperttoTD3Hopper_evaluations_dir2 = results_dir + 'Hopper-v3_results/TD3_Hopper-v3_1_2021-12-27 18:42:33.1105842021-12-27 18:42:33.110973'
		ExperttoTD3Hopper_evaluations_dir3 = results_dir + 'Hopper-v3_results/TD3_Hopper-v3_2_2021-12-27 22:47:43.1387302021-12-27 22:47:43.139094'
		ExperttoTD3Hopper_evaluations_dir4 = results_dir + 'Hopper-v3_results/TD3_Hopper-v3_3_2021-12-28 02:05:38.1828732021-12-28 02:05:38.183159'
		ExperttoTD3Hopper_evaluations_dir5 = results_dir + 'Hopper-v3_results/TD3_Hopper-v3_4_2021-12-28 04:51:33.2137222021-12-28 04:51:33.214031'
		TD3Hopper_evaluations_dir1 = results_dir + 'Hopper-v3_results/TD3_Hopper-v3_1_2021-12-28 19:09:34.3959692021-12-28 19:09:34.396277'
		TD3Hopper_evaluations_dir2 = results_dir + 'Hopper-v3_results/TD3_Hopper-v3_2_2021-12-29 01:52:25.6338392021-12-29 01:52:25.633937'
		TD3Hopper_evaluations_dir3 = results_dir + 'Hopper-v3_results/TD3_Hopper-v3_3_2021-12-29 07:49:08.2000782021-12-29 07:49:08.200449'
		TD3Hopper_evaluations_dir4 = results_dir + 'Hopper-v3_results/TD3_Hopper-v3_4_2021-12-29 13:07:01.5267102021-12-29 13:07:01.526795'
		TD3Hopper_evaluations_dir5 = results_dir + 'Hopper-v3_results/TD3_Hopper-v3_0_2021-12-29 18:27:14.2190282021-12-29 18:27:14.219403'
		
		# BC_Uncertainty_evaluations_dir1 = results_dir + 'Hopper-v3_results/TD3_BC_Uncertainty_Hopper-v3_0_2021-12-29 14:50:01.3617132021-12-29 14:50:01.361835'
		# BC_Uncertainty_evaluations_dir2 = results_dir + 'Hopper-v3_results/TD3_BC_Uncertainty_Hopper-v3_1_2021-12-29 21:09:29.8605492021-12-29 21:09:29.860667'
		# BC_Uncertainty_evaluations_dir3 = results_dir + 'Hopper-v3_results/TD3_BC_Uncertainty_Hopper-v3_2_2021-12-30 02:12:01.6658742021-12-30 02:12:01.666245'
		# BC_Uncertainty_evaluations_dir4 = results_dir + 'Hopper-v3_results/TD3_BC_Uncertainty_Hopper-v3_3_2021-12-30 05:00:49.9923552021-12-30 05:00:49.992823'
		# BC_Uncertainty_evaluations_dir5 = results_dir + 'Hopper-v3_results/TD3_BC_Uncertainty_Hopper-v3_4_2021-12-30 08:01:30.0183632021-12-30 08:01:30.018889'
			
		BC_Uncertainty_evaluations_dir1 = results_dir + 'Hopper-v3_results/TD3CP_Hopper-v3_0_2022-01-09 17:05:52.2413032022-01-09 17:05:52.241725'
		BC_Uncertainty_evaluations_dir2 = results_dir + 'Hopper-v3_results/TD3CP_Hopper-v3_1_2022-01-09 19:30:08.9340972022-01-09 19:30:08.934234'
		BC_Uncertainty_evaluations_dir3 = results_dir + 'Hopper-v3_results/TD3CP_Hopper-v3_2_2022-01-09 22:32:47.1933082022-01-09 22:32:47.193661'
		BC_Uncertainty_evaluations_dir4 = results_dir + 'Hopper-v3_results/TD3CP_Hopper-v3_3_2022-01-10 01:33:08.3446112022-01-10 01:33:08.344933'
		BC_Uncertainty_evaluations_dir5 = results_dir + 'Hopper-v3_results/TD3CP_Hopper-v3_4_2022-01-10 05:14:21.3675142022-01-10 05:14:21.367699'
		
		###########################

		ExperttoTD3Hopper_evaluations1, ExperttoTD3Hopper_evaluations2, ExperttoTD3Hopper_evaluations3,\
			ExperttoTD3Hopper_evaluations4, ExperttoTD3Hopper_evaluations5 = [], [], [], [], []

		TD3Hopper_evaluations1, TD3Hopper_evaluations2, TD3Hopper_evaluations3,\
			TD3Hopper_evaluations4, TD3Hopper_evaluations5 = [], [], [], [], []

		BC_Uncertainty_evaluations1, BC_Uncertainty_evaluations2, BC_Uncertainty_evaluations3,\
			BC_Uncertainty_evaluations4, BC_Uncertainty_evaluations5 = [], [], [], [], []

		for filename in os.listdir(ExperttoTD3Hopper_evaluations_dir1):
			print(filename)
			if filename.startswith('evaluations'):
				ExperttoTD3Hopper_evaluations1=(np.load(\
					os.path.join(ExperttoTD3Hopper_evaluations_dir1,filename), allow_pickle=True))

		for filename in os.listdir(ExperttoTD3Hopper_evaluations_dir2):
			print(filename)
			if filename.startswith('evaluations'):
				ExperttoTD3Hopper_evaluations2=(np.load(\
					os.path.join(ExperttoTD3Hopper_evaluations_dir2,filename), allow_pickle=True))

				
		for filename in os.listdir(ExperttoTD3Hopper_evaluations_dir3):
			print(filename)
			if filename.startswith('evaluations'):
				ExperttoTD3Hopper_evaluations3=(np.load(\
					os.path.join(ExperttoTD3Hopper_evaluations_dir3,filename), allow_pickle=True))


		for filename in os.listdir(ExperttoTD3Hopper_evaluations_dir4):
			print(filename)
			if filename.startswith('evaluations'):
				ExperttoTD3Hopper_evaluations4=(np.load(\
					os.path.join(ExperttoTD3Hopper_evaluations_dir4,filename), allow_pickle=True))


		for filename in os.listdir(ExperttoTD3Hopper_evaluations_dir5):
			print(filename)
			if filename.startswith('evaluations'):
				ExperttoTD3Hopper_evaluations5=(np.load(\
					os.path.join(ExperttoTD3Hopper_evaluations_dir5,filename), allow_pickle=True))

		#####################################################
		#####################################################

		for filename in os.listdir(TD3Hopper_evaluations_dir1):
			print(filename)
			if filename.startswith('evaluations'):
				TD3Hopper_evaluations1=(np.load(\
					os.path.join(TD3Hopper_evaluations_dir1,filename), allow_pickle=True))

		for filename in os.listdir(TD3Hopper_evaluations_dir2):
			print(filename)
			if filename.startswith('evaluations'):
				TD3Hopper_evaluations2=(np.load(\
					os.path.join(TD3Hopper_evaluations_dir2,filename), allow_pickle=True))

				
		for filename in os.listdir(TD3Hopper_evaluations_dir3):
			print(filename)
			if filename.startswith('evaluations'):
				TD3Hopper_evaluations3=(np.load(\
					os.path.join(TD3Hopper_evaluations_dir3,filename), allow_pickle=True))


		for filename in os.listdir(TD3Hopper_evaluations_dir4):
			print(filename)
			if filename.startswith('evaluations'):
				TD3Hopper_evaluations4=(np.load(\
					os.path.join(TD3Hopper_evaluations_dir4,filename), allow_pickle=True))


		for filename in os.listdir(TD3Hopper_evaluations_dir5):
			print(filename)
			if filename.startswith('evaluations'):
				TD3Hopper_evaluations5=(np.load(\
					os.path.join(TD3Hopper_evaluations_dir5,filename), allow_pickle=True))

		#####################################################
		#####################################################

		for filename in os.listdir(BC_Uncertainty_evaluations_dir1):
			print(filename)
			if filename.startswith('evaluations'):
				BC_Uncertainty_evaluations1=(np.load(\
					os.path.join(BC_Uncertainty_evaluations_dir1,filename), allow_pickle=True))

		for filename in os.listdir(BC_Uncertainty_evaluations_dir2):
			print(filename)
			if filename.startswith('evaluations'):
				BC_Uncertainty_evaluations2=(np.load(\
					os.path.join(BC_Uncertainty_evaluations_dir2,filename), allow_pickle=True))

				
		for filename in os.listdir(BC_Uncertainty_evaluations_dir3):
			print(filename)
			if filename.startswith('evaluations'):
				BC_Uncertainty_evaluations3=(np.load(\
					os.path.join(BC_Uncertainty_evaluations_dir3,filename), allow_pickle=True))


		for filename in os.listdir(BC_Uncertainty_evaluations_dir4):
			print(filename)
			if filename.startswith('evaluations'):
				BC_Uncertainty_evaluations4=(np.load(\
					os.path.join(BC_Uncertainty_evaluations_dir4,filename), allow_pickle=True))

		for filename in os.listdir(BC_Uncertainty_evaluations_dir5):
			print(filename)
			if filename.startswith('evaluations'):
				BC_Uncertainty_evaluations5=(np.load(\
					os.path.join(BC_Uncertainty_evaluations_dir5,filename), allow_pickle=True))

		#####################################################################################
		#####################################################################################

		ExperttoTD3Hopper_eval1 = ExperttoTD3Hopper_evaluations1[:,1]
		ExperttoTD3Hopper_eval1_range = ExperttoTD3Hopper_evaluations1[:,0]

		ExperttoTD3Hopper_eval2 = ExperttoTD3Hopper_evaluations2[:,1]
		ExperttoTD3Hopper_eval2_range = ExperttoTD3Hopper_evaluations2[:,0]

		ExperttoTD3Hopper_eval3 = ExperttoTD3Hopper_evaluations3[:,1]
		ExperttoTD3Hopper_eval3_range = ExperttoTD3Hopper_evaluations3[:,0]

		ExperttoTD3Hopper_eval4 = ExperttoTD3Hopper_evaluations4[:,1]
		ExperttoTD3Hopper_eval4_range = ExperttoTD3Hopper_evaluations4[:,0]

		ExperttoTD3Hopper_eval5 = ExperttoTD3Hopper_evaluations5[:,1]
		ExperttoTD3Hopper_eval5_range = ExperttoTD3Hopper_evaluations5[:,0]

		ExperttoTD3Hopper_evals = np.array([ExperttoTD3Hopper_eval1, ExperttoTD3Hopper_eval2, ExperttoTD3Hopper_eval3, \
									ExperttoTD3Hopper_eval4, ExperttoTD3Hopper_eval5])

		ExperttoTD3Hopper_mean = np.mean(ExperttoTD3Hopper_evals,axis=0)
		ExperttoTD3Hopper_quartile1 = np.quantile(ExperttoTD3Hopper_evals, .25, interpolation='midpoint',axis=0)
		ExperttoTD3Hopper_quartile2 = np.quantile(ExperttoTD3Hopper_evals, .50, interpolation='midpoint',axis=0)
		ExperttoTD3Hopper_quartile3 = np.quantile(ExperttoTD3Hopper_evals, .75, interpolation='midpoint',axis=0)
		#####################################################################################
		#####################################################################################

		TD3Hopper_eval1 = TD3Hopper_evaluations1[:,1]
		TD3Hopper_eval1_range = TD3Hopper_evaluations1[:,0]

		TD3Hopper_eval2 = TD3Hopper_evaluations2[:,1]
		TD3Hopper_eval2_range = TD3Hopper_evaluations2[:,0]

		TD3Hopper_eval3 = TD3Hopper_evaluations3[:,1]
		TD3Hopper_eval3_range = TD3Hopper_evaluations3[:,0]

		TD3Hopper_eval4 = TD3Hopper_evaluations4[:,1]
		TD3Hopper_eval4_range = TD3Hopper_evaluations4[:,0]

		TD3Hopper_eval5 = TD3Hopper_evaluations5[:,1]
		TD3Hopper_eval5_range = TD3Hopper_evaluations5[:,0]

		TD3Hopper_evals = np.array([TD3Hopper_eval1, TD3Hopper_eval2, TD3Hopper_eval3, \
									TD3Hopper_eval4, TD3Hopper_eval5])

		TD3Hopper_mean = np.mean(TD3Hopper_evals,axis=0)
		TD3Hopper_quartile1 = np.quantile(TD3Hopper_evals, .25, interpolation='midpoint',axis=0)
		TD3Hopper_quartile2 = np.quantile(TD3Hopper_evals, .50, interpolation='midpoint',axis=0)
		TD3Hopper_quartile3 = np.quantile(TD3Hopper_evals, .75, interpolation='midpoint',axis=0)
		# ###################################################################################

		BC_Uncertainty_eval1 = BC_Uncertainty_evaluations1[:,1]
		BC_Uncertainty_eval1_range = BC_Uncertainty_evaluations1[:,0]

		BC_Uncertainty_eval2 = BC_Uncertainty_evaluations2[:,1]
		BC_Uncertainty_eval2_range = BC_Uncertainty_evaluations2[:,0]

		BC_Uncertainty_eval3 = BC_Uncertainty_evaluations3[:,1]
		BC_Uncertainty_eval3_range = BC_Uncertainty_evaluations3[:,0]

		BC_Uncertainty_eval4 = BC_Uncertainty_evaluations4[:,1]
		BC_Uncertainty_eval4_range = BC_Uncertainty_evaluations4[:,0]

		BC_Uncertainty_eval5 = BC_Uncertainty_evaluations5[:,1]
		BC_Uncertainty_eval5_range = BC_Uncertainty_evaluations5[:,0]

		BC_Uncertainty_evals = np.array([BC_Uncertainty_eval1, BC_Uncertainty_eval2, BC_Uncertainty_eval3, \
									BC_Uncertainty_eval4, BC_Uncertainty_eval5])

		BC_Uncertainty_mean = np.mean(BC_Uncertainty_evals,axis=0)
		BC_Uncertainty_quartile1 = np.quantile(BC_Uncertainty_evals, .25, interpolation='midpoint',axis=0)
		BC_Uncertainty_quartile2 = np.quantile(BC_Uncertainty_evals, .50, interpolation='midpoint',axis=0)
		BC_Uncertainty_quartile3 = np.quantile(BC_Uncertainty_evals, .75, interpolation='midpoint',axis=0)
		# ##################################################################

		plt.title('Hopper CCL-PQD vs. Warm-Start TD3 vs. TD3', fontsize=15)

		plt.xlabel("evaluations", fontsize=15)
		plt.ylabel("rewards", fontsize=15)
		
		plt.plot(ExperttoTD3Hopper_eval1_range, ExperttoTD3Hopper_quartile2, label='Warm-Start TD3', color='tab:purple')
		plt.fill_between(ExperttoTD3Hopper_eval1_range, ExperttoTD3Hopper_quartile2, ExperttoTD3Hopper_quartile1,alpha=0.3,color='tab:purple'); 
		plt.fill_between(ExperttoTD3Hopper_eval1_range, ExperttoTD3Hopper_quartile2, ExperttoTD3Hopper_quartile3,alpha=0.3,color='tab:purple'); 
		
		plt.plot(TD3Hopper_eval1_range, TD3Hopper_quartile2, label='TD3', color='tab:red')
		plt.fill_between(TD3Hopper_eval1_range, TD3Hopper_quartile2, TD3Hopper_quartile1,alpha=0.3,color='tab:red'); 
		plt.fill_between(TD3Hopper_eval1_range, TD3Hopper_quartile2, TD3Hopper_quartile3,alpha=0.3,color='tab:red'); 

		plt.plot(BC_Uncertainty_eval1_range, BC_Uncertainty_quartile2, label='CCL-PQD', color='tab:green')
		plt.fill_between(BC_Uncertainty_eval1_range, BC_Uncertainty_quartile2, BC_Uncertainty_quartile1,alpha=0.3,color='tab:green'); 
		plt.fill_between(BC_Uncertainty_eval1_range, BC_Uncertainty_quartile2, BC_Uncertainty_quartile3,alpha=0.3,color='tab:green'); 

		plt.style.use('ggplot')
		plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
		
		plt.legend(fontsize=15)
		plt.savefig('Hopper Hopper_Confidence_Scheduled_BC vs. ExperttoTD3 vs. TD3.png', bbox_inches = 'tight')
		plt.close()
		##################################################################
		run_evals = [(TD3Hopper_evals, 'Hopper', 'TD3', '0', ''), \
						(ExperttoTD3Hopper_evals, '', 'TD3', '3K', ''), \
						(BC_Uncertainty_evals, '', 'CCL-PQD', '3K', '0.0001')]
		print_metrics(run_evals)
if __name__ == "__main__":

	dg = DrawGraphs()
	dg.draw()