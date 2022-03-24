import numpy as np
import os
from matplotlib import pyplot as plt
import copy
import seaborn as sns; sns.set()
from adjustText import adjust_text

class DrawGraphs:
	def __init__(self):
		pass
	def draw(self, is_4000=False):

		results_dir='../results/'


		# #PERTURBATION
		# # ############4000
		if is_4000:
			#alpha: 0.01
			ExperttoTD3Cheetah_evaluations_dir11 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_1_2021-12-14 22:22:13.2940302021-12-14 22:22:13.294131'
			ExperttoTD3Cheetah_evaluations_dir12 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_2_2021-12-15 01:12:45.5435472021-12-15 01:12:45.543643'
			ExperttoTD3Cheetah_evaluations_dir13 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_3_2021-12-15 03:53:19.6722132021-12-15 03:53:19.672315'
			ExperttoTD3Cheetah_evaluations_dir14 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_4_2021-12-15 06:39:22.5135062021-12-15 06:39:22.513602'
			#alpha: 0.1
			ExperttoTD3Cheetah_evaluations_dir21 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_1_2021-12-14 22:22:12.6823562021-12-14 22:22:12.682691'
			ExperttoTD3Cheetah_evaluations_dir22 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_2_2021-12-15 01:12:45.3415072021-12-15 01:12:45.341602'
			ExperttoTD3Cheetah_evaluations_dir23 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_3_2021-12-15 03:53:20.0082602021-12-15 03:53:20.008360'
			ExperttoTD3Cheetah_evaluations_dir24 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_4_2021-12-15 06:39:17.9453102021-12-15 06:39:17.945511'
			#alpha: 0.2
			ExperttoTD3Cheetah_evaluations_dir31 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_1_2021-12-14 22:22:12.8553002021-12-14 22:22:12.855707'
			ExperttoTD3Cheetah_evaluations_dir32 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_2_2021-12-15 01:12:41.0802342021-12-15 01:12:41.080345'
			ExperttoTD3Cheetah_evaluations_dir33 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_3_2021-12-15 03:53:19.4878112021-12-15 03:53:19.487898'
			ExperttoTD3Cheetah_evaluations_dir34 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_4_2021-12-15 06:39:22.3166292021-12-15 06:39:22.316724'
			#alpha: 0.25
			ExperttoTD3Cheetah_evaluations_dir41 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_1_2021-12-14 22:22:13.5114062021-12-14 22:22:13.511496'
			ExperttoTD3Cheetah_evaluations_dir42 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_2_2021-12-15 01:12:46.0339462021-12-15 01:12:46.034029'
			ExperttoTD3Cheetah_evaluations_dir43 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_3_2021-12-15 03:53:15.6466002021-12-15 03:53:15.646702'
			ExperttoTD3Cheetah_evaluations_dir44 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_4_2021-12-15 06:39:21.9603882021-12-15 06:39:21.960476'
			#alpha: 1
			ExperttoTD3Cheetah_evaluations_dir51 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_1_2021-12-14 22:22:13.0730412021-12-14 22:22:13.073154'
			ExperttoTD3Cheetah_evaluations_dir52 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_2_2021-12-15 01:12:45.1403352021-12-15 01:12:45.140430'
			ExperttoTD3Cheetah_evaluations_dir53 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_3_2021-12-15 03:53:20.4215842021-12-15 03:53:20.421687'
			ExperttoTD3Cheetah_evaluations_dir54 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_4_2021-12-15 06:39:22.1248622021-12-15 06:39:22.124957'
			
		###########################
		else:
			# ############10000
			#alpha: 0.01
			ExperttoTD3Cheetah_evaluations_dir11 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_1_2021-12-15 09:26:39.1108762021-12-15 09:26:39.111055'
			ExperttoTD3Cheetah_evaluations_dir12 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_2_2021-12-15 12:13:41.2559132021-12-15 12:13:41.256002'
			ExperttoTD3Cheetah_evaluations_dir13 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_3_2021-12-15 15:03:10.7373042021-12-15 15:03:10.737413'
			ExperttoTD3Cheetah_evaluations_dir14 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_4_2021-12-15 17:44:59.5222242021-12-15 17:44:59.522351'
			#alpha: 0.1
			ExperttoTD3Cheetah_evaluations_dir21 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_1_2021-12-15 09:26:43.2689612021-12-15 09:26:43.269083'
			ExperttoTD3Cheetah_evaluations_dir22 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_2_2021-12-15 12:13:41.6784042021-12-15 12:13:41.678503'
			ExperttoTD3Cheetah_evaluations_dir23 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_3_2021-12-15 15:03:10.5368282021-12-15 15:03:10.536935'
			ExperttoTD3Cheetah_evaluations_dir24 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_4_2021-12-15 17:44:58.4262572021-12-15 17:44:58.426354'
			#alpha: 0.2
			ExperttoTD3Cheetah_evaluations_dir31 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_1_2021-12-15 09:26:43.6333592021-12-15 09:26:43.633464'
			ExperttoTD3Cheetah_evaluations_dir32 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_2_2021-12-15 12:13:41.8512872021-12-15 12:13:41.851381'
			ExperttoTD3Cheetah_evaluations_dir33 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_3_2021-12-15 15:03:12.5133212021-12-15 15:03:12.513420'
			ExperttoTD3Cheetah_evaluations_dir34 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_4_2021-12-15 17:44:54.4277282021-12-15 17:44:54.428258'
			#alpha: 0.25
			ExperttoTD3Cheetah_evaluations_dir41 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_1_2021-12-15 09:26:43.4499942021-12-15 09:26:43.450092'
			ExperttoTD3Cheetah_evaluations_dir42 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_2_2021-12-15 12:13:41.4700502021-12-15 12:13:41.470146'
			ExperttoTD3Cheetah_evaluations_dir43 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_3_2021-12-15 15:03:06.5759112021-12-15 15:03:06.576027'
			ExperttoTD3Cheetah_evaluations_dir44 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_4_2021-12-15 17:44:58.2433702021-12-15 17:44:58.243453'
			#alpha: 1
			ExperttoTD3Cheetah_evaluations_dir51 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_1_2021-12-15 09:26:44.0137092021-12-15 09:26:44.013803'
			ExperttoTD3Cheetah_evaluations_dir52 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_2_2021-12-15 12:13:37.0312132021-12-15 12:13:37.031332'
			ExperttoTD3Cheetah_evaluations_dir53 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_3_2021-12-15 15:03:11.6214862021-12-15 15:03:11.621578'
			ExperttoTD3Cheetah_evaluations_dir54 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Pertubation_HalfCheetah-v3_4_2021-12-15 17:44:58.9201562021-12-15 17:44:58.920346'

		ExperttoTD3Cheetah_evaluations_dir1 = \
									[ExperttoTD3Cheetah_evaluations_dir11, ExperttoTD3Cheetah_evaluations_dir12, \
										ExperttoTD3Cheetah_evaluations_dir13, ExperttoTD3Cheetah_evaluations_dir14, '0.01']

		ExperttoTD3Cheetah_evaluations_dir2 = \
									[ExperttoTD3Cheetah_evaluations_dir21, ExperttoTD3Cheetah_evaluations_dir22, \
										ExperttoTD3Cheetah_evaluations_dir23, ExperttoTD3Cheetah_evaluations_dir24,	'0.1']

		ExperttoTD3Cheetah_evaluations_dir3 = \
									[ExperttoTD3Cheetah_evaluations_dir31, ExperttoTD3Cheetah_evaluations_dir32, \
										ExperttoTD3Cheetah_evaluations_dir33, ExperttoTD3Cheetah_evaluations_dir34,	'0.2']

		ExperttoTD3Cheetah_evaluations_dir4 = \
									[ExperttoTD3Cheetah_evaluations_dir41, ExperttoTD3Cheetah_evaluations_dir42, \
										ExperttoTD3Cheetah_evaluations_dir43, ExperttoTD3Cheetah_evaluations_dir44, '0.25']

		ExperttoTD3Cheetah_evaluations_dir5 = \
									[ExperttoTD3Cheetah_evaluations_dir51, ExperttoTD3Cheetah_evaluations_dir52, \
										ExperttoTD3Cheetah_evaluations_dir53, ExperttoTD3Cheetah_evaluations_dir54,	'1.0']

		Expert1toTD3Cheetah_evaluations_dir = \
									[('Perturbation Net', 'tab:red', 'x'), \
										ExperttoTD3Cheetah_evaluations_dir1, ExperttoTD3Cheetah_evaluations_dir2, \
										ExperttoTD3Cheetah_evaluations_dir3, ExperttoTD3Cheetah_evaluations_dir4]
										# ExperttoTD3Cheetah_evaluations_dir3, ExperttoTD3Cheetah_evaluations_dir4, \
										# ExperttoTD3Cheetah_evaluations_dir5]


		# # ###########################

		# #BC CONSTRAINT
		# # ############4000
		if is_4000:
			#alpha: 0.0001
			ExperttoTD3Cheetah_evaluations_dir11 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_1_2021-12-09 19:55:57.9916382021-12-09 19:55:57.992060'
			ExperttoTD3Cheetah_evaluations_dir12 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_2_2021-12-09 22:31:18.8946212021-12-09 22:31:18.894751'
			ExperttoTD3Cheetah_evaluations_dir13 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_3_2021-12-10 01:11:05.5739282021-12-10 01:11:05.574285'
			ExperttoTD3Cheetah_evaluations_dir14 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_4_2021-12-10 03:56:30.7110632021-12-10 03:56:30.711163'
			#alpha: 0.01
			ExperttoTD3Cheetah_evaluations_dir21 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_1_2021-12-09 19:56:02.4915442021-12-09 19:56:02.491642'
			ExperttoTD3Cheetah_evaluations_dir22 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_2_2021-12-09 22:31:23.6474182021-12-09 22:31:23.647530'
			ExperttoTD3Cheetah_evaluations_dir23 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_3_2021-12-10 01:11:09.6143292021-12-10 01:11:09.614454'
			ExperttoTD3Cheetah_evaluations_dir24 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_4_2021-12-10 03:56:34.7999702021-12-10 03:56:34.800088'
			#alpha: 0.1
			ExperttoTD3Cheetah_evaluations_dir31 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_1_2021-12-09 19:56:02.0725412021-12-09 19:56:02.072625'
			ExperttoTD3Cheetah_evaluations_dir32 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_2_2021-12-09 22:31:22.9039692021-12-09 22:31:22.904056'
			ExperttoTD3Cheetah_evaluations_dir33 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_3_2021-12-10 01:11:09.7680552021-12-10 01:11:09.768154'
			ExperttoTD3Cheetah_evaluations_dir34 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_4_2021-12-10 03:56:34.9996262021-12-10 03:56:34.999728'
			#alpha: 0.5
			ExperttoTD3Cheetah_evaluations_dir41 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_1_2021-12-09 19:56:02.2888612021-12-09 19:56:02.288955'
			ExperttoTD3Cheetah_evaluations_dir42 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_2_2021-12-09 22:31:23.1356572021-12-09 22:31:23.135762'
			ExperttoTD3Cheetah_evaluations_dir43 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_3_2021-12-10 01:11:09.9399882021-12-10 01:11:09.940084'
			ExperttoTD3Cheetah_evaluations_dir44 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_4_2021-12-10 03:56:35.2712102021-12-10 03:56:35.271317'
			# fig_name = 'Cheetah ExperttoTD3 BC Constraint4000.png'
			###########################
		else:
			############100000
			#alpha: 0.0001
			ExperttoTD3Cheetah_evaluations_dir11 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_1_2021-12-12 18:43:15.0263762021-12-12 18:43:15.026469'
			ExperttoTD3Cheetah_evaluations_dir12 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_2_2021-12-12 21:23:55.9492802021-12-12 21:23:55.949384'
			ExperttoTD3Cheetah_evaluations_dir13 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_3_2021-12-12 23:45:52.3066282021-12-12 23:45:52.306743'
			ExperttoTD3Cheetah_evaluations_dir14 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_4_2021-12-13 01:58:49.1980252021-12-13 01:58:49.198146'
			#alpha: 0.01
			ExperttoTD3Cheetah_evaluations_dir21 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_1_2021-12-12 18:43:15.4206322021-12-12 18:43:15.420733'
			ExperttoTD3Cheetah_evaluations_dir22 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_2_2021-12-12 21:23:56.1341352021-12-12 21:23:56.134234'
			ExperttoTD3Cheetah_evaluations_dir23 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_3_2021-12-12 23:45:56.7075342021-12-12 23:45:56.707629'
			ExperttoTD3Cheetah_evaluations_dir24 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_4_2021-12-13 01:58:53.1629162021-12-13 01:58:53.163008'
			#alpha: 0.1
			ExperttoTD3Cheetah_evaluations_dir31 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_1_2021-12-12 18:43:15.2211742021-12-12 18:43:15.221275'
			ExperttoTD3Cheetah_evaluations_dir32 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_2_2021-12-12 21:23:59.7055152021-12-12 21:23:59.705620'
			ExperttoTD3Cheetah_evaluations_dir33 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_3_2021-12-12 23:45:56.4552202021-12-12 23:45:56.455322'
			ExperttoTD3Cheetah_evaluations_dir34 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_4_2021-12-13 01:58:54.0993832021-12-13 01:58:54.099494'
			#alpha: 0.5
			ExperttoTD3Cheetah_evaluations_dir41 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_1_2021-12-12 18:43:11.4222972021-12-12 18:43:11.422559'
			ExperttoTD3Cheetah_evaluations_dir42 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_2_2021-12-12 21:23:59.8961352021-12-12 21:23:59.896230'
			ExperttoTD3Cheetah_evaluations_dir43 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_3_2021-12-12 23:45:56.2426432021-12-12 23:45:56.242748'
			ExperttoTD3Cheetah_evaluations_dir44 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Constraint_HalfCheetah-v3_4_2021-12-13 01:58:53.3449112021-12-13 01:58:53.345011'

		ExperttoTD3Cheetah_evaluations_dir1 = \
									[ExperttoTD3Cheetah_evaluations_dir11, ExperttoTD3Cheetah_evaluations_dir12, \
										ExperttoTD3Cheetah_evaluations_dir13, ExperttoTD3Cheetah_evaluations_dir14, '1e-4']

		ExperttoTD3Cheetah_evaluations_dir2 = \
									[ExperttoTD3Cheetah_evaluations_dir21, ExperttoTD3Cheetah_evaluations_dir22, \
										ExperttoTD3Cheetah_evaluations_dir23, ExperttoTD3Cheetah_evaluations_dir24,	'0.01']

		ExperttoTD3Cheetah_evaluations_dir3 = \
									[ExperttoTD3Cheetah_evaluations_dir31, ExperttoTD3Cheetah_evaluations_dir32, \
										ExperttoTD3Cheetah_evaluations_dir33, ExperttoTD3Cheetah_evaluations_dir34,	'0.1']

		ExperttoTD3Cheetah_evaluations_dir4 = \
									[ExperttoTD3Cheetah_evaluations_dir41, ExperttoTD3Cheetah_evaluations_dir42, \
										ExperttoTD3Cheetah_evaluations_dir43, ExperttoTD3Cheetah_evaluations_dir44, '0.5']

		Expert2toTD3Cheetah_evaluations_dir = [('BC Policy Penalty', 'tab:blue', 'v'), \
										ExperttoTD3Cheetah_evaluations_dir1, ExperttoTD3Cheetah_evaluations_dir2, \
										ExperttoTD3Cheetah_evaluations_dir3, ExperttoTD3Cheetah_evaluations_dir4]
		# ###########################

		# #BC PENALTY
		# ############4000
		if is_4000:
			#alpha: 0.000000003
			ExperttoTD3Cheetah_evaluations_dir11 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 15:35:02.1975332021-12-13 15:35:02.197651'
			ExperttoTD3Cheetah_evaluations_dir12 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 15:35:02.1975332021-12-13 15:35:02.197651'
			ExperttoTD3Cheetah_evaluations_dir13 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 15:35:02.1975332021-12-13 15:35:02.197651'
			ExperttoTD3Cheetah_evaluations_dir14 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 15:35:02.1975332021-12-13 15:35:02.197651'
			#alpha: 0.00000003
			ExperttoTD3Cheetah_evaluations_dir21 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 15:35:06.5162572021-12-13 15:35:06.516347'
			ExperttoTD3Cheetah_evaluations_dir22 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 15:35:06.5162572021-12-13 15:35:06.516347'
			ExperttoTD3Cheetah_evaluations_dir23 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 15:35:06.5162572021-12-13 15:35:06.516347'
			ExperttoTD3Cheetah_evaluations_dir24 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 15:35:06.5162572021-12-13 15:35:06.516347'
			#alpha: 0.0000003
			ExperttoTD3Cheetah_evaluations_dir31 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 15:35:06.7254962021-12-13 15:35:06.725589'
			ExperttoTD3Cheetah_evaluations_dir32 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 15:35:06.7254962021-12-13 15:35:06.725589'
			ExperttoTD3Cheetah_evaluations_dir33 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 15:35:06.7254962021-12-13 15:35:06.725589'
			ExperttoTD3Cheetah_evaluations_dir34 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 15:35:06.7254962021-12-13 15:35:06.725589'
			#alpha: 0.000003
			ExperttoTD3Cheetah_evaluations_dir41 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 15:35:06.9185622021-12-13 15:35:06.918649'
			ExperttoTD3Cheetah_evaluations_dir42 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 15:35:06.9185622021-12-13 15:35:06.918649'
			ExperttoTD3Cheetah_evaluations_dir43 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 15:35:06.9185622021-12-13 15:35:06.918649'
			ExperttoTD3Cheetah_evaluations_dir44 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 15:35:06.9185622021-12-13 15:35:06.918649'
			#alpha: 0.00003
			ExperttoTD3Cheetah_evaluations_dir51 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 16:47:22.6210432021-12-13 16:47:22.621229'
			ExperttoTD3Cheetah_evaluations_dir52 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 16:47:22.6210432021-12-13 16:47:22.621229'
			ExperttoTD3Cheetah_evaluations_dir53 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 16:47:22.6210432021-12-13 16:47:22.621229'
			ExperttoTD3Cheetah_evaluations_dir54 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 16:47:22.6210432021-12-13 16:47:22.621229'
			#alpha: 0.0003
			ExperttoTD3Cheetah_evaluations_dir61 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 16:07:05.2648642021-12-13 16:07:05.264964'
			ExperttoTD3Cheetah_evaluations_dir62 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 16:07:05.2648642021-12-13 16:07:05.264964'
			ExperttoTD3Cheetah_evaluations_dir63 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 16:07:05.2648642021-12-13 16:07:05.264964'
			ExperttoTD3Cheetah_evaluations_dir64 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 16:07:05.2648642021-12-13 16:07:05.264964'
			#alpha: 0.003
			ExperttoTD3Cheetah_evaluations_dir71 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 15:35:06.9185622021-12-13 15:35:06.918649'
			ExperttoTD3Cheetah_evaluations_dir72 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 15:35:06.9185622021-12-13 15:35:06.918649'
			ExperttoTD3Cheetah_evaluations_dir73 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 15:35:06.9185622021-12-13 15:35:06.918649'
			ExperttoTD3Cheetah_evaluations_dir74 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 15:35:06.9185622021-12-13 15:35:06.918649'
			#alpha: 0.03
			ExperttoTD3Cheetah_evaluations_dir81 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 16:21:26.7056752021-12-13 16:21:26.705856'
			ExperttoTD3Cheetah_evaluations_dir82 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 16:21:26.7056752021-12-13 16:21:26.705856'
			ExperttoTD3Cheetah_evaluations_dir83 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 16:21:26.7056752021-12-13 16:21:26.705856'
			ExperttoTD3Cheetah_evaluations_dir84 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 16:21:26.7056752021-12-13 16:21:26.705856'
			#alpha: 0.3
			ExperttoTD3Cheetah_evaluations_dir91 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 16:37:05.0775322021-12-13 16:37:05.077753'
			ExperttoTD3Cheetah_evaluations_dir92 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 16:37:05.0775322021-12-13 16:37:05.077753'
			ExperttoTD3Cheetah_evaluations_dir93 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 16:37:05.0775322021-12-13 16:37:05.077753'
			ExperttoTD3Cheetah_evaluations_dir94 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_1_2021-12-13 16:37:05.0775322021-12-13 16:37:05.077753'
			#########################

		else:
			############10000
			#alpha: 0.000000003
			ExperttoTD3Cheetah_evaluations_dir11 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:43.3220432021-12-13 18:02:43.322128'
			ExperttoTD3Cheetah_evaluations_dir12 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:43.3220432021-12-13 18:02:43.322128'
			ExperttoTD3Cheetah_evaluations_dir13 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:43.3220432021-12-13 18:02:43.322128'
			ExperttoTD3Cheetah_evaluations_dir14 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:43.3220432021-12-13 18:02:43.322128'
			#alpha: 0.00000003
			ExperttoTD3Cheetah_evaluations_dir21 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:38.9533002021-12-13 18:02:38.953401'
			ExperttoTD3Cheetah_evaluations_dir22 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:38.9533002021-12-13 18:02:38.953401'
			ExperttoTD3Cheetah_evaluations_dir23 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:38.9533002021-12-13 18:02:38.953401'
			ExperttoTD3Cheetah_evaluations_dir24 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:38.9533002021-12-13 18:02:38.953401'
			#alpha: 0.0000003
			ExperttoTD3Cheetah_evaluations_dir31 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:43.5466232021-12-13 18:02:43.546733'
			ExperttoTD3Cheetah_evaluations_dir32 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:43.5466232021-12-13 18:02:43.546733'
			ExperttoTD3Cheetah_evaluations_dir33 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:43.5466232021-12-13 18:02:43.546733'
			ExperttoTD3Cheetah_evaluations_dir34 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:43.5466232021-12-13 18:02:43.546733'
			#alpha: 0.000003
			ExperttoTD3Cheetah_evaluations_dir41 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:43.7175822021-12-13 18:02:43.717671'
			ExperttoTD3Cheetah_evaluations_dir42 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:43.7175822021-12-13 18:02:43.717671'
			ExperttoTD3Cheetah_evaluations_dir43 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:43.7175822021-12-13 18:02:43.717671'
			ExperttoTD3Cheetah_evaluations_dir44 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:43.7175822021-12-13 18:02:43.717671'
			#alpha: 0.00003
			ExperttoTD3Cheetah_evaluations_dir51 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:44.0348672021-12-13 18:02:44.034965'
			ExperttoTD3Cheetah_evaluations_dir52 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:44.0348672021-12-13 18:02:44.034965'
			ExperttoTD3Cheetah_evaluations_dir53 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:44.0348672021-12-13 18:02:44.034965'
			ExperttoTD3Cheetah_evaluations_dir54 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:44.0348672021-12-13 18:02:44.034965'
			#alpha: 0.0003
			ExperttoTD3Cheetah_evaluations_dir61 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:44.0348672021-12-13 18:02:44.034965'
			ExperttoTD3Cheetah_evaluations_dir62 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:44.0348672021-12-13 18:02:44.034965'
			ExperttoTD3Cheetah_evaluations_dir63 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:44.0348672021-12-13 18:02:44.034965'
			ExperttoTD3Cheetah_evaluations_dir64 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:44.0348672021-12-13 18:02:44.034965'
			#alpha: 0.003
			ExperttoTD3Cheetah_evaluations_dir71 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:44.5211172021-12-13 18:02:44.521237'
			ExperttoTD3Cheetah_evaluations_dir72 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:44.5211172021-12-13 18:02:44.521237'
			ExperttoTD3Cheetah_evaluations_dir73 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:44.5211172021-12-13 18:02:44.521237'
			ExperttoTD3Cheetah_evaluations_dir74 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:44.5211172021-12-13 18:02:44.521237'
			#alpha: 0.03
			ExperttoTD3Cheetah_evaluations_dir81 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:44.8344432021-12-13 18:02:44.834544'
			ExperttoTD3Cheetah_evaluations_dir82 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:44.8344432021-12-13 18:02:44.834544'
			ExperttoTD3Cheetah_evaluations_dir83 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:44.8344432021-12-13 18:02:44.834544'
			ExperttoTD3Cheetah_evaluations_dir84 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:44.8344432021-12-13 18:02:44.834544'
			#alpha: 0.3
			ExperttoTD3Cheetah_evaluations_dir91 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:45.0920112021-12-13 18:02:45.092114'
			ExperttoTD3Cheetah_evaluations_dir92 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:45.0920112021-12-13 18:02:45.092114'
			ExperttoTD3Cheetah_evaluations_dir93 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:45.0920112021-12-13 18:02:45.092114'
			ExperttoTD3Cheetah_evaluations_dir94 = results_dir + 'HalfCheetah-v3_results/TD3_BC_Penalty_HalfCheetah-v3_0_2021-12-13 18:02:45.0920112021-12-13 18:02:45.092114'
		
		ExperttoTD3Cheetah_evaluations_dir1 = \
									[ExperttoTD3Cheetah_evaluations_dir11, ExperttoTD3Cheetah_evaluations_dir12, \
										ExperttoTD3Cheetah_evaluations_dir13, ExperttoTD3Cheetah_evaluations_dir14, '3e-9']

		ExperttoTD3Cheetah_evaluations_dir2 = \
									[ExperttoTD3Cheetah_evaluations_dir21, ExperttoTD3Cheetah_evaluations_dir22, \
										ExperttoTD3Cheetah_evaluations_dir23, ExperttoTD3Cheetah_evaluations_dir24,	'3e-8']

		ExperttoTD3Cheetah_evaluations_dir3 = \
									[ExperttoTD3Cheetah_evaluations_dir31, ExperttoTD3Cheetah_evaluations_dir32, \
										ExperttoTD3Cheetah_evaluations_dir33, ExperttoTD3Cheetah_evaluations_dir34,	'3e-7']

		ExperttoTD3Cheetah_evaluations_dir4 = \
									[ExperttoTD3Cheetah_evaluations_dir41, ExperttoTD3Cheetah_evaluations_dir42, \
										ExperttoTD3Cheetah_evaluations_dir43, ExperttoTD3Cheetah_evaluations_dir44, '3e-6']

		ExperttoTD3Cheetah_evaluations_dir5 = \
									[ExperttoTD3Cheetah_evaluations_dir51, ExperttoTD3Cheetah_evaluations_dir52, \
										ExperttoTD3Cheetah_evaluations_dir53, ExperttoTD3Cheetah_evaluations_dir54, '3e-5']

		ExperttoTD3Cheetah_evaluations_dir6 = \
									[ExperttoTD3Cheetah_evaluations_dir61, ExperttoTD3Cheetah_evaluations_dir62, \
										ExperttoTD3Cheetah_evaluations_dir63, ExperttoTD3Cheetah_evaluations_dir64,	'3e-4']

		ExperttoTD3Cheetah_evaluations_dir7 = \
									[ExperttoTD3Cheetah_evaluations_dir71, ExperttoTD3Cheetah_evaluations_dir72, \
										ExperttoTD3Cheetah_evaluations_dir73, ExperttoTD3Cheetah_evaluations_dir74,	'3e-3']

		ExperttoTD3Cheetah_evaluations_dir8 = \
									[ExperttoTD3Cheetah_evaluations_dir81, ExperttoTD3Cheetah_evaluations_dir82, \
										ExperttoTD3Cheetah_evaluations_dir83, ExperttoTD3Cheetah_evaluations_dir84, '3e-2']

		ExperttoTD3Cheetah_evaluations_dir9 = \
									[ExperttoTD3Cheetah_evaluations_dir91, ExperttoTD3Cheetah_evaluations_dir92, \
										ExperttoTD3Cheetah_evaluations_dir93, ExperttoTD3Cheetah_evaluations_dir94, '3e-1']

		Expert3toTD3Cheetah_evaluations_dir = [('BC Penalty', 'tab:purple'), \
										ExperttoTD3Cheetah_evaluations_dir1, ExperttoTD3Cheetah_evaluations_dir2, \
										ExperttoTD3Cheetah_evaluations_dir3, ExperttoTD3Cheetah_evaluations_dir4, \
										ExperttoTD3Cheetah_evaluations_dir5, ExperttoTD3Cheetah_evaluations_dir6, \
										ExperttoTD3Cheetah_evaluations_dir7, ExperttoTD3Cheetah_evaluations_dir8, \
										ExperttoTD3Cheetah_evaluations_dir9]
		# # ###########################

		# #LEARNING RATE
		# # ###########4000
		if is_4000:
			#lr:3e-7
			ExperttoTD3Cheetah_evaluations_dir11 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 01:05:43.7208942022-02-17 01:05:43.720999'
			ExperttoTD3Cheetah_evaluations_dir12 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 01:05:43.7208942022-02-17 01:05:43.720999'
			ExperttoTD3Cheetah_evaluations_dir13 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 01:05:43.7208942022-02-17 01:05:43.720999'
			ExperttoTD3Cheetah_evaluations_dir14 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 01:05:43.7208942022-02-17 01:05:43.720999'
			#lr3e-6
			ExperttoTD3Cheetah_evaluations_dir21 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 01:05:43.4023082022-02-17 01:05:43.402403'
			ExperttoTD3Cheetah_evaluations_dir22 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 01:05:43.4023082022-02-17 01:05:43.402403'
			ExperttoTD3Cheetah_evaluations_dir23 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 01:05:43.4023082022-02-17 01:05:43.402403'
			ExperttoTD3Cheetah_evaluations_dir24 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 01:05:43.4023082022-02-17 01:05:43.402403'
			#lr:3e-5
			ExperttoTD3Cheetah_evaluations_dir31 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 01:05:43.5466082022-02-17 01:05:43.546690'
			ExperttoTD3Cheetah_evaluations_dir32 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 01:05:43.5466082022-02-17 01:05:43.546690'
			ExperttoTD3Cheetah_evaluations_dir33 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 01:05:43.5466082022-02-17 01:05:43.546690'
			ExperttoTD3Cheetah_evaluations_dir34 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 01:05:43.5466082022-02-17 01:05:43.546690'
			#lr: 0.0003
			ExperttoTD3Cheetah_evaluations_dir41 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 01:05:39.6776132022-02-17 01:05:39.677705'
			ExperttoTD3Cheetah_evaluations_dir42 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 01:05:39.6776132022-02-17 01:05:39.677705'
			ExperttoTD3Cheetah_evaluations_dir43 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 01:05:39.6776132022-02-17 01:05:39.677705'
			ExperttoTD3Cheetah_evaluations_dir44 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 01:05:39.6776132022-02-17 01:05:39.677705'
			###########################
		else:
			###########10000
			#lr: 3e-7
			ExperttoTD3Cheetah_evaluations_dir11 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 19:17:06.2175642022-02-17 19:17:06.217670'
			ExperttoTD3Cheetah_evaluations_dir12 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 19:17:06.2175642022-02-17 19:17:06.217670'
			ExperttoTD3Cheetah_evaluations_dir13 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 19:17:06.2175642022-02-17 19:17:06.217670'
			ExperttoTD3Cheetah_evaluations_dir14 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 19:17:06.2175642022-02-17 19:17:06.217670'
			#lr: 3e-6
			ExperttoTD3Cheetah_evaluations_dir21 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 19:17:05.8429232022-02-17 19:17:05.843018'
			ExperttoTD3Cheetah_evaluations_dir22 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 19:17:05.8429232022-02-17 19:17:05.843018'
			ExperttoTD3Cheetah_evaluations_dir23 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 19:17:05.8429232022-02-17 19:17:05.843018'
			ExperttoTD3Cheetah_evaluations_dir24 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 19:17:05.8429232022-02-17 19:17:05.843018'
			#lr: 3e-5
			ExperttoTD3Cheetah_evaluations_dir31 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 19:17:01.8207742022-02-17 19:17:01.820888'
			ExperttoTD3Cheetah_evaluations_dir32 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 19:17:01.8207742022-02-17 19:17:01.820888'
			ExperttoTD3Cheetah_evaluations_dir33 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 19:17:01.8207742022-02-17 19:17:01.820888'
			ExperttoTD3Cheetah_evaluations_dir34 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 19:17:01.8207742022-02-17 19:17:01.820888'
			#lr: 0.0003
			ExperttoTD3Cheetah_evaluations_dir41 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 19:17:06.0383432022-02-17 19:17:06.038483'
			ExperttoTD3Cheetah_evaluations_dir42 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 19:17:06.0383432022-02-17 19:17:06.038483'
			ExperttoTD3Cheetah_evaluations_dir43 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 19:17:06.0383432022-02-17 19:17:06.038483'
			ExperttoTD3Cheetah_evaluations_dir44 = results_dir + 'HalfCheetah-v3_results/TD3_learning_rate_HalfCheetah-v3_1_2022-02-17 19:17:06.0383432022-02-17 19:17:06.038483'

		ExperttoTD3Cheetah_evaluations_dir1 = \
									[ExperttoTD3Cheetah_evaluations_dir11, ExperttoTD3Cheetah_evaluations_dir12, \
										ExperttoTD3Cheetah_evaluations_dir13, ExperttoTD3Cheetah_evaluations_dir14, '3e-6']

		ExperttoTD3Cheetah_evaluations_dir2 = \
									[ExperttoTD3Cheetah_evaluations_dir21, ExperttoTD3Cheetah_evaluations_dir22, \
										ExperttoTD3Cheetah_evaluations_dir23, ExperttoTD3Cheetah_evaluations_dir24,	'3e-5']

		ExperttoTD3Cheetah_evaluations_dir3 = \
									[ExperttoTD3Cheetah_evaluations_dir31, ExperttoTD3Cheetah_evaluations_dir32, \
										ExperttoTD3Cheetah_evaluations_dir33, ExperttoTD3Cheetah_evaluations_dir34,	'3e-4']

		ExperttoTD3Cheetah_evaluations_dir4 = \
									[ExperttoTD3Cheetah_evaluations_dir41, ExperttoTD3Cheetah_evaluations_dir42, \
										ExperttoTD3Cheetah_evaluations_dir43, ExperttoTD3Cheetah_evaluations_dir44, '3e-3']

		Expert4toTD3Cheetah_evaluations_dir = [('Learning Rate', 'tab:olive', 's'), \
										ExperttoTD3Cheetah_evaluations_dir1, ExperttoTD3Cheetah_evaluations_dir2, \
										ExperttoTD3Cheetah_evaluations_dir3, ExperttoTD3Cheetah_evaluations_dir4]
		# # ###########################

		# #GRADIENT CLIPPING
		# # # ############4000
		if is_4000:
			#gradient: 3e-9
			ExperttoTD3Cheetah_evaluations_dir11 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_1_2021-12-09 18:01:06.5959822021-12-09 18:01:06.596229'
			ExperttoTD3Cheetah_evaluations_dir12 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_2_2021-12-09 20:13:53.7573202021-12-09 20:13:53.757429'
			ExperttoTD3Cheetah_evaluations_dir13 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_3_2021-12-09 22:50:20.7931852021-12-09 22:50:20.793443'
			ExperttoTD3Cheetah_evaluations_dir14 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_4_2021-12-10 01:28:42.8752192021-12-10 01:28:42.875369'
			#gradient: 3e-8
			ExperttoTD3Cheetah_evaluations_dir21 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_1_2021-12-09 18:01:11.2102802021-12-09 18:01:11.210376'
			ExperttoTD3Cheetah_evaluations_dir22 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_2_2021-12-09 20:13:49.2973722021-12-09 20:13:49.297512'
			ExperttoTD3Cheetah_evaluations_dir23 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_3_2021-12-09 22:50:24.3868882021-12-09 22:50:24.387003'
			ExperttoTD3Cheetah_evaluations_dir24 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_4_2021-12-10 01:28:43.1240672021-12-10 01:28:43.124174'
			#gradient: 3e-6
			ExperttoTD3Cheetah_evaluations_dir31 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_1_2021-12-09 18:01:10.8715212021-12-09 18:01:10.871621'
			ExperttoTD3Cheetah_evaluations_dir32 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_2_2021-12-09 20:13:53.5381622021-12-09 20:13:53.538253'
			ExperttoTD3Cheetah_evaluations_dir33 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_3_2021-12-09 22:50:20.8916982021-12-09 22:50:20.891784'
			ExperttoTD3Cheetah_evaluations_dir34 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_4_2021-12-10 01:28:42.6650042021-12-10 01:28:42.665105'
			#gradient: 3e-3
			ExperttoTD3Cheetah_evaluations_dir41 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_1_2021-12-09 18:01:10.6687962021-12-09 18:01:10.669201'
			ExperttoTD3Cheetah_evaluations_dir42 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_2_2021-12-09 20:13:54.4104982021-12-09 20:13:54.410592'
			ExperttoTD3Cheetah_evaluations_dir43 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_3_2021-12-09 22:50:24.5792802021-12-09 22:50:24.579388'
			ExperttoTD3Cheetah_evaluations_dir44 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_4_2021-12-10 01:28:38.4601412021-12-10 01:28:38.460235'
			# ###########################
		else:
			############100000
			#gradient: 3e-9
			ExperttoTD3Cheetah_evaluations_dir11 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_1_2021-12-10 04:06:10.3431012021-12-10 04:06:10.343218'
			ExperttoTD3Cheetah_evaluations_dir12 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_2_2021-12-10 06:49:10.7289162021-12-10 06:49:10.729008'
			ExperttoTD3Cheetah_evaluations_dir13 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_3_2021-12-10 09:04:06.8769352021-12-10 09:04:06.877074'
			ExperttoTD3Cheetah_evaluations_dir14 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_4_2021-12-10 11:11:52.9994882021-12-10 11:11:52.999586'
			#gradient: 3e-8
			ExperttoTD3Cheetah_evaluations_dir21 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_1_2021-12-10 04:06:10.8396962021-12-10 04:06:10.839821'
			ExperttoTD3Cheetah_evaluations_dir22 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_2_2021-12-10 06:49:06.8055152021-12-10 06:49:06.805610'
			ExperttoTD3Cheetah_evaluations_dir23 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_3_2021-12-10 09:04:11.3086542021-12-10 09:04:11.308758'
			ExperttoTD3Cheetah_evaluations_dir24 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_4_2021-12-10 11:11:48.4818202021-12-10 11:11:48.481914'
			#gradient: 3e-6
			ExperttoTD3Cheetah_evaluations_dir31 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_1_2021-12-10 04:06:06.1347522021-12-10 04:06:06.134851'
			ExperttoTD3Cheetah_evaluations_dir32 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_2_2021-12-10 06:49:11.3126672021-12-10 06:49:11.312766'
			ExperttoTD3Cheetah_evaluations_dir33 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_3_2021-12-10 09:04:10.9247702021-12-10 09:04:10.924863'
			ExperttoTD3Cheetah_evaluations_dir34 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_4_2021-12-10 11:11:52.6093702021-12-10 11:11:52.609464'
			#gradient: 3e-3
			ExperttoTD3Cheetah_evaluations_dir41 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_1_2021-12-10 04:06:10.1604992021-12-10 04:06:10.160598'
			ExperttoTD3Cheetah_evaluations_dir42 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_2_2021-12-10 06:49:10.9401152021-12-10 06:49:10.940213'
			ExperttoTD3Cheetah_evaluations_dir43 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_3_2021-12-10 09:04:10.7125892021-12-10 09:04:10.712677'
			ExperttoTD3Cheetah_evaluations_dir44 = results_dir + 'HalfCheetah-v3_results/TD3_gradient_clipping_HalfCheetah-v3_4_2021-12-10 11:11:52.8706102021-12-10 11:11:52.870702'
			###########################

		ExperttoTD3Cheetah_evaluations_dir1 = \
									[ExperttoTD3Cheetah_evaluations_dir11, ExperttoTD3Cheetah_evaluations_dir12, \
										ExperttoTD3Cheetah_evaluations_dir13, ExperttoTD3Cheetah_evaluations_dir14, '3e-9']

		ExperttoTD3Cheetah_evaluations_dir2 = \
									[ExperttoTD3Cheetah_evaluations_dir21, ExperttoTD3Cheetah_evaluations_dir22, \
										ExperttoTD3Cheetah_evaluations_dir23, ExperttoTD3Cheetah_evaluations_dir24,	'3e-8']

		ExperttoTD3Cheetah_evaluations_dir3 = \
									[ExperttoTD3Cheetah_evaluations_dir31, ExperttoTD3Cheetah_evaluations_dir32, \
										ExperttoTD3Cheetah_evaluations_dir33, ExperttoTD3Cheetah_evaluations_dir34,	'3e-6']

		ExperttoTD3Cheetah_evaluations_dir4 = \
									[ExperttoTD3Cheetah_evaluations_dir41, ExperttoTD3Cheetah_evaluations_dir42, \
										ExperttoTD3Cheetah_evaluations_dir43, ExperttoTD3Cheetah_evaluations_dir44, '3e-3']

		Expert5toTD3Cheetah_evaluations_dir = [('Gradient Clip', 'tab:pink', 'P'), \
										ExperttoTD3Cheetah_evaluations_dir1, ExperttoTD3Cheetah_evaluations_dir2, \
										ExperttoTD3Cheetah_evaluations_dir3, ExperttoTD3Cheetah_evaluations_dir4]
		# ##################################################################
		# ##################################################################

		if is_4000:
			#0.01
			CCL_evaluations_dir11 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_0_2022-01-09 17:05:52.4804842022-01-09 17:05:52.480589'
			CCL_evaluations_dir12 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_1_2022-01-09 19:30:13.6972252022-01-09 19:30:13.697332'
			CCL_evaluations_dir13 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_2_2022-01-09 22:32:47.3887652022-01-09 22:32:47.388906'
			CCL_evaluations_dir14 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_3_2022-01-10 01:33:13.4627242022-01-10 01:33:13.462879'
			CCL_evaluations_dir15 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_4_2022-01-10 05:14:21.6788572022-01-10 05:14:21.679020'
		
			#0.001
			CCL_evaluations_dir21 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_0_2022-01-20 16:04:38.1257992022-01-20 16:04:38.125955'
			CCL_evaluations_dir22 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_1_2022-01-20 16:04:31.7042002022-01-20 16:04:31.704591'
			CCL_evaluations_dir23 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_2_2022-01-20 16:04:37.0387232022-01-20 16:04:37.038848'
			CCL_evaluations_dir24 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_3_2022-01-20 16:04:37.7288342022-01-20 16:04:37.728995'
			CCL_evaluations_dir25 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_4_2022-01-20 16:04:37.9302352022-01-20 16:04:37.930610'
		
			#0.0001
			CCL_evaluations_dir31 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_0_2022-01-20 16:04:39.7479022022-01-20 16:04:39.748026'
			CCL_evaluations_dir32 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_1_2022-01-20 16:04:39.1380382022-01-20 16:04:39.138200'
			CCL_evaluations_dir33 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_2_2022-01-20 16:04:39.3892042022-01-20 16:04:39.389378'
			CCL_evaluations_dir34 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_3_2022-01-20 16:04:38.9156322022-01-20 16:04:38.915766'
			CCL_evaluations_dir35 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_4_2022-01-20 16:04:38.7216832022-01-20 16:04:38.721803'
		
		else:
			#0.01
			CCL_evaluations_dir11 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_0_2022-01-20 16:04:40.0593822022-01-20 16:04:40.059562'
			CCL_evaluations_dir12 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_1_2022-01-20 16:04:36.4496822022-01-20 16:04:36.449798'
			CCL_evaluations_dir13 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_2_2022-01-20 16:04:38.3681302022-01-20 16:04:38.368257'
			CCL_evaluations_dir14 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_3_2022-01-20 16:04:36.2393762022-01-20 16:04:36.239484'
			CCL_evaluations_dir15 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_4_2022-01-20 16:04:38.4762222022-01-20 16:04:38.476387'

			#0.001
			CCL_evaluations_dir21 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_0_2022-01-20 16:04:35.9743922022-01-20 16:04:35.974519'
			CCL_evaluations_dir22 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_1_2022-01-20 16:04:37.2322712022-01-20 16:04:37.232428'
			CCL_evaluations_dir23 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_2_2022-01-20 16:04:39.5153022022-01-20 16:04:39.515471'
			CCL_evaluations_dir24 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_3_2022-01-20 16:04:40.3176002022-01-20 16:04:40.317817'
			CCL_evaluations_dir25 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_4_2022-01-20 16:04:37.5537942022-01-20 16:04:37.553967'
	
			#0.0001
			CCL_evaluations_dir31 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_0_2022-01-09 17:05:47.8701432022-01-09 17:05:47.870514'
			CCL_evaluations_dir32 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_1_2022-01-09 19:30:13.5075892022-01-09 19:30:13.507738'
			CCL_evaluations_dir33 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_2_2022-01-09 22:32:42.5473522022-01-09 22:32:42.547460'
			CCL_evaluations_dir34 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_3_2022-01-10 01:33:13.2583532022-01-10 01:33:13.258533'
			CCL_evaluations_dir35 = results_dir + 'HalfCheetah-v3_results/TD3CP_HalfCheetah-v3_4_2022-01-10 05:14:26.4863192022-01-10 05:14:26.486556'
	
			###########################

		CCL_evaluations_dir1 = \
									[CCL_evaluations_dir11, CCL_evaluations_dir12, \
										CCL_evaluations_dir13, CCL_evaluations_dir14, '0.01']

		CCL_evaluations_dir2 = \
									[CCL_evaluations_dir21, CCL_evaluations_dir22, \
										CCL_evaluations_dir23, CCL_evaluations_dir24,	'1e-3']

		CCL_evaluations_dir3 = \
									[CCL_evaluations_dir31, CCL_evaluations_dir32, \
										CCL_evaluations_dir33, CCL_evaluations_dir34,	'1e-4']

		Expert6toTD3Cheetah_evaluations_dir = [('CCL-PQD', 'tab:green', 'o'), \
										CCL_evaluations_dir1, CCL_evaluations_dir2, \
										CCL_evaluations_dir3]

		# CCL_evaluations_dir1 = \
		# 							[CCL_evaluations_dir11, CCL_evaluations_dir12, \
		# 								CCL_evaluations_dir13, CCL_evaluations_dir14, '0.01']

		# Expert6toTD3Cheetah_evaluations_dir = [('CCL PQD Clipping', 'tab:green'), \
		# 								CCL_evaluations_dir1]
		# ##################################################################
		# ##################################################################
		if is_4000:

			ExperttoTD3Cheetah_evaluations_dir1 = results_dir + 'HalfCheetah-v3_results/TD3_HalfCheetah-v3_4_2021-12-24 06:58:37.6312812021-12-24 06:58:37.631397'
			ExperttoTD3Cheetah_evaluations_dir2 = results_dir + 'HalfCheetah-v3_results/TD3_HalfCheetah-v3_1_2021-12-24 00:09:17.8000022021-12-24 00:09:17.800097'
			ExperttoTD3Cheetah_evaluations_dir3 = results_dir + 'HalfCheetah-v3_results/TD3_HalfCheetah-v3_2_2021-12-24 02:38:42.1222522021-12-24 02:38:42.122389'
			ExperttoTD3Cheetah_evaluations_dir4 = results_dir + 'HalfCheetah-v3_results/TD3_HalfCheetah-v3_3_2021-12-24 04:46:30.8405012021-12-24 04:46:30.840632'

		else:

			ExperttoTD3Cheetah_evaluations_dir1 = results_dir + 'HalfCheetah-v3_results/TD3_HalfCheetah-v3_0_2021-11-29 23:21:26.3488922021-11-29 23:21:26.348994'
			ExperttoTD3Cheetah_evaluations_dir2 = results_dir + 'HalfCheetah-v3_results/TD3_HalfCheetah-v3_1_2021-11-30 01:43:50.4262522021-11-30 01:43:50.426349'
			ExperttoTD3Cheetah_evaluations_dir3 = results_dir + 'HalfCheetah-v3_results/TD3_HalfCheetah-v3_2_2021-11-30 04:13:18.8107842021-11-30 04:13:18.811053'
			ExperttoTD3Cheetah_evaluations_dir4 = results_dir + 'HalfCheetah-v3_results/TD3_HalfCheetah-v3_3_2021-11-30 06:37:03.3265092021-11-30 06:37:03.326855'
							
		ExperttoTD3Cheetah_dir = \
									[ExperttoTD3Cheetah_evaluations_dir1, ExperttoTD3Cheetah_evaluations_dir2, \
										ExperttoTD3Cheetah_evaluations_dir3, ExperttoTD3Cheetah_evaluations_dir4, 'WS']

		Expert7toTD3Cheetah_evaluations_dir = [('Warm-Start', 'tab:purple', '^'), ExperttoTD3Cheetah_dir]

		# ##################################################################
		# ##################################################################
		method_evaluations = [Expert1toTD3Cheetah_evaluations_dir, Expert2toTD3Cheetah_evaluations_dir, \
																	Expert4toTD3Cheetah_evaluations_dir, \
								Expert5toTD3Cheetah_evaluations_dir, Expert6toTD3Cheetah_evaluations_dir, \
								Expert7toTD3Cheetah_evaluations_dir]

								# Expert3toTD3Cheetah_evaluations_dir, Expert4toTD3Cheetah_evaluations_dir, \
		# plt.title('Cheetah ExperttoTD3 learning rate')



		# plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
		texts = []
		Xs = []
		Ys = []
		# plt.style.use('ggplot')

		for method_evaluation in method_evaluations:
			(method_name, color, marker) = method_evaluation[0]
			for i, evaluation_dir in enumerate(method_evaluation[1:]):
				
				evaluations_dir1 = evaluation_dir[0]
				evaluations_dir2 = evaluation_dir[1]
				evaluations_dir3 = evaluation_dir[2]
				evaluations_dir4 = evaluation_dir[3]
				alpha = evaluation_dir[4]

				for filename in os.listdir(evaluations_dir1):
					print(filename)
					if filename.startswith('evaluations'):
						ExperttoTD3Cheetah_evaluations1=(np.load(\
							os.path.join(evaluations_dir1,filename), allow_pickle=True))

				for filename in os.listdir(evaluations_dir2):
					print(filename)
					if filename.startswith('evaluations'):
						ExperttoTD3Cheetah_evaluations2=(np.load(\
							os.path.join(evaluations_dir2,filename), allow_pickle=True))

				for filename in os.listdir(evaluations_dir3):
					print(filename)
					if filename.startswith('evaluations'):
						ExperttoTD3Cheetah_evaluations3=(np.load(\
							os.path.join(evaluations_dir3,filename), allow_pickle=True))

				for filename in os.listdir(evaluations_dir4):
					print(filename)
					if filename.startswith('evaluations'):
						ExperttoTD3Cheetah_evaluations4=(np.load(\
							os.path.join(evaluations_dir4,filename), allow_pickle=True))


				ExperttoTD3Cheetah_eval1 = ExperttoTD3Cheetah_evaluations1[:,1]
				ExperttoTD3Cheetah_eval1_range = ExperttoTD3Cheetah_evaluations1[:,0]

				ExperttoTD3Cheetah_eval2 = ExperttoTD3Cheetah_evaluations2[:,1]
				ExperttoTD3Cheetah_eval2_range = ExperttoTD3Cheetah_evaluations2[:,0]

				ExperttoTD3Cheetah_eval3 = ExperttoTD3Cheetah_evaluations3[:,1]
				ExperttoTD3Cheetah_eval3_range = ExperttoTD3Cheetah_evaluations3[:,0]

				ExperttoTD3Cheetah_eval4 = ExperttoTD3Cheetah_evaluations4[:,1]
				ExperttoTD3Cheetah_eval4_range = ExperttoTD3Cheetah_evaluations4[:,0]

				ExperttoTD3Cheetah_evals = np.array([ExperttoTD3Cheetah_eval1, ExperttoTD3Cheetah_eval2, \
											ExperttoTD3Cheetah_eval3, ExperttoTD3Cheetah_eval4])

				ExperttoTD3Cheetah_mean = np.mean(ExperttoTD3Cheetah_evals,axis=0)

				#max drop
				max_drop = ExperttoTD3Cheetah_mean[0]-np.min(ExperttoTD3Cheetah_mean)
				max_drop *= -1
				#final performance
				# final_performance = ExperttoTD3Cheetah_mean[-1]
				final_performance = np.max(ExperttoTD3Cheetah_mean)

				# x = np.linspace(0, 5000, 1000)
				# y = np.linspace(0, 5000, 1000)

				# plt.plot(x, y, color='k')
				plt.xlabel('max drop', fontsize=15)
				# plt.ylabel('final_performance')
				plt.ylabel('max performance', fontsize=15)



				plt.scatter(max_drop, final_performance, color=color, marker=marker)

				# plt.annotate(alpha, (max_drop, final_performance), fontsize=11)
				# plt.text(max_drop, final_performance, alpha)
				texts.append(plt.text(max_drop, final_performance, alpha, fontsize=14))
				Xs.append(max_drop)
				Ys.append(final_performance)

				if i == 0:
					plt.scatter(max_drop, final_performance, color=color, label=method_name, marker=marker)

		# plt.gca().invert_yaxis()
		if is_4000:
			plt.xlim([-5000, 1000])

			ppo_max_drop = -441.5
			ppo_final_performance = 6397


			# plt.ylim([4000, 11000])
			# plt.legend(loc='lower right')
			plt.title('HalfCheetah 4K Expert', fontsize=15)
			file_name = 'Cheetah ExperttoTD3 Constraint Compare4000.png'

			plt.scatter(ppo_max_drop, ppo_final_performance, color='tab:orange', marker='d',label='PPO')
			texts.append(plt.text(ppo_max_drop, ppo_final_performance, 'PPO', fontsize=14))
			Xs.append(ppo_max_drop)
			Ys.append(ppo_final_performance)

			plt.legend(loc='lower left', fontsize=13,labelspacing=0.05)
		else:
			ppo_max_drop=-1667.9042914598458

			ppo_final_performance=10200.48596471069

			# plt.legend(loc='upper right', fontsize=13)
			plt.title('HalfCheetah 10K Expert', fontsize=15)
			# plt.legend(fontsize=15)
			file_name = 'Cheetah ExperttoTD3 Constraint Compare10000.png'

			plt.scatter(ppo_max_drop, ppo_final_performance, color='tab:orange', marker='d',label='PPO')
			texts.append(plt.text(ppo_max_drop, ppo_final_performance, 'PPO', fontsize=14))
			Xs.append(ppo_max_drop)
			Ys.append(ppo_final_performance)
			plt.legend(fontsize=13, ncol=2,columnspacing=0.2,labelspacing=0.05, handletextpad=0.2)



		# Find lowest values for cost and highest for savings
		p_front = self.pareto_frontier(Xs, Ys, maxX = True, maxY = True) 
		# Then plot the Pareto frontier on top
		plt.plot(p_front[0], p_front[1])


		adjust_text(texts)
		# plt.savefig('Cheetah ExperttoTD3 learning rate.png')
		
		plt.savefig(file_name, bbox_inches = 'tight')
		# plt.savefig(file_name)

		plt.close()
		##################################################################

	'''
	Method to take two equally-sized lists and return just the elements which lie 
	on the Pareto frontier, sorted into order.
	Default behaviour is to find the maximum for both X and Y, but the option is
	available to specify maxX = False or maxY = False to find the minimum for either
	or both of the parameters.
	'''
	def pareto_frontier(self, Xs, Ys, maxX = True, maxY = True):
		# Sort the list in either ascending or descending order of X
		myList = sorted([[Xs[i], Ys[i]] for i in range(len(Xs))], reverse=maxX)
		# Start the Pareto frontier with the first value in the sorted list
		p_front = [myList[0]]    
		# Loop through the sorted list
		for pair in myList[1:]:
			if maxY: 
				if pair[1] >= p_front[-1][1]: # Look for higher values of Y…
					p_front.append(pair) # … and add them to the Pareto frontier
			else:
				if pair[1] <= p_front[-1][1]: # Look for lower values of Y…
					p_front.append(pair) # … and add them to the Pareto frontier
		# Turn resulting pairs back into a list of Xs and Ys
		p_frontX = [pair[0] for pair in p_front]
		p_frontY = [pair[1] for pair in p_front]
		return p_frontX, p_frontY
if __name__ == "__main__":
	

	dg = DrawGraphs()

	dg.draw(True)
	dg.draw()