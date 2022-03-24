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

		ExperttoTD3Fetch_evaluations_dir1 = results_dir + 'FetchPush-v1_results/TD3_FetchPush-v1_0_2022-02-15 22:03:53.3557772022-02-15 22:03:53.355863'
		ExperttoTD3Fetch_evaluations_dir2 = results_dir + 'FetchPush-v1_results/TD3_FetchPush-v1_1_2022-02-16 01:09:08.5588012022-02-16 01:09:08.558902'
		ExperttoTD3Fetch_evaluations_dir3 = results_dir + 'FetchPush-v1_results/TD3_FetchPush-v1_2_2022-02-16 04:20:47.6671742022-02-16 04:20:47.667272'
		ExperttoTD3Fetch_evaluations_dir4 = results_dir + 'FetchPush-v1_results/TD3_FetchPush-v1_3_2022-02-16 07:26:59.2407832022-02-16 07:26:59.240877'
		ExperttoTD3Fetch_evaluations_dir5 = results_dir + 'FetchPush-v1_results/TD3_FetchPush-v1_4_2022-02-16 10:23:05.6956892022-02-16 10:23:05.695777'
		
		TD3Fetch_evaluations_dir1 = results_dir + 'FetchPush-v1_results/TD3_FetchPush-v1_0_2022-02-15 21:55:44.4476832022-02-15 21:55:44.447778'
		TD3Fetch_evaluations_dir2 = results_dir + 'FetchPush-v1_results/TD3_FetchPush-v1_1_2022-02-16 00:42:08.3953142022-02-16 00:42:08.395419'
		TD3Fetch_evaluations_dir3 = results_dir + 'FetchPush-v1_results/TD3_FetchPush-v1_2_2022-02-16 03:35:53.8775342022-02-16 03:35:53.877618'
		TD3Fetch_evaluations_dir4 = results_dir + 'FetchPush-v1_results/TD3_FetchPush-v1_3_2022-02-16 06:18:33.3301112022-02-16 06:18:33.330212'
		TD3Fetch_evaluations_dir5 = results_dir + 'FetchPush-v1_results/TD3_FetchPush-v1_4_2022-02-16 09:14:55.6942382022-02-16 09:14:55.694330'
		
		alpha=''
		# alpha=0.01
		BC_Uncertainty_evaluations_dir1 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_0_2022-02-15 22:02:25.9402272022-02-15 22:02:25.940467'
		BC_Uncertainty_evaluations_dir2 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_1_2022-02-16 01:23:50.4597002022-02-16 01:23:50.459793'
		BC_Uncertainty_evaluations_dir3 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_2_2022-02-16 04:46:22.3117432022-02-16 04:46:22.311840'
		BC_Uncertainty_evaluations_dir4 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_3_2022-02-16 08:04:07.4408542022-02-16 08:04:07.441288'
		BC_Uncertainty_evaluations_dir5 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_4_2022-02-16 11:26:37.2449252022-02-16 11:26:37.245029'		
		
		# alpha=0.001
		# BC_Uncertainty_evaluations_dir1 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_0_2022-02-15 22:02:29.9934402022-02-15 22:02:29.993525'
		# BC_Uncertainty_evaluations_dir2 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_1_2022-02-16 01:23:46.3490712022-02-16 01:23:46.349185'
		# BC_Uncertainty_evaluations_dir3 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_2_2022-02-16 04:46:18.1847532022-02-16 04:46:18.184888'
		# BC_Uncertainty_evaluations_dir4 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_3_2022-02-16 08:04:11.3784132022-02-16 08:04:11.378517'
		# BC_Uncertainty_evaluations_dir5 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_4_2022-02-16 11:26:32.9627592022-02-16 11:26:32.963018'

		# alpha=0.0001
		# BC_Uncertainty_evaluations_dir1 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_0_2022-02-15 22:02:30.1508222022-02-15 22:02:30.150915'
		# BC_Uncertainty_evaluations_dir2 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_1_2022-02-16 01:23:50.6473152022-02-16 01:23:50.647408'
		# BC_Uncertainty_evaluations_dir3 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_2_2022-02-16 04:46:22.4742092022-02-16 04:46:22.474305'
		# BC_Uncertainty_evaluations_dir4 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_3_2022-02-16 08:04:11.5692702022-02-16 08:04:11.569370'
		# BC_Uncertainty_evaluations_dir5 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_4_2022-02-16 11:26:37.0066002022-02-16 11:26:37.006981'
		
		###########################

		ExperttoTD3Fetch_evaluations1, ExperttoTD3Fetch_evaluations2, ExperttoTD3Fetch_evaluations3,\
			ExperttoTD3Fetch_evaluations4, ExperttoTD3Fetch_evaluations5 = [], [], [], [], []

		TD3Fetch_evaluations1, TD3Fetch_evaluations2, TD3Fetch_evaluations3,\
			TD3Fetch_evaluations4, TD3Fetch_evaluations5 = [], [], [], [], []

		BC_Uncertainty_evaluations1, BC_Uncertainty_evaluations2, BC_Uncertainty_evaluations3,\
			BC_Uncertainty_evaluations4, BC_Uncertainty_evaluations5 = [], [], [], [], []

		for filename in os.listdir(ExperttoTD3Fetch_evaluations_dir1):
			print(filename)
			if filename.startswith('evaluations'):
				ExperttoTD3Fetch_evaluations1=(np.load(\
					os.path.join(ExperttoTD3Fetch_evaluations_dir1,filename), allow_pickle=True))

		for filename in os.listdir(ExperttoTD3Fetch_evaluations_dir2):
			print(filename)
			if filename.startswith('evaluations'):
				ExperttoTD3Fetch_evaluations2=(np.load(\
					os.path.join(ExperttoTD3Fetch_evaluations_dir2,filename), allow_pickle=True))

				
		for filename in os.listdir(ExperttoTD3Fetch_evaluations_dir3):
			print(filename)
			if filename.startswith('evaluations'):
				ExperttoTD3Fetch_evaluations3=(np.load(\
					os.path.join(ExperttoTD3Fetch_evaluations_dir3,filename), allow_pickle=True))


		for filename in os.listdir(ExperttoTD3Fetch_evaluations_dir4):
			print(filename)
			if filename.startswith('evaluations'):
				ExperttoTD3Fetch_evaluations4=(np.load(\
					os.path.join(ExperttoTD3Fetch_evaluations_dir4,filename), allow_pickle=True))


		for filename in os.listdir(ExperttoTD3Fetch_evaluations_dir5):
			print(filename)
			if filename.startswith('evaluations'):
				ExperttoTD3Fetch_evaluations5=(np.load(\
					os.path.join(ExperttoTD3Fetch_evaluations_dir5,filename), allow_pickle=True))

		#####################################################
		#####################################################

		for filename in os.listdir(TD3Fetch_evaluations_dir1):
			print(filename)
			if filename.startswith('evaluations'):
				TD3Fetch_evaluations1=(np.load(\
					os.path.join(TD3Fetch_evaluations_dir1,filename), allow_pickle=True))

		for filename in os.listdir(TD3Fetch_evaluations_dir2):
			print(filename)
			if filename.startswith('evaluations'):
				TD3Fetch_evaluations2=(np.load(\
					os.path.join(TD3Fetch_evaluations_dir2,filename), allow_pickle=True))

				
		for filename in os.listdir(TD3Fetch_evaluations_dir3):
			print(filename)
			if filename.startswith('evaluations'):
				TD3Fetch_evaluations3=(np.load(\
					os.path.join(TD3Fetch_evaluations_dir3,filename), allow_pickle=True))


		for filename in os.listdir(TD3Fetch_evaluations_dir4):
			print(filename)
			if filename.startswith('evaluations'):
				TD3Fetch_evaluations4=(np.load(\
					os.path.join(TD3Fetch_evaluations_dir4,filename), allow_pickle=True))


		for filename in os.listdir(TD3Fetch_evaluations_dir5):
			print(filename)
			if filename.startswith('evaluations'):
				TD3Fetch_evaluations5=(np.load(\
					os.path.join(TD3Fetch_evaluations_dir5,filename), allow_pickle=True))

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

		ExperttoTD3Fetch_eval1 = ExperttoTD3Fetch_evaluations1[:,1]
		ExperttoTD3Fetch_eval1_range = ExperttoTD3Fetch_evaluations1[:,0]

		ExperttoTD3Fetch_eval2 = ExperttoTD3Fetch_evaluations2[:,1]
		ExperttoTD3Fetch_eval2_range = ExperttoTD3Fetch_evaluations2[:,0]

		ExperttoTD3Fetch_eval3 = ExperttoTD3Fetch_evaluations3[:,1]
		ExperttoTD3Fetch_eval3_range = ExperttoTD3Fetch_evaluations3[:,0]

		ExperttoTD3Fetch_eval4 = ExperttoTD3Fetch_evaluations4[:,1]
		ExperttoTD3Fetch_eval4_range = ExperttoTD3Fetch_evaluations4[:,0]

		ExperttoTD3Fetch_eval5 = ExperttoTD3Fetch_evaluations5[:,1]
		ExperttoTD3Fetch_eval5_range = ExperttoTD3Fetch_evaluations5[:,0]

		ExperttoTD3Fetch_evals = np.array([ExperttoTD3Fetch_eval1, ExperttoTD3Fetch_eval2, ExperttoTD3Fetch_eval3, \
									ExperttoTD3Fetch_eval4, ExperttoTD3Fetch_eval5])

		ExperttoTD3Fetch_mean = np.mean(ExperttoTD3Fetch_evals,axis=0)
		ExperttoTD3Fetch_quartile1 = np.quantile(ExperttoTD3Fetch_evals, .25, interpolation='midpoint',axis=0)
		ExperttoTD3Fetch_quartile2 = np.quantile(ExperttoTD3Fetch_evals, .50, interpolation='midpoint',axis=0)
		ExperttoTD3Fetch_quartile3 = np.quantile(ExperttoTD3Fetch_evals, .75, interpolation='midpoint',axis=0)

		#####################################################################################
		#####################################################################################

		TD3Fetch_eval1 = TD3Fetch_evaluations1[:,1]
		TD3Fetch_eval1_range = TD3Fetch_evaluations1[:,0]

		TD3Fetch_eval2 = TD3Fetch_evaluations2[:,1]
		TD3Fetch_eval2_range = TD3Fetch_evaluations2[:,0]

		TD3Fetch_eval3 = TD3Fetch_evaluations3[:,1]
		TD3Fetch_eval3_range = TD3Fetch_evaluations3[:,0]

		TD3Fetch_eval4 = TD3Fetch_evaluations4[:,1]
		TD3Fetch_eval4_range = TD3Fetch_evaluations4[:,0]

		TD3Fetch_eval5 = TD3Fetch_evaluations5[:,1]
		TD3Fetch_eval5_range = TD3Fetch_evaluations5[:,0]

		TD3Fetch_evals = np.array([TD3Fetch_eval1, TD3Fetch_eval2, TD3Fetch_eval3, \
									TD3Fetch_eval4, TD3Fetch_eval5])

		TD3Fetch_mean = np.mean(TD3Fetch_evals,axis=0)
		TD3Fetch_quartile1 = np.quantile(TD3Fetch_evals, .25, interpolation='midpoint',axis=0)
		TD3Fetch_quartile2 = np.quantile(TD3Fetch_evals, .50, interpolation='midpoint',axis=0)
		TD3Fetch_quartile3 = np.quantile(TD3Fetch_evals, .75, interpolation='midpoint',axis=0)

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

		plt.title('Fetch Push', fontsize=25)

		plt.xlabel("evaluations", fontsize=18)
		plt.ylabel("rewards", fontsize=18)
		
		plt.plot(ExperttoTD3Fetch_eval1_range, ExperttoTD3Fetch_quartile2, label='Warm-Start TD3', color='tab:purple')
		plt.fill_between(ExperttoTD3Fetch_eval1_range, ExperttoTD3Fetch_quartile2, ExperttoTD3Fetch_quartile1,alpha=0.3,color='tab:purple'); 
		plt.fill_between(ExperttoTD3Fetch_eval1_range, ExperttoTD3Fetch_quartile2, ExperttoTD3Fetch_quartile3,alpha=0.3,color='tab:purple'); 
		
		plt.plot(TD3Fetch_eval1_range, TD3Fetch_quartile2, label='TD3', color='tab:red')
		plt.fill_between(TD3Fetch_eval1_range, TD3Fetch_quartile2, TD3Fetch_quartile1,alpha=0.3,color='tab:red'); 
		plt.fill_between(TD3Fetch_eval1_range, TD3Fetch_quartile2, TD3Fetch_quartile3,alpha=0.3,color='tab:red'); 

		plt.plot(BC_Uncertainty_eval1_range, BC_Uncertainty_quartile2, label='CCL-PQD ', color='tab:green')
		plt.fill_between(BC_Uncertainty_eval1_range, BC_Uncertainty_quartile2, BC_Uncertainty_quartile1,alpha=0.3,color='tab:green'); 
		plt.fill_between(BC_Uncertainty_eval1_range, BC_Uncertainty_quartile2, BC_Uncertainty_quartile3,alpha=0.3,color='tab:green'); 

		plt.style.use('ggplot')
		plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
		ax = plt.gca()
		ax.xaxis.get_offset_text().set_fontsize(16)
		ax.yaxis.get_offset_text().set_fontsize(16)
		ax.yaxis.get_offset_text().set_x(-.1)
		
		plt.xticks(fontsize=18)
		plt.yticks(fontsize=18)
		
		plt.legend(fontsize=18)
		plt.savefig('Fetch Push Confidence_Scheduled_BC ' + str(alpha) + ' vs. ExperttoTD3 vs. TD3.png', bbox_inches = 'tight')
		plt.close()
		##################################################################
		run_evals = [(TD3Fetch_evals, 'Fetch', 'TD3', '0', ''), \
						(ExperttoTD3Fetch_evals, 'Push BC', 'TD3', '26.4', ''), \
						(BC_Uncertainty_evals, '', 'CCL-PQD', '26.4', '0.01')]

		print_metrics(run_evals)

if __name__ == "__main__":

	dg = DrawGraphs()
	dg.draw()