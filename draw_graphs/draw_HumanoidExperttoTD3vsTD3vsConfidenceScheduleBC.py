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

		ExperttoTD3Humanoid_evaluations_dir1 = results_dir + 'Humanoid-v3_results/TD3_Humanoid-v3_0_2021-12-27 15:35:01.9113032021-12-27 15:35:01.911673'
		ExperttoTD3Humanoid_evaluations_dir2 = results_dir + 'Humanoid-v3_results/TD3_Humanoid-v3_1_2021-12-27 18:42:37.0999932021-12-27 18:42:37.100090'
		ExperttoTD3Humanoid_evaluations_dir3 = results_dir + 'Humanoid-v3_results/TD3_Humanoid-v3_2_2021-12-27 22:47:38.5108682021-12-27 22:47:38.510982'
		ExperttoTD3Humanoid_evaluations_dir4 = results_dir + 'Humanoid-v3_results/TD3_Humanoid-v3_3_2021-12-28 02:05:38.3853732021-12-28 02:05:38.385455'
		ExperttoTD3Humanoid_evaluations_dir5 = results_dir + 'Humanoid-v3_results/TD3_Humanoid-v3_4_2021-12-28 04:51:37.3841332021-12-28 04:51:37.384242'
		TD3Humanoid_evaluations_dir1 = results_dir + 'Humanoid-v3_results/TD3_Humanoid-v3_1_2021-12-28 19:09:38.3064662021-12-28 19:09:38.306558'
		TD3Humanoid_evaluations_dir2 = results_dir + 'Humanoid-v3_results/TD3_Humanoid-v3_2_2021-12-29 01:52:21.0897492021-12-29 01:52:21.089862'
		TD3Humanoid_evaluations_dir3 = results_dir + 'Humanoid-v3_results/TD3_Humanoid-v3_3_2021-12-29 07:49:12.7217772021-12-29 07:49:12.721891'
		TD3Humanoid_evaluations_dir4 = results_dir + 'Humanoid-v3_results/TD3_Humanoid-v3_4_2021-12-29 13:06:57.4555452021-12-29 13:06:57.455637'
		TD3Humanoid_evaluations_dir5 = results_dir + 'Humanoid-v3_results/TD3_Humanoid-v3_0_2021-12-29 18:27:14.3973992021-12-29 18:27:14.397504'
		
		# BC_Uncertainty_evaluations_dir1 = results_dir + 'Humanoid-v3_results/TD3_BC_Uncertainty_Humanoid-v3_0_2021-12-29 14:50:05.8582982021-12-29 14:50:05.858638'
		# BC_Uncertainty_evaluations_dir2 = results_dir + 'Humanoid-v3_results/TD3_BC_Uncertainty_Humanoid-v3_1_2021-12-29 21:09:25.2635322021-12-29 21:09:25.263666'
		# BC_Uncertainty_evaluations_dir3 = results_dir + 'Humanoid-v3_results/TD3_BC_Uncertainty_Humanoid-v3_2_2021-12-30 02:11:57.6311832021-12-30 02:11:57.631262'
		# BC_Uncertainty_evaluations_dir4 = results_dir + 'Humanoid-v3_results/TD3_BC_Uncertainty_Humanoid-v3_3_2021-12-30 05:00:53.9762572021-12-30 05:00:53.976349'
		# BC_Uncertainty_evaluations_dir5 = results_dir + 'Humanoid-v3_results/TD3_BC_Uncertainty_Humanoid-v3_4_2021-12-30 08:01:25.8859882021-12-30 08:01:25.886079'
			
		# #0.0001
		BC_Uncertainty_evaluations_dir1 = results_dir + 'Humanoid-v3_results/TD3CP_Humanoid-v3_0_2022-01-09 17:05:52.0379792022-01-09 17:05:52.038345'
		BC_Uncertainty_evaluations_dir2 = results_dir + 'Humanoid-v3_results/TD3CP_Humanoid-v3_1_2022-01-09 19:30:13.8989892022-01-09 19:30:13.899110'
		BC_Uncertainty_evaluations_dir3 = results_dir + 'Humanoid-v3_results/TD3CP_Humanoid-v3_2_2022-01-09 22:32:47.0029892022-01-09 22:32:47.003103'
		BC_Uncertainty_evaluations_dir4 = results_dir + 'Humanoid-v3_results/TD3CP_Humanoid-v3_3_2022-01-10 01:33:12.9980992022-01-10 01:33:12.998217'
		BC_Uncertainty_evaluations_dir5 = results_dir + 'Humanoid-v3_results/TD3CP_Humanoid-v3_4_2022-01-10 05:14:26.0875472022-01-10 05:14:26.087744'
		
		#0.001
		# BC_Uncertainty_evaluations_dir1 = results_dir + 'Humanoid-v3_results/TD3CCL_PQD_Humanoid-v3_0_2022-01-27 21:34:09.7733932022-01-27 21:34:09.773497'
		# BC_Uncertainty_evaluations_dir2 = results_dir + 'Humanoid-v3_results/TD3CCL_PQD_Humanoid-v3_0_2022-01-27 21:34:09.7733932022-01-27 21:34:09.773497'
		# BC_Uncertainty_evaluations_dir3 = results_dir + 'Humanoid-v3_results/TD3CCL_PQD_Humanoid-v3_0_2022-01-27 21:34:09.7733932022-01-27 21:34:09.773497'
		# BC_Uncertainty_evaluations_dir4 = results_dir + 'Humanoid-v3_results/TD3CCL_PQD_Humanoid-v3_0_2022-01-27 21:34:09.7733932022-01-27 21:34:09.773497'
		# BC_Uncertainty_evaluations_dir5 = results_dir + 'Humanoid-v3_results/TD3CCL_PQD_Humanoid-v3_0_2022-01-27 21:34:09.7733932022-01-27 21:34:09.773497'
	
		# #0.01
		# BC_Uncertainty_evaluations_dir1 = results_dir + 'Humanoid-v3_results/TD3CCL_PQD_Humanoid-v3_0_2022-01-27 21:34:05.3702312022-01-27 21:34:05.370324'
		# BC_Uncertainty_evaluations_dir2 = results_dir + 'Humanoid-v3_results/TD3CCL_PQD_Humanoid-v3_0_2022-01-27 21:34:05.3702312022-01-27 21:34:05.370324'
		# BC_Uncertainty_evaluations_dir3 = results_dir + 'Humanoid-v3_results/TD3CCL_PQD_Humanoid-v3_0_2022-01-27 21:34:05.3702312022-01-27 21:34:05.370324'
		# BC_Uncertainty_evaluations_dir4 = results_dir + 'Humanoid-v3_results/TD3CCL_PQD_Humanoid-v3_0_2022-01-27 21:34:05.3702312022-01-27 21:34:05.370324'
		# BC_Uncertainty_evaluations_dir5 = results_dir + 'Humanoid-v3_results/TD3CCL_PQD_Humanoid-v3_0_2022-01-27 21:34:05.3702312022-01-27 21:34:05.370324'
		
		###########################

		ExperttoTD3Humanoid_evaluations1, ExperttoTD3Humanoid_evaluations2, ExperttoTD3Humanoid_evaluations3,\
			ExperttoTD3Humanoid_evaluations4, ExperttoTD3Humanoid_evaluations5 = [], [], [], [], []

		TD3Humanoid_evaluations1, TD3Humanoid_evaluations2, TD3Humanoid_evaluations3,\
			TD3Humanoid_evaluations4, TD3Humanoid_evaluations5 = [], [], [], [], []

		BC_Uncertainty_evaluations1, BC_Uncertainty_evaluations2, BC_Uncertainty_evaluations3,\
			BC_Uncertainty_evaluations4, BC_Uncertainty_evaluations5 = [], [], [], [], []

		for filename in os.listdir(ExperttoTD3Humanoid_evaluations_dir1):
			print(filename)
			if filename.startswith('evaluations'):
				ExperttoTD3Humanoid_evaluations1=(np.load(\
					os.path.join(ExperttoTD3Humanoid_evaluations_dir1,filename), allow_pickle=True))

		for filename in os.listdir(ExperttoTD3Humanoid_evaluations_dir2):
			print(filename)
			if filename.startswith('evaluations'):
				ExperttoTD3Humanoid_evaluations2=(np.load(\
					os.path.join(ExperttoTD3Humanoid_evaluations_dir2,filename), allow_pickle=True))

				
		for filename in os.listdir(ExperttoTD3Humanoid_evaluations_dir3):
			print(filename)
			if filename.startswith('evaluations'):
				ExperttoTD3Humanoid_evaluations3=(np.load(\
					os.path.join(ExperttoTD3Humanoid_evaluations_dir3,filename), allow_pickle=True))


		for filename in os.listdir(ExperttoTD3Humanoid_evaluations_dir4):
			print(filename)
			if filename.startswith('evaluations'):
				ExperttoTD3Humanoid_evaluations4=(np.load(\
					os.path.join(ExperttoTD3Humanoid_evaluations_dir4,filename), allow_pickle=True))


		for filename in os.listdir(ExperttoTD3Humanoid_evaluations_dir5):
			print(filename)
			if filename.startswith('evaluations'):
				ExperttoTD3Humanoid_evaluations5=(np.load(\
					os.path.join(ExperttoTD3Humanoid_evaluations_dir5,filename), allow_pickle=True))

		#####################################################
		#####################################################

		for filename in os.listdir(TD3Humanoid_evaluations_dir1):
			print(filename)
			if filename.startswith('evaluations'):
				TD3Humanoid_evaluations1=(np.load(\
					os.path.join(TD3Humanoid_evaluations_dir1,filename), allow_pickle=True))

		for filename in os.listdir(TD3Humanoid_evaluations_dir2):
			print(filename)
			if filename.startswith('evaluations'):
				TD3Humanoid_evaluations2=(np.load(\
					os.path.join(TD3Humanoid_evaluations_dir2,filename), allow_pickle=True))

				
		for filename in os.listdir(TD3Humanoid_evaluations_dir3):
			print(filename)
			if filename.startswith('evaluations'):
				TD3Humanoid_evaluations3=(np.load(\
					os.path.join(TD3Humanoid_evaluations_dir3,filename), allow_pickle=True))


		for filename in os.listdir(TD3Humanoid_evaluations_dir4):
			print(filename)
			if filename.startswith('evaluations'):
				TD3Humanoid_evaluations4=(np.load(\
					os.path.join(TD3Humanoid_evaluations_dir4,filename), allow_pickle=True))


		for filename in os.listdir(TD3Humanoid_evaluations_dir5):
			print(filename)
			if filename.startswith('evaluations'):
				TD3Humanoid_evaluations5=(np.load(\
					os.path.join(TD3Humanoid_evaluations_dir5,filename), allow_pickle=True))

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

		ExperttoTD3Humanoid_eval1 = ExperttoTD3Humanoid_evaluations1[:,1]
		ExperttoTD3Humanoid_eval1_range = ExperttoTD3Humanoid_evaluations1[:,0]

		ExperttoTD3Humanoid_eval2 = ExperttoTD3Humanoid_evaluations2[:,1]
		ExperttoTD3Humanoid_eval2_range = ExperttoTD3Humanoid_evaluations2[:,0]

		ExperttoTD3Humanoid_eval3 = ExperttoTD3Humanoid_evaluations3[:,1]
		ExperttoTD3Humanoid_eval3_range = ExperttoTD3Humanoid_evaluations3[:,0]

		ExperttoTD3Humanoid_eval4 = ExperttoTD3Humanoid_evaluations4[:,1]
		ExperttoTD3Humanoid_eval4_range = ExperttoTD3Humanoid_evaluations4[:,0]

		ExperttoTD3Humanoid_eval5 = ExperttoTD3Humanoid_evaluations5[:,1]
		ExperttoTD3Humanoid_eval5_range = ExperttoTD3Humanoid_evaluations5[:,0]

		ExperttoTD3Humanoid_evals = np.array([ExperttoTD3Humanoid_eval1, ExperttoTD3Humanoid_eval2, ExperttoTD3Humanoid_eval3, \
									ExperttoTD3Humanoid_eval4, ExperttoTD3Humanoid_eval5])

		ExperttoTD3Humanoid_mean = np.mean(ExperttoTD3Humanoid_evals,axis=0)
		ExperttoTD3Humanoid_quartile1 = np.quantile(ExperttoTD3Humanoid_evals, .25, interpolation='midpoint',axis=0)
		ExperttoTD3Humanoid_quartile2 = np.quantile(ExperttoTD3Humanoid_evals, .50, interpolation='midpoint',axis=0)
		ExperttoTD3Humanoid_quartile3 = np.quantile(ExperttoTD3Humanoid_evals, .75, interpolation='midpoint',axis=0)

		#####################################################################################
		#####################################################################################

		TD3Humanoid_eval1 = TD3Humanoid_evaluations1[:,1]
		TD3Humanoid_eval1_range = TD3Humanoid_evaluations1[:,0]

		TD3Humanoid_eval2 = TD3Humanoid_evaluations2[:,1]
		TD3Humanoid_eval2_range = TD3Humanoid_evaluations2[:,0]

		TD3Humanoid_eval3 = TD3Humanoid_evaluations3[:,1]
		TD3Humanoid_eval3_range = TD3Humanoid_evaluations3[:,0]

		TD3Humanoid_eval4 = TD3Humanoid_evaluations4[:,1]
		TD3Humanoid_eval4_range = TD3Humanoid_evaluations4[:,0]

		TD3Humanoid_eval5 = TD3Humanoid_evaluations5[:,1]
		TD3Humanoid_eval5_range = TD3Humanoid_evaluations5[:,0]

		TD3Humanoid_evals = np.array([TD3Humanoid_eval1, TD3Humanoid_eval2, TD3Humanoid_eval3, \
									TD3Humanoid_eval4, TD3Humanoid_eval5])

		TD3Humanoid_mean = np.mean(TD3Humanoid_evals,axis=0)
		TD3Humanoid_quartile1 = np.quantile(TD3Humanoid_evals, .25, interpolation='midpoint',axis=0)
		TD3Humanoid_quartile2 = np.quantile(TD3Humanoid_evals, .50, interpolation='midpoint',axis=0)
		TD3Humanoid_quartile3 = np.quantile(TD3Humanoid_evals, .75, interpolation='midpoint',axis=0)

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

		plt.title('Humanoid', fontsize=25)

		plt.xlabel("evaluations", fontsize=18)
		plt.ylabel("rewards", fontsize=18)
		
		plt.plot(ExperttoTD3Humanoid_eval1_range, ExperttoTD3Humanoid_quartile2, label='Warm-Start TD3', color='tab:purple')
		plt.fill_between(ExperttoTD3Humanoid_eval1_range, ExperttoTD3Humanoid_quartile2, ExperttoTD3Humanoid_quartile1,alpha=0.3,color='tab:purple'); 
		plt.fill_between(ExperttoTD3Humanoid_eval1_range, ExperttoTD3Humanoid_quartile2, ExperttoTD3Humanoid_quartile3,alpha=0.3,color='tab:purple'); 
		
		plt.plot(TD3Humanoid_eval1_range, TD3Humanoid_quartile2, label='TD3', color='tab:red')
		plt.fill_between(TD3Humanoid_eval1_range, TD3Humanoid_quartile2, TD3Humanoid_quartile1,alpha=0.3,color='tab:red'); 
		plt.fill_between(TD3Humanoid_eval1_range, TD3Humanoid_quartile2, TD3Humanoid_quartile3,alpha=0.3,color='tab:red'); 

		plt.plot(BC_Uncertainty_eval1_range, BC_Uncertainty_quartile2, label='CCL-PQD', color='tab:green')
		plt.fill_between(BC_Uncertainty_eval1_range, BC_Uncertainty_quartile2, BC_Uncertainty_quartile1,alpha=0.3,color='tab:green'); 
		plt.fill_between(BC_Uncertainty_eval1_range, BC_Uncertainty_quartile2, BC_Uncertainty_quartile3,alpha=0.3,color='tab:green'); 

		plt.style.use('ggplot')
		plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
		plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))	
		ax = plt.gca()
		ax.xaxis.get_offset_text().set_fontsize(16)
		ax.yaxis.get_offset_text().set_fontsize(16)
		ax.yaxis.get_offset_text().set_x(-.1)
		
		plt.xticks(fontsize=18)
		plt.yticks(fontsize=18)
		
		plt.legend(fontsize=18)
		plt.savefig('Humanoid Humanoid_Confidence_Scheduled_BC vs. ExperttoTD3 vs. TD3.png', bbox_inches = 'tight')
		plt.close()
		##################################################################
		run_evals = [(TD3Humanoid_evals, 'Humanoid', 'TD3', '0', ''), \
						(ExperttoTD3Humanoid_evals, '', 'TD3', '2.5K', ''), \
						(BC_Uncertainty_evals, '', 'CCL-PQD', '2.5K', '0.0001')]

		print_metrics(run_evals)

if __name__ == "__main__":

	dg = DrawGraphs()
	dg.draw()