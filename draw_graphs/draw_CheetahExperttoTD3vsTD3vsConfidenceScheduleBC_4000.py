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

		ExperttoTD3Cheetah_evaluations_dir1 = results_dir + 'HalfCheetah-v3_results/TD3_HalfCheetah-v3_4_2021-12-24 06:58:37.6312812021-12-24 06:58:37.631397'
		ExperttoTD3Cheetah_evaluations_dir2 = results_dir + 'HalfCheetah-v3_results/TD3_HalfCheetah-v3_1_2021-12-24 00:09:17.8000022021-12-24 00:09:17.800097'
		ExperttoTD3Cheetah_evaluations_dir3 = results_dir + 'HalfCheetah-v3_results/TD3_HalfCheetah-v3_2_2021-12-24 02:38:42.1222522021-12-24 02:38:42.122389'
		ExperttoTD3Cheetah_evaluations_dir4 = results_dir + 'HalfCheetah-v3_results/TD3_HalfCheetah-v3_3_2021-12-24 04:46:30.8405012021-12-24 04:46:30.840632'
		TD3Cheetah_evaluations_dir1 = results_dir + 'HalfCheetah-v3_results/TD3_HalfCheetah-v3_0_2021-11-29 18:25:31.4546912021-11-29 18:25:31.455376'
		TD3Cheetah_evaluations_dir2 = results_dir + 'HalfCheetah-v3_results/TD3_HalfCheetah-v3_1_2021-11-29 20:40:42.3665752021-11-29 20:40:42.366904'
		TD3Cheetah_evaluations_dir3 = results_dir + 'HalfCheetah-v3_results/TD3_HalfCheetah-v3_2_2021-11-29 22:49:27.3104442021-11-29 22:49:27.310567'
		TD3Cheetah_evaluations_dir4 = results_dir + 'HalfCheetah-v3_results/TD3_HalfCheetah-v3_3_2021-11-30 01:02:23.7569392021-11-30 01:02:23.757037'
		TD3Cheetah_evaluations_dir5 = results_dir + 'HalfCheetah-v3_results/TD3_HalfCheetah-v3_4_2021-11-30 03:23:27.9658612021-11-30 03:23:27.965994'
		
		# BC_Uncertainty_evaluations_dir1 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Uncertainty_HalfCheetah-v3_0_2021-12-23 21:34:37.1370192021-12-23 21:34:37.137141'
		# BC_Uncertainty_evaluations_dir2 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Uncertainty_HalfCheetah-v3_1_2021-12-23 21:34:36.7642492021-12-23 21:34:36.764357'
		# # BC_Uncertainty_evaluations_dir2 = results_dir + 'HalfCheetah-v3_results/'
		# BC_Uncertainty_evaluations_dir3 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Uncertainty_HalfCheetah-v3_2_2021-12-23 21:34:36.5695962021-12-23 21:34:36.569704'
		# BC_Uncertainty_evaluations_dir4 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Uncertainty_HalfCheetah-v3_3_2021-12-23 21:34:37.5391022021-12-23 21:34:37.539207'
				
		BC_Uncertainty_evaluations_dir1 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_0_2022-01-09 17:05:52.4804842022-01-09 17:05:52.480589'
		BC_Uncertainty_evaluations_dir2 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_1_2022-01-09 19:30:13.6972252022-01-09 19:30:13.697332'
		BC_Uncertainty_evaluations_dir3 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_2_2022-01-09 22:32:47.3887652022-01-09 22:32:47.388906'
		BC_Uncertainty_evaluations_dir4 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_3_2022-01-10 01:33:13.4627242022-01-10 01:33:13.462879'
		BC_Uncertainty_evaluations_dir5 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_4_2022-01-10 05:14:21.6788572022-01-10 05:14:21.679020'
		
		###########################

		ExperttoTD3Cheetah_evaluations1, ExperttoTD3Cheetah_evaluations2, ExperttoTD3Cheetah_evaluations3,\
			ExperttoTD3Cheetah_evaluations4 = [], [], [], []

		TD3Cheetah_evaluations1, TD3Cheetah_evaluations2, TD3Cheetah_evaluations3,\
			TD3Cheetah_evaluations4, TD3Cheetah_evaluations5 = [], [], [], [], []

		BC_Uncertainty_evaluations1, BC_Uncertainty_evaluations2, BC_Uncertainty_evaluations3,\
			BC_Uncertainty_evaluations4, BC_Uncertainty_evaluations5 = [], [], [], [], []

		for filename in os.listdir(ExperttoTD3Cheetah_evaluations_dir1):
			print(filename)
			if filename.startswith('evaluations'):
				ExperttoTD3Cheetah_evaluations1=(np.load(\
					os.path.join(ExperttoTD3Cheetah_evaluations_dir1,filename), allow_pickle=True))

		for filename in os.listdir(ExperttoTD3Cheetah_evaluations_dir2):
			print(filename)
			if filename.startswith('evaluations'):
				ExperttoTD3Cheetah_evaluations2=(np.load(\
					os.path.join(ExperttoTD3Cheetah_evaluations_dir2,filename), allow_pickle=True))

				
		for filename in os.listdir(ExperttoTD3Cheetah_evaluations_dir3):
			print(filename)
			if filename.startswith('evaluations'):
				ExperttoTD3Cheetah_evaluations3=(np.load(\
					os.path.join(ExperttoTD3Cheetah_evaluations_dir3,filename), allow_pickle=True))


		for filename in os.listdir(ExperttoTD3Cheetah_evaluations_dir4):
			print(filename)
			if filename.startswith('evaluations'):
				ExperttoTD3Cheetah_evaluations4=(np.load(\
					os.path.join(ExperttoTD3Cheetah_evaluations_dir4,filename), allow_pickle=True))

		#####################################################
		#####################################################

		for filename in os.listdir(TD3Cheetah_evaluations_dir1):
			print(filename)
			if filename.startswith('evaluations'):
				TD3Cheetah_evaluations1=(np.load(\
					os.path.join(TD3Cheetah_evaluations_dir1,filename), allow_pickle=True))

		for filename in os.listdir(TD3Cheetah_evaluations_dir2):
			print(filename)
			if filename.startswith('evaluations'):
				TD3Cheetah_evaluations2=(np.load(\
					os.path.join(TD3Cheetah_evaluations_dir2,filename), allow_pickle=True))

				
		for filename in os.listdir(TD3Cheetah_evaluations_dir3):
			print(filename)
			if filename.startswith('evaluations'):
				TD3Cheetah_evaluations3=(np.load(\
					os.path.join(TD3Cheetah_evaluations_dir3,filename), allow_pickle=True))


		for filename in os.listdir(TD3Cheetah_evaluations_dir4):
			print(filename)
			if filename.startswith('evaluations'):
				TD3Cheetah_evaluations4=(np.load(\
					os.path.join(TD3Cheetah_evaluations_dir4,filename), allow_pickle=True))


		for filename in os.listdir(TD3Cheetah_evaluations_dir5):
			print(filename)
			if filename.startswith('evaluations'):
				TD3Cheetah_evaluations5=(np.load(\
					os.path.join(TD3Cheetah_evaluations_dir5,filename), allow_pickle=True))

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

		ExperttoTD3Cheetah_eval1 = ExperttoTD3Cheetah_evaluations1[:,1]
		ExperttoTD3Cheetah_eval1_range = ExperttoTD3Cheetah_evaluations1[:,0]

		ExperttoTD3Cheetah_eval2 = ExperttoTD3Cheetah_evaluations2[:,1]
		ExperttoTD3Cheetah_eval2_range = ExperttoTD3Cheetah_evaluations2[:,0]

		ExperttoTD3Cheetah_eval3 = ExperttoTD3Cheetah_evaluations3[:,1]
		ExperttoTD3Cheetah_eval3_range = ExperttoTD3Cheetah_evaluations3[:,0]

		ExperttoTD3Cheetah_eval4 = ExperttoTD3Cheetah_evaluations4[:,1]
		ExperttoTD3Cheetah_eval4_range = ExperttoTD3Cheetah_evaluations4[:,0]

		ExperttoTD3Cheetah_evals = np.array([ExperttoTD3Cheetah_eval1, ExperttoTD3Cheetah_eval2, ExperttoTD3Cheetah_eval3, \
									ExperttoTD3Cheetah_eval4])

		ExperttoTD3Cheetah_mean = np.mean(ExperttoTD3Cheetah_evals,axis=0)
		ExperttoTD3Cheetah_quartile1 = np.quantile(ExperttoTD3Cheetah_evals, .25, interpolation='midpoint',axis=0)
		ExperttoTD3Cheetah_quartile2 = np.quantile(ExperttoTD3Cheetah_evals, .50, interpolation='midpoint',axis=0)
		ExperttoTD3Cheetah_quartile3 = np.quantile(ExperttoTD3Cheetah_evals, .75, interpolation='midpoint',axis=0)
		#####################################################################################
		#####################################################################################

		TD3Cheetah_eval1 = TD3Cheetah_evaluations1[:,1]
		TD3Cheetah_eval1_range = TD3Cheetah_evaluations1[:,0]

		TD3Cheetah_eval2 = TD3Cheetah_evaluations2[:,1]
		TD3Cheetah_eval2_range = TD3Cheetah_evaluations2[:,0]

		TD3Cheetah_eval3 = TD3Cheetah_evaluations3[:,1]
		TD3Cheetah_eval3_range = TD3Cheetah_evaluations3[:,0]

		TD3Cheetah_eval4 = TD3Cheetah_evaluations4[:,1]
		TD3Cheetah_eval4_range = TD3Cheetah_evaluations4[:,0]

		TD3Cheetah_eval5 = TD3Cheetah_evaluations5[:,1]
		TD3Cheetah_eval5_range = TD3Cheetah_evaluations5[:,0]

		TD3Cheetah_evals = np.array([TD3Cheetah_eval1, TD3Cheetah_eval2, TD3Cheetah_eval3, \
									TD3Cheetah_eval4, TD3Cheetah_eval5])

		TD3Cheetah_mean = np.mean(TD3Cheetah_evals,axis=0)
		TD3Cheetah_quartile1 = np.quantile(TD3Cheetah_evals, .25, interpolation='midpoint',axis=0)
		TD3Cheetah_quartile2 = np.quantile(TD3Cheetah_evals, .50, interpolation='midpoint',axis=0)
		TD3Cheetah_quartile3 = np.quantile(TD3Cheetah_evals, .75, interpolation='midpoint',axis=0)
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

		plt.title('HalfCheetah 4K Expert', fontsize=25)

		plt.xlabel("evaluations", fontsize=18)
		plt.ylabel("rewards", fontsize=18)
		
		plt.plot(ExperttoTD3Cheetah_eval1_range, ExperttoTD3Cheetah_quartile2, label='Warm-Start TD3', color='tab:purple')
		plt.fill_between(ExperttoTD3Cheetah_eval1_range, ExperttoTD3Cheetah_quartile2, ExperttoTD3Cheetah_quartile1,alpha=0.3,color='tab:purple'); 
		plt.fill_between(ExperttoTD3Cheetah_eval1_range, ExperttoTD3Cheetah_quartile2, ExperttoTD3Cheetah_quartile3,alpha=0.3,color='tab:purple'); 
		
		plt.plot(TD3Cheetah_eval1_range, TD3Cheetah_quartile2, label='TD3', color='tab:red')
		plt.fill_between(TD3Cheetah_eval1_range, TD3Cheetah_quartile2, TD3Cheetah_quartile1,alpha=0.3,color='tab:red'); 
		plt.fill_between(TD3Cheetah_eval1_range, TD3Cheetah_quartile2, TD3Cheetah_quartile3,alpha=0.3,color='tab:red'); 

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
		plt.savefig('Cheetah Cheetah_Confidence_Scheduled_BC vs. ExperttoTD3 vs. TD3 4000.png', bbox_inches = 'tight')
		plt.close()
		##################################################################

		run_evals = [(TD3Cheetah_evals, 'Half', 'TD3', '0', ''), \
						(ExperttoTD3Cheetah_evals, 'Cheetah', 'TD3', '4K', ''), \
						(BC_Uncertainty_evals, '', 'CCL-PQD', '4K', '0.01')]

		print_metrics(run_evals)


if __name__ == "__main__":

	dg = DrawGraphs()
	dg.draw()