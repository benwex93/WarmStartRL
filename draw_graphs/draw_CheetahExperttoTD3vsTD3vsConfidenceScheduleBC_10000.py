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

		ExperttoTD3Cheetah_evaluations_dir1 = results_dir + 'HalfCheetah-v3_results/TD3_HalfCheetah-v3_0_2021-11-29 23:21:26.3488922021-11-29 23:21:26.348994'
		ExperttoTD3Cheetah_evaluations_dir2 = results_dir + 'HalfCheetah-v3_results/TD3_HalfCheetah-v3_1_2021-11-30 01:43:50.4262522021-11-30 01:43:50.426349'
		ExperttoTD3Cheetah_evaluations_dir3 = results_dir + 'HalfCheetah-v3_results/TD3_HalfCheetah-v3_2_2021-11-30 04:13:18.8107842021-11-30 04:13:18.811053'
		ExperttoTD3Cheetah_evaluations_dir4 = results_dir + 'HalfCheetah-v3_results/TD3_HalfCheetah-v3_3_2021-11-30 06:37:03.3265092021-11-30 06:37:03.326855'
		ExperttoTD3Cheetah_evaluations_dir5 = results_dir + 'HalfCheetah-v3_results/TD3_HalfCheetah-v3_4_2021-11-30 09:04:34.2556072021-11-30 09:04:34.255990'
		TD3Cheetah_evaluations_dir1 = results_dir + 'HalfCheetah-v3_results/TD3_HalfCheetah-v3_0_2021-11-29 18:25:31.4546912021-11-29 18:25:31.455376'
		TD3Cheetah_evaluations_dir2 = results_dir + 'HalfCheetah-v3_results/TD3_HalfCheetah-v3_1_2021-11-29 20:40:42.3665752021-11-29 20:40:42.366904'
		TD3Cheetah_evaluations_dir3 = results_dir + 'HalfCheetah-v3_results/TD3_HalfCheetah-v3_2_2021-11-29 22:49:27.3104442021-11-29 22:49:27.310567'
		TD3Cheetah_evaluations_dir4 = results_dir + 'HalfCheetah-v3_results/TD3_HalfCheetah-v3_3_2021-11-30 01:02:23.7569392021-11-30 01:02:23.757037'
		TD3Cheetah_evaluations_dir5 = results_dir + 'HalfCheetah-v3_results/TD3_HalfCheetah-v3_4_2021-11-30 03:23:27.9658612021-11-30 03:23:27.965994'
		
		# BC_Uncertainty_evaluations_dir1 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Uncertainty_HalfCheetah-v3_0_2021-12-27 15:47:08.9061192021-12-27 15:47:08.906232'
		# BC_Uncertainty_evaluations_dir2 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Uncertainty_HalfCheetah-v3_1_2021-12-27 15:47:08.7120392021-12-27 15:47:08.712158'
		# BC_Uncertainty_evaluations_dir3 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Uncertainty_HalfCheetah-v3_2_2021-12-27 15:47:09.0895232021-12-27 15:47:09.089644'
		# BC_Uncertainty_evaluations_dir4 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Uncertainty_HalfCheetah-v3_3_2021-12-27 15:47:04.3335282021-12-27 15:47:04.334018'
		
		BC_Uncertainty_evaluations_dir1 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_0_2022-01-09 17:05:47.8701432022-01-09 17:05:47.870514'
		BC_Uncertainty_evaluations_dir2 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_1_2022-01-09 19:30:13.5075892022-01-09 19:30:13.507738'
		BC_Uncertainty_evaluations_dir3 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_2_2022-01-09 22:32:42.5473522022-01-09 22:32:42.547460'
		BC_Uncertainty_evaluations_dir4 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_3_2022-01-10 01:33:13.2583532022-01-10 01:33:13.258533'
		BC_Uncertainty_evaluations_dir5 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_4_2022-01-10 05:14:26.4863192022-01-10 05:14:26.486556'
		
		###########################

		ExperttoTD3Cheetah_evaluations1, ExperttoTD3Cheetah_evaluations2, ExperttoTD3Cheetah_evaluations3,\
			ExperttoTD3Cheetah_evaluations4, ExperttoTD3Cheetah_evaluations5 = [], [], [], [], []

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


		for filename in os.listdir(ExperttoTD3Cheetah_evaluations_dir5):
			print(filename)
			if filename.startswith('evaluations'):
				ExperttoTD3Cheetah_evaluations5=(np.load(\
					os.path.join(ExperttoTD3Cheetah_evaluations_dir5,filename), allow_pickle=True))

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

		ExperttoTD3Cheetah_eval5 = ExperttoTD3Cheetah_evaluations5[:,1]
		ExperttoTD3Cheetah_eval5_range = ExperttoTD3Cheetah_evaluations5[:,0]

		ExperttoTD3Cheetah_evals = np.array([ExperttoTD3Cheetah_eval1, ExperttoTD3Cheetah_eval2, ExperttoTD3Cheetah_eval3, \
									ExperttoTD3Cheetah_eval4, ExperttoTD3Cheetah_eval5])

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

		plt.title('HalfCheetah 10K Expert', fontsize=25)

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
		plt.savefig('Cheetah Cheetah_Confidence_Scheduled_BC vs. ExperttoTD3 vs. TD3 10000.png', bbox_inches = 'tight')
		plt.close()
		##################################################################
		run_evals = [(TD3Cheetah_evals, 'Half', 'TD3', '0', ''), \
						(ExperttoTD3Cheetah_evals, 'Cheetah', 'TD3', '10K', ''), \
						(BC_Uncertainty_evals, '', 'CCL-PQD', '10K', '0.0001')]

		print_metrics(run_evals)

if __name__ == "__main__":

	dg = DrawGraphs()
	dg.draw()