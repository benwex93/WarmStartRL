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

		ExperttoTD3Fetch_evaluations_dir1 = results_dir + 'FetchPickAndPlace-v1_results/TD3_FetchPickAndPlace-v1_0_2022-02-27 13:37:42.0553692022-02-27 13:37:42.055509'
		ExperttoTD3Fetch_evaluations_dir2 = results_dir + 'FetchPickAndPlace-v1_results/TD3_FetchPickAndPlace-v1_1_2022-02-27 13:37:41.0139052022-02-27 13:37:41.014213'
		ExperttoTD3Fetch_evaluations_dir3 = results_dir + 'FetchPickAndPlace-v1_results/TD3_FetchPickAndPlace-v1_2_2022-02-27 13:37:41.8403662022-02-27 13:37:41.840466'
		ExperttoTD3Fetch_evaluations_dir4 = results_dir + 'FetchPickAndPlace-v1_results/TD3_FetchPickAndPlace-v1_3_2022-02-27 13:37:41.5917212022-02-27 13:37:41.591849'
		ExperttoTD3Fetch_evaluations_dir5 = results_dir + 'FetchPickAndPlace-v1_results/TD3_FetchPickAndPlace-v1_4_2022-02-27 13:37:41.3900502022-02-27 13:37:41.390177'
		
		# ExperttoTD3Fetch_evaluations_dir1 = results_dir + 'FetchPickAndPlace-v1_results/TD3_FetchPickAndPlace-v1_0_2022-01-13 18:19:40.8659802022-01-13 18:19:40.866088'
		# ExperttoTD3Fetch_evaluations_dir2 = results_dir + 'FetchPickAndPlace-v1_results/TD3_FetchPickAndPlace-v1_1_2022-01-13 20:39:34.7526402022-01-13 20:39:34.752742'
		# ExperttoTD3Fetch_evaluations_dir3 = results_dir + 'FetchPickAndPlace-v1_results/TD3_FetchPickAndPlace-v1_2_2022-01-13 23:13:05.1979372022-01-13 23:13:05.198016'
		# ExperttoTD3Fetch_evaluations_dir4 = results_dir + 'FetchPickAndPlace-v1_results/TD3_FetchPickAndPlace-v1_3_2022-01-14 02:10:15.5546672022-01-14 02:10:15.554760'
		# ExperttoTD3Fetch_evaluations_dir5 = results_dir + 'FetchPickAndPlace-v1_results/TD3_FetchPickAndPlace-v1_4_2022-01-14 04:47:32.6942552022-01-14 04:47:32.694373'
		
		TD3Fetch_evaluations_dir1 = results_dir + 'FetchPickAndPlace-v1_results/TD3_FetchPickAndPlace-v1_0_2022-01-13 18:19:45.1439122022-01-13 18:19:45.143996'
		TD3Fetch_evaluations_dir2 = results_dir + 'FetchPickAndPlace-v1_results/TD3_FetchPickAndPlace-v1_1_2022-01-13 20:39:38.8056292022-01-13 20:39:38.805711'
		TD3Fetch_evaluations_dir3 = results_dir + 'FetchPickAndPlace-v1_results/TD3_FetchPickAndPlace-v1_2_2022-01-13 23:13:00.7499872022-01-13 23:13:00.750084'
		TD3Fetch_evaluations_dir4 = results_dir + 'FetchPickAndPlace-v1_results/TD3_FetchPickAndPlace-v1_3_2022-01-14 02:10:15.6817772022-01-14 02:10:15.681897'
		TD3Fetch_evaluations_dir5 = results_dir + 'FetchPickAndPlace-v1_results/TD3_FetchPickAndPlace-v1_4_2022-01-14 04:47:37.0016152022-01-14 04:47:37.001694'
		
		# #.01 old
		# BC_Uncertainty_evaluations_dir1 = results_dir + 'FetchPickAndPlace-v1_results/TD3CP_FetchPickAndPlace-v1_0_2022-01-12 22:08:03.9761662022-01-12 22:08:03.976257'
		# BC_Uncertainty_evaluations_dir2 = results_dir + 'FetchPickAndPlace-v1_results/TD3CP_FetchPickAndPlace-v1_1_2022-01-13 01:04:50.0991872022-01-13 01:04:50.099269'
		# BC_Uncertainty_evaluations_dir3 = results_dir + 'FetchPickAndPlace-v1_results/TD3CP_FetchPickAndPlace-v1_2_2022-01-13 03:49:28.7424042022-01-13 03:49:28.742495'
		# BC_Uncertainty_evaluations_dir4 = results_dir + 'FetchPickAndPlace-v1_results/TD3CP_FetchPickAndPlace-v1_3_2022-01-13 06:38:58.1611962022-01-13 06:38:58.161287'
		# BC_Uncertainty_evaluations_dir5 = results_dir + 'FetchPickAndPlace-v1_results/TD3CP_FetchPickAndPlace-v1_4_2022-01-13 09:23:59.0033872022-01-13 09:23:59.003634'
				
		#.01
		BC_Uncertainty_evaluations_dir1 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_0_2022-02-27 00:07:16.2669012022-02-27 00:07:16.267215'
		BC_Uncertainty_evaluations_dir2 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_1_2022-02-27 02:09:27.7487322022-02-27 02:09:27.748805'
		BC_Uncertainty_evaluations_dir3 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_2_2022-02-27 04:13:26.1045802022-02-27 04:13:26.104666'
		BC_Uncertainty_evaluations_dir4 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_3_2022-02-27 06:11:11.6969652022-02-27 06:11:11.697039'
		BC_Uncertainty_evaluations_dir5 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_4_2022-02-27 08:09:23.9029102022-02-27 08:09:23.902988'
		
		# # alpha=0.01
		# CCL_evaluations_dir11 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_0_2022-02-27 00:07:16.2669012022-02-27 00:07:16.267215'
		# CCL_evaluations_dir12 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_1_2022-02-27 02:09:27.7487322022-02-27 02:09:27.748805'
		# CCL_evaluations_dir13 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_2_2022-02-27 04:13:26.1045802022-02-27 04:13:26.104666'
		# CCL_evaluations_dir14 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_3_2022-02-27 06:11:11.6969652022-02-27 06:11:11.697039'
		# CCL_evaluations_dir15 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_4_2022-02-27 08:09:23.9029102022-02-27 08:09:23.902988'		
		
		# # alpha=0.001
		# CCL_evaluations_dir21 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_0_2022-02-27 00:07:18.7510262022-02-27 00:07:18.751101'
		# CCL_evaluations_dir22 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_1_2022-02-27 02:09:27.5306242022-02-27 02:09:27.530701'
		# CCL_evaluations_dir23 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_2_2022-02-27 04:13:28.4861802022-02-27 04:13:28.486457'
		# CCL_evaluations_dir24 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_3_2022-02-27 06:11:08.1119882022-02-27 06:11:08.112073'
		# CCL_evaluations_dir25 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_4_2022-02-27 08:09:23.6173892022-02-27 08:09:23.617461'

		# # alpha=0.0001
		# CCL_evaluations_dir31 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_0_2022-02-27 00:07:19.0476952022-02-27 00:07:19.047766'
		# CCL_evaluations_dir32 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_1_2022-02-27 02:09:24.1677552022-02-27 02:09:24.167863'
		# CCL_evaluations_dir33 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_2_2022-02-27 04:13:28.7291782022-02-27 04:13:28.729255'
		# CCL_evaluations_dir34 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_3_2022-02-27 06:11:11.8853902022-02-27 06:11:11.885468'
		# CCL_evaluations_dir35 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_4_2022-02-27 08:09:20.0370842022-02-27 08:09:20.037174'
			

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

		plt.title('Fetch PickAndPlace', fontsize=25)

		plt.xlabel("evaluations", fontsize=18)
		plt.ylabel("rewards", fontsize=18)
		
		plt.plot(ExperttoTD3Fetch_eval1_range, ExperttoTD3Fetch_quartile2, label='Warm-Start TD3', color='tab:purple')
		plt.fill_between(ExperttoTD3Fetch_eval1_range, ExperttoTD3Fetch_quartile2, ExperttoTD3Fetch_quartile1,alpha=0.3,color='tab:purple'); 
		plt.fill_between(ExperttoTD3Fetch_eval1_range, ExperttoTD3Fetch_quartile2, ExperttoTD3Fetch_quartile3,alpha=0.3,color='tab:purple'); 
		
		plt.plot(TD3Fetch_eval1_range, TD3Fetch_quartile2, label='TD3', color='tab:red')
		plt.fill_between(TD3Fetch_eval1_range, TD3Fetch_quartile2, TD3Fetch_quartile1,alpha=0.3,color='tab:red'); 
		plt.fill_between(TD3Fetch_eval1_range, TD3Fetch_quartile2, TD3Fetch_quartile3,alpha=0.3,color='tab:red'); 

		plt.plot(BC_Uncertainty_eval1_range, BC_Uncertainty_quartile2, label='CCL-PQD', color='tab:green')
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
		plt.savefig('Fetch Confidence_Scheduled_BC vs. ExperttoTD3 vs. TD3.png', bbox_inches = 'tight')
		plt.close()
		##################################################################
		run_evals = [(TD3Fetch_evals, 'Fetch', 'TD3', '0', ''), \
						(ExperttoTD3Fetch_evals, 'PickAnd', 'TD3', '43.6', ''), \
						(BC_Uncertainty_evals, 'Place BC', 'CCL-PQD', '43.6', '0.0001')]

		print_metrics(run_evals)

if __name__ == "__main__":

	dg = DrawGraphs()
	dg.draw()