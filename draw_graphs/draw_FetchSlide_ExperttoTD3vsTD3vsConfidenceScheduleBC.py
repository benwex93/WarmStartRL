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


		ExperttoTD3Fetch_evaluations_dir1 = results_dir + 'FetchSlide-v1_results/TD3_FetchSlide-v1_0_2022-02-27 13:37:41.1768132022-02-27 13:37:41.176899'
		ExperttoTD3Fetch_evaluations_dir2 = results_dir + 'FetchSlide-v1_results/TD3_FetchSlide-v1_1_2022-02-27 13:37:38.4446422022-02-27 13:37:38.445160'
		ExperttoTD3Fetch_evaluations_dir3 = results_dir + 'FetchSlide-v1_results/TD3_FetchSlide-v1_2_2022-02-27 13:37:42.2376532022-02-27 13:37:42.237808'
		ExperttoTD3Fetch_evaluations_dir4 = results_dir + 'FetchSlide-v1_results/TD3_FetchSlide-v1_3_2022-02-27 13:37:40.6054162022-02-27 13:37:40.605512'
		ExperttoTD3Fetch_evaluations_dir5 = results_dir + 'FetchSlide-v1_results/TD3_FetchSlide-v1_4_2022-02-27 13:37:40.7992212022-02-27 13:37:40.799335'
		
		# ExperttoTD3Fetch_evaluations_dir1 = results_dir + 'FetchSlide-v1_results/TD3_FetchSlide-v1_0_2022-02-15 22:03:49.1804152022-02-15 22:03:49.180506'
		# ExperttoTD3Fetch_evaluations_dir2 = results_dir + 'FetchSlide-v1_results/TD3_FetchSlide-v1_1_2022-02-16 01:09:04.2793792022-02-16 01:09:04.279468'
		# ExperttoTD3Fetch_evaluations_dir3 = results_dir + 'FetchSlide-v1_results/TD3_FetchSlide-v1_2_2022-02-16 04:20:43.3935422022-02-16 04:20:43.393636'
		# ExperttoTD3Fetch_evaluations_dir4 = results_dir + 'FetchSlide-v1_results/TD3_FetchSlide-v1_3_2022-02-16 07:26:55.2588082022-02-16 07:26:55.258895'
		# ExperttoTD3Fetch_evaluations_dir5 = results_dir + 'FetchSlide-v1_results/TD3_FetchSlide-v1_4_2022-02-16 10:23:01.5373872022-02-16 10:23:01.537492'
		
		TD3Fetch_evaluations_dir1 = results_dir + 'FetchSlide-v1_results/TD3_FetchSlide-v1_4_2022-02-16 09:14:51.4408902022-02-16 09:14:51.441219'
		TD3Fetch_evaluations_dir2 = results_dir + 'FetchSlide-v1_results/TD3_FetchSlide-v1_0_2022-02-15 21:55:48.7511262022-02-15 21:55:48.751207'
		TD3Fetch_evaluations_dir3 = results_dir + 'FetchSlide-v1_results/TD3_FetchSlide-v1_1_2022-02-16 00:42:12.4793252022-02-16 00:42:12.479761'
		TD3Fetch_evaluations_dir4 = results_dir + 'FetchSlide-v1_results/TD3_FetchSlide-v1_2_2022-02-16 03:35:49.7585972022-02-16 03:35:49.758716'
		TD3Fetch_evaluations_dir5 = results_dir + 'FetchSlide-v1_results/TD3_FetchSlide-v1_3_2022-02-16 06:18:37.8166032022-02-16 06:18:37.816694'
		
		# alpha=0.01
		# BC_Uncertainty_evaluations_dir1 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_0_2022-02-15 21:58:48.9754602022-02-15 21:58:48.975546'
		# BC_Uncertainty_evaluations_dir2 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_1_2022-02-16 01:21:38.4889652022-02-16 01:21:38.489086'
		# BC_Uncertainty_evaluations_dir3 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_2_2022-02-16 04:39:31.4981872022-02-16 04:39:31.498275'
		# BC_Uncertainty_evaluations_dir4 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_3_2022-02-16 07:58:57.6848682022-02-16 07:58:57.684968'
		# BC_Uncertainty_evaluations_dir5 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_4_2022-02-16 11:23:06.6755102022-02-16 11:23:06.675600'
				
		# alpha=0.001
		# BC_Uncertainty_evaluations_dir1 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_0_2022-02-15 21:58:49.1734242022-02-15 21:58:49.173513'
		# BC_Uncertainty_evaluations_dir2 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_1_2022-02-16 01:21:38.6871412022-02-16 01:21:38.687232'
		# BC_Uncertainty_evaluations_dir3 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_2_2022-02-16 04:39:31.7164442022-02-16 04:39:31.716568'
		# BC_Uncertainty_evaluations_dir4 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_3_2022-02-16 07:58:53.5848292022-02-16 07:58:53.585050'
		# BC_Uncertainty_evaluations_dir5 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_4_2022-02-16 11:23:02.8097372022-02-16 11:23:02.809837'
				
		# alpha=0.0001
		# BC_Uncertainty_evaluations_dir1 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_0_2022-02-15 21:58:44.6693912022-02-15 21:58:44.669718'
		# BC_Uncertainty_evaluations_dir2 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_1_2022-02-16 01:21:34.3237152022-02-16 01:21:34.323823'
		# BC_Uncertainty_evaluations_dir3 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_2_2022-02-16 04:39:27.4398982022-02-16 04:39:27.440010'
		# BC_Uncertainty_evaluations_dir4 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_3_2022-02-16 07:58:58.3473242022-02-16 07:58:58.347971'
		# BC_Uncertainty_evaluations_dir5 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_4_2022-02-16 11:23:06.8222142022-02-16 11:23:06.822302'
		
		#################
		#NEW
		alpha=''
		# alpha=0.01
		BC_Uncertainty_evaluations_dir1 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_0_2022-02-25 13:43:37.1231412022-02-25 13:43:37.123218'
		BC_Uncertainty_evaluations_dir2 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_1_2022-02-25 16:37:25.5898372022-02-25 16:37:25.589929'
		BC_Uncertainty_evaluations_dir3 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_2_2022-02-25 19:20:04.6730892022-02-25 19:20:04.673168'
		BC_Uncertainty_evaluations_dir4 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_3_2022-02-25 22:02:12.5018952022-02-25 22:02:12.501992'
		BC_Uncertainty_evaluations_dir5 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_4_2022-02-26 00:47:04.7317882022-02-26 00:47:04.732108'
				
		# alpha=0.001
		# BC_Uncertainty_evaluations_dir1 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_0_2022-02-25 13:43:24.7503682022-02-25 13:43:24.750601'
		# BC_Uncertainty_evaluations_dir2 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_1_2022-02-25 16:37:37.8291192022-02-25 16:37:37.829198'
		# BC_Uncertainty_evaluations_dir3 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_2_2022-02-25 19:19:56.6678302022-02-25 19:19:56.667911'
		# BC_Uncertainty_evaluations_dir4 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_3_2022-02-25 22:02:17.0399402022-02-25 22:02:17.040023'
		# BC_Uncertainty_evaluations_dir5 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_4_2022-02-26 00:46:56.9317122022-02-26 00:46:56.931811'
				
		# alpha=0.0001
		# BC_Uncertainty_evaluations_dir1 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_0_2022-02-25 13:43:29.2679492022-02-25 13:43:29.268035'
		# BC_Uncertainty_evaluations_dir2 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_1_2022-02-25 16:37:29.9582002022-02-25 16:37:29.958281'
		# BC_Uncertainty_evaluations_dir3 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_2_2022-02-25 19:19:52.7087622022-02-25 19:19:52.708855'
		# BC_Uncertainty_evaluations_dir4 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_3_2022-02-25 22:02:24.9767592022-02-25 22:02:24.976871'
		# BC_Uncertainty_evaluations_dir5 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_4_2022-02-26 00:46:48.8000942022-02-26 00:46:48.800178'
		

		# ###########################

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

		plt.title('Fetch Slide', fontsize=25)

		plt.xlabel("evaluations", fontsize=18)
		plt.ylabel("rewards", fontsize=18)
		
		plt.plot(ExperttoTD3Fetch_eval1_range, ExperttoTD3Fetch_quartile2, label='Warm-Start TD3', color='tab:purple')
		plt.fill_between(ExperttoTD3Fetch_eval1_range, ExperttoTD3Fetch_quartile2, ExperttoTD3Fetch_quartile1,alpha=0.3,color='tab:purple'); 
		plt.fill_between(ExperttoTD3Fetch_eval1_range, ExperttoTD3Fetch_quartile2, ExperttoTD3Fetch_quartile3,alpha=0.3,color='tab:purple'); 
		
		plt.plot(TD3Fetch_eval1_range, TD3Fetch_quartile2, label='TD3', color='tab:red')
		plt.fill_between(TD3Fetch_eval1_range, TD3Fetch_quartile2, TD3Fetch_quartile1,alpha=0.3,color='tab:red'); 
		plt.fill_between(TD3Fetch_eval1_range, TD3Fetch_quartile2, TD3Fetch_quartile3,alpha=0.3,color='tab:red'); 

		plt.plot(BC_Uncertainty_eval1_range, BC_Uncertainty_quartile2, label='CCL-PQD '+str(alpha), color='tab:green')
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
		# plt.savefig('Fetch Slide Confidence_Scheduled_BC ' + str(alpha) + ' vs. ExperttoTD3 vs. TD3.png', bbox_inches = 'tight')
		plt.savefig('Fetch Slide Confidence_Scheduled_BC vs. ExperttoTD3 vs. TD3.png', bbox_inches = 'tight')
		plt.close()
		##################################################################
		run_evals = [(TD3Fetch_evals, 'Fetch', 'TD3', '0', ''), \
						(ExperttoTD3Fetch_evals, 'Slide BC', 'TD3', '21.5', ''), \
						(BC_Uncertainty_evals, '', 'CCL-PQD', '21.5', '0.01')]

		print_metrics(run_evals)

if __name__ == "__main__":

	dg = DrawGraphs()
	dg.draw()