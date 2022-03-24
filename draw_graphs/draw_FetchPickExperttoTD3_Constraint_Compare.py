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
			ExperttoTD3Hopper_evaluations_dir11 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Pertubation_FetchPickAndPlace-v1_1_2022-02-26 23:43:53.7193192022-02-26 23:43:53.719397'
			ExperttoTD3Hopper_evaluations_dir12 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Pertubation_FetchPickAndPlace-v1_2_2022-02-27 02:08:04.9026462022-02-27 02:08:04.902736'
			ExperttoTD3Hopper_evaluations_dir13 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Pertubation_FetchPickAndPlace-v1_3_2022-02-27 04:34:49.0365852022-02-27 04:34:49.036685'
			ExperttoTD3Hopper_evaluations_dir14 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Pertubation_FetchPickAndPlace-v1_4_2022-02-27 06:55:50.0001492022-02-27 06:55:50.000260'
			#alpha: 0.1
			ExperttoTD3Hopper_evaluations_dir21 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Pertubation_FetchPickAndPlace-v1_1_2022-02-26 23:43:53.9105472022-02-26 23:43:53.910634'
			ExperttoTD3Hopper_evaluations_dir22 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Pertubation_FetchPickAndPlace-v1_2_2022-02-27 02:08:01.6610242022-02-27 02:08:01.661428'
			ExperttoTD3Hopper_evaluations_dir23 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Pertubation_FetchPickAndPlace-v1_3_2022-02-27 04:34:45.4149962022-02-27 04:34:45.415106'
			ExperttoTD3Hopper_evaluations_dir24 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Pertubation_FetchPickAndPlace-v1_4_2022-02-27 06:55:49.8122712022-02-27 06:55:49.812352'
			#alpha: 0.2
			ExperttoTD3Hopper_evaluations_dir31 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Pertubation_FetchPickAndPlace-v1_1_2022-02-26 23:43:51.0825872022-02-26 23:43:51.083005'
			ExperttoTD3Hopper_evaluations_dir32 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Pertubation_FetchPickAndPlace-v1_2_2022-02-27 02:08:05.3563992022-02-27 02:08:05.356491'
			ExperttoTD3Hopper_evaluations_dir33 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Pertubation_FetchPickAndPlace-v1_3_2022-02-27 04:34:48.7930112022-02-27 04:34:48.793094'
			ExperttoTD3Hopper_evaluations_dir34 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Pertubation_FetchPickAndPlace-v1_4_2022-02-27 06:55:46.6617982022-02-27 06:55:46.661880'
			#alpha: 0.25
			ExperttoTD3Hopper_evaluations_dir41 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Pertubation_FetchPickAndPlace-v1_1_2022-02-26 23:43:53.3476502022-02-26 23:43:53.347732'
			ExperttoTD3Hopper_evaluations_dir42 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Pertubation_FetchPickAndPlace-v1_2_2022-02-27 02:08:04.7016052022-02-27 02:08:04.701698'
			ExperttoTD3Hopper_evaluations_dir43 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Pertubation_FetchPickAndPlace-v1_3_2022-02-27 04:34:48.6294002022-02-27 04:34:48.629485'
			ExperttoTD3Hopper_evaluations_dir44 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Pertubation_FetchPickAndPlace-v1_4_2022-02-27 06:55:50.4407122022-02-27 06:55:50.440820'
			#alpha: 1
			ExperttoTD3Hopper_evaluations_dir51 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Pertubation_FetchPickAndPlace-v1_1_2022-02-26 23:43:53.5021912022-02-26 23:43:53.502290'
			ExperttoTD3Hopper_evaluations_dir52 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Pertubation_FetchPickAndPlace-v1_2_2022-02-27 02:08:05.1066932022-02-27 02:08:05.106843'
			ExperttoTD3Hopper_evaluations_dir53 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Pertubation_FetchPickAndPlace-v1_3_2022-02-27 04:34:49.2369132022-02-27 04:34:49.237001'
			ExperttoTD3Hopper_evaluations_dir54 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Pertubation_FetchPickAndPlace-v1_4_2022-02-27 06:55:50.2548382022-02-27 06:55:50.254942'

		ExperttoTD3Hopper_evaluations_dir1 = \
									[ExperttoTD3Hopper_evaluations_dir11, ExperttoTD3Hopper_evaluations_dir12, \
										ExperttoTD3Hopper_evaluations_dir13, ExperttoTD3Hopper_evaluations_dir14, '0.01']

		ExperttoTD3Hopper_evaluations_dir2 = \
									[ExperttoTD3Hopper_evaluations_dir21, ExperttoTD3Hopper_evaluations_dir22, \
										ExperttoTD3Hopper_evaluations_dir23, ExperttoTD3Hopper_evaluations_dir24,	'0.1']

		ExperttoTD3Hopper_evaluations_dir3 = \
									[ExperttoTD3Hopper_evaluations_dir31, ExperttoTD3Hopper_evaluations_dir32, \
										ExperttoTD3Hopper_evaluations_dir33, ExperttoTD3Hopper_evaluations_dir34,	'0.2']

		ExperttoTD3Hopper_evaluations_dir4 = \
									[ExperttoTD3Hopper_evaluations_dir41, ExperttoTD3Hopper_evaluations_dir42, \
										ExperttoTD3Hopper_evaluations_dir43, ExperttoTD3Hopper_evaluations_dir44, '0.25']

		ExperttoTD3Hopper_evaluations_dir5 = \
									[ExperttoTD3Hopper_evaluations_dir51, ExperttoTD3Hopper_evaluations_dir52, \
										ExperttoTD3Hopper_evaluations_dir53, ExperttoTD3Hopper_evaluations_dir54,	'1.0']

		Expert1toTD3Hopper_evaluations_dir = \
									[('Perturbation Net', 'tab:red', 'x'), \
										ExperttoTD3Hopper_evaluations_dir1, ExperttoTD3Hopper_evaluations_dir2, \
										ExperttoTD3Hopper_evaluations_dir3, ExperttoTD3Hopper_evaluations_dir4]
										# ExperttoTD3Hopper_evaluations_dir3, ExperttoTD3Hopper_evaluations_dir4, \
										# ExperttoTD3Hopper_evaluations_dir5]


		# # ###########################

		# #BC CONSTRAINT
		# # ############4000
		if is_4000:
			#alpha: 0.0001
			ExperttoTD3Hopper_evaluations_dir11 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Constraint_FetchPickAndPlace-v1_1_2022-02-26 23:53:40.3713102022-02-26 23:53:40.371412'
			ExperttoTD3Hopper_evaluations_dir12 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Constraint_FetchPickAndPlace-v1_2_2022-02-27 01:54:32.1566992022-02-27 01:54:32.156774'
			ExperttoTD3Hopper_evaluations_dir13 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Constraint_FetchPickAndPlace-v1_3_2022-02-27 03:56:45.6372202022-02-27 03:56:45.637294'
			ExperttoTD3Hopper_evaluations_dir14 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Constraint_FetchPickAndPlace-v1_4_2022-02-27 05:57:01.3719452022-02-27 05:57:01.372023'
			#alpha: 0.01
			ExperttoTD3Hopper_evaluations_dir21 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Constraint_FetchPickAndPlace-v1_1_2022-02-26 23:53:40.1577732022-02-26 23:53:40.157857'
			ExperttoTD3Hopper_evaluations_dir22 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Constraint_FetchPickAndPlace-v1_2_2022-02-27 01:54:32.3209382022-02-27 01:54:32.321041'
			ExperttoTD3Hopper_evaluations_dir23 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Constraint_FetchPickAndPlace-v1_3_2022-02-27 03:56:42.4671682022-02-27 03:56:42.467253'
			ExperttoTD3Hopper_evaluations_dir24 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Constraint_FetchPickAndPlace-v1_4_2022-02-27 05:56:58.5318442022-02-27 05:56:58.531937'
			#alpha: 0.1
			ExperttoTD3Hopper_evaluations_dir31 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Constraint_FetchPickAndPlace-v1_1_2022-02-26 23:53:40.1273922022-02-26 23:53:40.128076'
			ExperttoTD3Hopper_evaluations_dir32 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Constraint_FetchPickAndPlace-v1_2_2022-02-27 01:54:32.5971922022-02-27 01:54:32.597268'
			ExperttoTD3Hopper_evaluations_dir33 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Constraint_FetchPickAndPlace-v1_3_2022-02-27 03:56:45.4600492022-02-27 03:56:45.460127'
			ExperttoTD3Hopper_evaluations_dir34 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Constraint_FetchPickAndPlace-v1_4_2022-02-27 05:57:01.7840922022-02-27 05:57:01.784206'
			#alpha: 0.5
			ExperttoTD3Hopper_evaluations_dir41 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Constraint_FetchPickAndPlace-v1_1_2022-02-26 23:53:40.6851242022-02-26 23:53:40.685225'
			ExperttoTD3Hopper_evaluations_dir42 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Constraint_FetchPickAndPlace-v1_2_2022-02-27 01:54:29.0922802022-02-27 01:54:29.092603'
			ExperttoTD3Hopper_evaluations_dir43 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Constraint_FetchPickAndPlace-v1_3_2022-02-27 03:56:45.8871002022-02-27 03:56:45.887179'
			ExperttoTD3Hopper_evaluations_dir44 = results_dir + 'FetchPickAndPlace-v1_results/TD3_BC_Constraint_FetchPickAndPlace-v1_4_2022-02-27 05:57:01.5516192022-02-27 05:57:01.551704'
			# fig_name = 'Hopper ExperttoTD3 BC Constraint4000.png'
			###########################

		ExperttoTD3Hopper_evaluations_dir1 = \
									[ExperttoTD3Hopper_evaluations_dir11, ExperttoTD3Hopper_evaluations_dir12, \
										ExperttoTD3Hopper_evaluations_dir13, ExperttoTD3Hopper_evaluations_dir14, '1e-4']

		ExperttoTD3Hopper_evaluations_dir2 = \
									[ExperttoTD3Hopper_evaluations_dir21, ExperttoTD3Hopper_evaluations_dir22, \
										ExperttoTD3Hopper_evaluations_dir23, ExperttoTD3Hopper_evaluations_dir24,	'0.01']

		ExperttoTD3Hopper_evaluations_dir3 = \
									[ExperttoTD3Hopper_evaluations_dir31, ExperttoTD3Hopper_evaluations_dir32, \
										ExperttoTD3Hopper_evaluations_dir33, ExperttoTD3Hopper_evaluations_dir34,	'0.1']

		ExperttoTD3Hopper_evaluations_dir4 = \
									[ExperttoTD3Hopper_evaluations_dir41, ExperttoTD3Hopper_evaluations_dir42, \
										ExperttoTD3Hopper_evaluations_dir43, ExperttoTD3Hopper_evaluations_dir44, '0.5']

		Expert2toTD3Hopper_evaluations_dir = [('BC Policy Penalty', 'tab:blue', 'v'), \
										ExperttoTD3Hopper_evaluations_dir1, ExperttoTD3Hopper_evaluations_dir2, \
										ExperttoTD3Hopper_evaluations_dir3, ExperttoTD3Hopper_evaluations_dir4]
		# ###########################		

		# #LEARNING RATE ()
		# # ###########4000
		if is_4000:
			#lr: 3e-7
			ExperttoTD3Hopper_evaluations_dir11 = results_dir + 'FetchPickAndPlace-v1_results/TD3_learning_rate_FetchPickAndPlace-v1_1_2022-02-26 23:31:47.8416452022-02-26 23:31:47.841721'
			ExperttoTD3Hopper_evaluations_dir12 = results_dir + 'FetchPickAndPlace-v1_results/TD3_learning_rate_FetchPickAndPlace-v1_2_2022-02-27 01:59:02.9382622022-02-27 01:59:02.938366'
			ExperttoTD3Hopper_evaluations_dir13 = results_dir + 'FetchPickAndPlace-v1_results/TD3_learning_rate_FetchPickAndPlace-v1_3_2022-02-27 04:25:38.7926832022-02-27 04:25:38.792780'
			ExperttoTD3Hopper_evaluations_dir14 = results_dir + 'FetchPickAndPlace-v1_results/TD3_learning_rate_FetchPickAndPlace-v1_4_2022-02-27 06:49:26.9115122022-02-27 06:49:26.911600'
			#lr: 3e-6
			ExperttoTD3Hopper_evaluations_dir21 = results_dir + 'FetchPickAndPlace-v1_results/TD3_learning_rate_FetchPickAndPlace-v1_1_2022-02-26 23:31:52.0560812022-02-26 23:31:52.056166'
			ExperttoTD3Hopper_evaluations_dir22 = results_dir + 'FetchPickAndPlace-v1_results/TD3_learning_rate_FetchPickAndPlace-v1_2_2022-02-27 01:59:02.4955822022-02-27 01:59:02.495670'
			ExperttoTD3Hopper_evaluations_dir23 = results_dir + 'FetchPickAndPlace-v1_results/TD3_learning_rate_FetchPickAndPlace-v1_3_2022-02-27 04:25:38.5923692022-02-27 04:25:38.592452'
			ExperttoTD3Hopper_evaluations_dir24 = results_dir + 'FetchPickAndPlace-v1_results/TD3_learning_rate_FetchPickAndPlace-v1_4_2022-02-27 06:49:26.7034072022-02-27 06:49:26.703489'
			#lr: 3e-5
			ExperttoTD3Hopper_evaluations_dir31 = results_dir + 'FetchPickAndPlace-v1_results/TD3_learning_rate_FetchPickAndPlace-v1_1_2022-02-26 23:31:51.8502872022-02-26 23:31:51.850376'
			ExperttoTD3Hopper_evaluations_dir32 = results_dir + 'FetchPickAndPlace-v1_results/TD3_learning_rate_FetchPickAndPlace-v1_2_2022-02-27 01:59:02.6962192022-02-27 01:59:02.696309'
			ExperttoTD3Hopper_evaluations_dir33 = results_dir + 'FetchPickAndPlace-v1_results/TD3_learning_rate_FetchPickAndPlace-v1_3_2022-02-27 04:25:39.0738402022-02-27 04:25:39.073933'
			ExperttoTD3Hopper_evaluations_dir34 = results_dir + 'FetchPickAndPlace-v1_results/TD3_learning_rate_FetchPickAndPlace-v1_4_2022-02-27 06:49:23.3394452022-02-27 06:49:23.339986'
			#lr: 3e-4
			ExperttoTD3Hopper_evaluations_dir41 = results_dir + 'FetchPickAndPlace-v1_results/TD3_learning_rate_FetchPickAndPlace-v1_1_2022-02-26 23:31:51.6700522022-02-26 23:31:51.670154'
			ExperttoTD3Hopper_evaluations_dir42 = results_dir + 'FetchPickAndPlace-v1_results/TD3_learning_rate_FetchPickAndPlace-v1_2_2022-02-27 01:58:59.0926192022-02-27 01:58:59.092722'
			ExperttoTD3Hopper_evaluations_dir43 = results_dir + 'FetchPickAndPlace-v1_results/TD3_learning_rate_FetchPickAndPlace-v1_3_2022-02-27 04:25:35.3883512022-02-27 04:25:35.388654'
			ExperttoTD3Hopper_evaluations_dir44 = results_dir + 'FetchPickAndPlace-v1_results/TD3_learning_rate_FetchPickAndPlace-v1_4_2022-02-27 06:49:27.1053632022-02-27 06:49:27.105454'
			###########################

		ExperttoTD3Hopper_evaluations_dir1 = \
									[ExperttoTD3Hopper_evaluations_dir11, ExperttoTD3Hopper_evaluations_dir12, \
										ExperttoTD3Hopper_evaluations_dir13, ExperttoTD3Hopper_evaluations_dir14, '3e-7']

		ExperttoTD3Hopper_evaluations_dir2 = \
									[ExperttoTD3Hopper_evaluations_dir21, ExperttoTD3Hopper_evaluations_dir22, \
										ExperttoTD3Hopper_evaluations_dir23, ExperttoTD3Hopper_evaluations_dir24,	'3e-6']

		ExperttoTD3Hopper_evaluations_dir3 = \
									[ExperttoTD3Hopper_evaluations_dir31, ExperttoTD3Hopper_evaluations_dir32, \
										ExperttoTD3Hopper_evaluations_dir33, ExperttoTD3Hopper_evaluations_dir34,	'3e-5']

		ExperttoTD3Hopper_evaluations_dir4 = \
									[ExperttoTD3Hopper_evaluations_dir41, ExperttoTD3Hopper_evaluations_dir42, \
										ExperttoTD3Hopper_evaluations_dir43, ExperttoTD3Hopper_evaluations_dir44, '3e-4']

		Expert4toTD3Hopper_evaluations_dir = [('Learning Rate', 'tab:olive', 's'), \
										ExperttoTD3Hopper_evaluations_dir1, ExperttoTD3Hopper_evaluations_dir2] \
										# ExperttoTD3Hopper_evaluations_dir3, ExperttoTD3Hopper_evaluations_dir4]
		# # ###########################

		# #GRADIENT CLIPPING
		# # # ############4000
		if is_4000:
			#gradient: 3e-9
			ExperttoTD3Hopper_evaluations_dir11 = results_dir + 'FetchPickAndPlace-v1_results/TD3_gradient_clipping_FetchPickAndPlace-v1_4_2022-02-27 07:02:42.7350312022-02-27 07:02:42.735126'
			ExperttoTD3Hopper_evaluations_dir12 = results_dir + 'FetchPickAndPlace-v1_results/TD3_gradient_clipping_FetchPickAndPlace-v1_1_2022-02-26 23:31:28.4605612022-02-26 23:31:28.460640'
			ExperttoTD3Hopper_evaluations_dir13 = results_dir + 'FetchPickAndPlace-v1_results/TD3_gradient_clipping_FetchPickAndPlace-v1_2_2022-02-27 01:59:29.2809342022-02-27 01:59:29.281016'
			ExperttoTD3Hopper_evaluations_dir14 = results_dir + 'FetchPickAndPlace-v1_results/TD3_gradient_clipping_FetchPickAndPlace-v1_3_2022-02-27 04:32:11.5378682022-02-27 04:32:11.537958'
			#gradient: 3e-8
			ExperttoTD3Hopper_evaluations_dir21 = results_dir + 'FetchPickAndPlace-v1_results/TD3_gradient_clipping_FetchPickAndPlace-v1_4_2022-02-27 07:02:42.5554102022-02-27 07:02:42.555725'
			ExperttoTD3Hopper_evaluations_dir22 = results_dir + 'FetchPickAndPlace-v1_results/TD3_gradient_clipping_FetchPickAndPlace-v1_1_2022-02-26 23:31:28.8881812022-02-26 23:31:28.888282'
			ExperttoTD3Hopper_evaluations_dir23 = results_dir + 'FetchPickAndPlace-v1_results/TD3_gradient_clipping_FetchPickAndPlace-v1_2_2022-02-27 01:59:33.0377222022-02-27 01:59:33.037836'
			ExperttoTD3Hopper_evaluations_dir24 = results_dir + 'FetchPickAndPlace-v1_results/TD3_gradient_clipping_FetchPickAndPlace-v1_3_2022-02-27 04:32:11.1596382022-02-27 04:32:11.160099'
			#gradient: 3e-6
			ExperttoTD3Hopper_evaluations_dir31 = results_dir + 'FetchPickAndPlace-v1_results/TD3_gradient_clipping_FetchPickAndPlace-v1_4_2022-02-27 07:02:42.9306312022-02-27 07:02:42.930725'
			ExperttoTD3Hopper_evaluations_dir32 = results_dir + 'FetchPickAndPlace-v1_results/TD3_gradient_clipping_FetchPickAndPlace-v1_1_2022-02-26 23:31:28.6689172022-02-26 23:31:28.669039'
			ExperttoTD3Hopper_evaluations_dir33 = results_dir + 'FetchPickAndPlace-v1_results/TD3_gradient_clipping_FetchPickAndPlace-v1_2_2022-02-27 01:59:33.2284882022-02-27 01:59:33.228599'
			ExperttoTD3Hopper_evaluations_dir34 = results_dir + 'FetchPickAndPlace-v1_results/TD3_gradient_clipping_FetchPickAndPlace-v1_3_2022-02-27 04:32:11.3566532022-02-27 04:32:11.356743'
			#gradient: 3e-3
			ExperttoTD3Hopper_evaluations_dir41 = results_dir + 'FetchPickAndPlace-v1_results/TD3_gradient_clipping_FetchPickAndPlace-v1_4_2022-02-27 07:02:39.5552612022-02-27 07:02:39.555383'
			ExperttoTD3Hopper_evaluations_dir42 = results_dir + 'FetchPickAndPlace-v1_results/TD3_gradient_clipping_FetchPickAndPlace-v1_1_2022-02-26 23:31:26.0074782022-02-26 23:31:26.008136'
			ExperttoTD3Hopper_evaluations_dir43 = results_dir + 'FetchPickAndPlace-v1_results/TD3_gradient_clipping_FetchPickAndPlace-v1_2_2022-02-27 01:59:33.4628702022-02-27 01:59:33.462966'
			ExperttoTD3Hopper_evaluations_dir44 = results_dir + 'FetchPickAndPlace-v1_results/TD3_gradient_clipping_FetchPickAndPlace-v1_3_2022-02-27 04:32:07.7453452022-02-27 04:32:07.745433'
			# ###########################

		ExperttoTD3Hopper_evaluations_dir1 = \
									[ExperttoTD3Hopper_evaluations_dir11, ExperttoTD3Hopper_evaluations_dir12, \
										ExperttoTD3Hopper_evaluations_dir13, ExperttoTD3Hopper_evaluations_dir14, '3e-9']

		ExperttoTD3Hopper_evaluations_dir2 = \
									[ExperttoTD3Hopper_evaluations_dir21, ExperttoTD3Hopper_evaluations_dir22, \
										ExperttoTD3Hopper_evaluations_dir23, ExperttoTD3Hopper_evaluations_dir24,	'3e-8']

		ExperttoTD3Hopper_evaluations_dir3 = \
									[ExperttoTD3Hopper_evaluations_dir31, ExperttoTD3Hopper_evaluations_dir32, \
										ExperttoTD3Hopper_evaluations_dir33, ExperttoTD3Hopper_evaluations_dir34,	'3e-6']

		ExperttoTD3Hopper_evaluations_dir4 = \
									[ExperttoTD3Hopper_evaluations_dir41, ExperttoTD3Hopper_evaluations_dir42, \
										ExperttoTD3Hopper_evaluations_dir43, ExperttoTD3Hopper_evaluations_dir44, '3e-3']

		Expert5toTD3Hopper_evaluations_dir = [('Gradient Clip', 'tab:pink', 'P'), \
										ExperttoTD3Hopper_evaluations_dir1, ExperttoTD3Hopper_evaluations_dir2]
										# , \
										# ExperttoTD3Hopper_evaluations_dir3, ExperttoTD3Hopper_evaluations_dir4]
		# ##################################################################
		# ##################################################################

		if is_4000:
			# alpha=0.01
			CCL_evaluations_dir11 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_0_2022-02-27 00:07:16.2669012022-02-27 00:07:16.267215'
			CCL_evaluations_dir12 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_1_2022-02-27 02:09:27.7487322022-02-27 02:09:27.748805'
			CCL_evaluations_dir13 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_2_2022-02-27 04:13:26.1045802022-02-27 04:13:26.104666'
			CCL_evaluations_dir14 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_3_2022-02-27 06:11:11.6969652022-02-27 06:11:11.697039'
			CCL_evaluations_dir15 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_4_2022-02-27 08:09:23.9029102022-02-27 08:09:23.902988'		
			
			# alpha=0.001
			CCL_evaluations_dir21 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_0_2022-02-27 00:07:18.7510262022-02-27 00:07:18.751101'
			CCL_evaluations_dir22 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_1_2022-02-27 02:09:27.5306242022-02-27 02:09:27.530701'
			CCL_evaluations_dir23 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_2_2022-02-27 04:13:28.4861802022-02-27 04:13:28.486457'
			CCL_evaluations_dir24 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_3_2022-02-27 06:11:08.1119882022-02-27 06:11:08.112073'
			CCL_evaluations_dir25 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_4_2022-02-27 08:09:23.6173892022-02-27 08:09:23.617461'

			# alpha=0.0001
			CCL_evaluations_dir31 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_0_2022-02-27 00:07:19.0476952022-02-27 00:07:19.047766'
			CCL_evaluations_dir32 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_1_2022-02-27 02:09:24.1677552022-02-27 02:09:24.167863'
			CCL_evaluations_dir33 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_2_2022-02-27 04:13:28.7291782022-02-27 04:13:28.729255'
			CCL_evaluations_dir34 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_3_2022-02-27 06:11:11.8853902022-02-27 06:11:11.885468'
			CCL_evaluations_dir35 = results_dir + 'FetchPickAndPlace-v1_results/TD3CCL_PQD_FetchPickAndPlace-v1_4_2022-02-27 08:09:20.0370842022-02-27 08:09:20.037174'
				

		CCL_evaluations_dir1 = \
									[CCL_evaluations_dir11, CCL_evaluations_dir12, \
										CCL_evaluations_dir13, CCL_evaluations_dir14, '0.01']

		CCL_evaluations_dir2 = \
									[CCL_evaluations_dir21, CCL_evaluations_dir22, \
										CCL_evaluations_dir23, CCL_evaluations_dir24,	'1e-3']

		CCL_evaluations_dir3 = \
									[CCL_evaluations_dir31, CCL_evaluations_dir32, \
										CCL_evaluations_dir33, CCL_evaluations_dir34,	'1e-4']

		Expert6toTD3Hopper_evaluations_dir = [('CCL-PQD', 'tab:green', 'o'), \
										CCL_evaluations_dir1, CCL_evaluations_dir2, \
										CCL_evaluations_dir3]

		# CCL_evaluations_dir1 = \
		# 							[CCL_evaluations_dir11, CCL_evaluations_dir12, \
		# 								CCL_evaluations_dir13, CCL_evaluations_dir14, '0.01']

		# Expert6toTD3Hopper_evaluations_dir = [('CCL PQD Clipping', 'tab:green'), \
		# 								CCL_evaluations_dir1]
		# ##################################################################
		# ##################################################################
		# method_evaluations = [Expert1toTD3Hopper_evaluations_dir, Expert2toTD3Hopper_evaluations_dir, \
		# 															Expert4toTD3Hopper_evaluations_dir, \
		# 						Expert5toTD3Hopper_evaluations_dir, Expert6toTD3Hopper_evaluations_dir]

								# Expert3toTD3Hopper_evaluations_dir, Expert4toTD3Hopper_evaluations_dir, \
		# plt.title('Hopper ExperttoTD3 learning rate')

		# CCL_evaluations_dir1 = \
		# 							[CCL_evaluations_dir11, CCL_evaluations_dir12, \
		# 								CCL_evaluations_dir13, CCL_evaluations_dir14, '0.01']

		# Expert6toTD3Hopper_evaluations_dir = [('CCL PQD Clipping', 'tab:green'), \
		# 								CCL_evaluations_dir1]

		if is_4000:
			ExperttoTD3Fetch_evaluations_dir1 = results_dir + 'FetchPickAndPlace-v1_results/TD3_FetchPickAndPlace-v1_0_2022-02-27 13:37:42.0553692022-02-27 13:37:42.055509'
			ExperttoTD3Fetch_evaluations_dir2 = results_dir + 'FetchPickAndPlace-v1_results/TD3_FetchPickAndPlace-v1_1_2022-02-27 13:37:41.0139052022-02-27 13:37:41.014213'
			ExperttoTD3Fetch_evaluations_dir3 = results_dir + 'FetchPickAndPlace-v1_results/TD3_FetchPickAndPlace-v1_2_2022-02-27 13:37:41.8403662022-02-27 13:37:41.840466'
			ExperttoTD3Fetch_evaluations_dir4 = results_dir + 'FetchPickAndPlace-v1_results/TD3_FetchPickAndPlace-v1_3_2022-02-27 13:37:41.5917212022-02-27 13:37:41.591849'
			ExperttoTD3Fetch_evaluations_dir5 = results_dir + 'FetchPickAndPlace-v1_results/TD3_FetchPickAndPlace-v1_4_2022-02-27 13:37:41.3900502022-02-27 13:37:41.390177'
		
		ExperttoTD3Fetch_dir = \
									[ExperttoTD3Fetch_evaluations_dir1, ExperttoTD3Fetch_evaluations_dir2, \
										ExperttoTD3Fetch_evaluations_dir3, ExperttoTD3Fetch_evaluations_dir4, 'WS']

		Expert7toTD3Fetch_evaluations_dir = [('Warm-Start', 'tab:purple', '^'), ExperttoTD3Fetch_dir]

		# ##################################################################
		# ##################################################################
		method_evaluations = [Expert1toTD3Hopper_evaluations_dir, Expert2toTD3Hopper_evaluations_dir, \
																	Expert4toTD3Hopper_evaluations_dir, \
								Expert5toTD3Hopper_evaluations_dir, Expert6toTD3Hopper_evaluations_dir, \
								Expert7toTD3Fetch_evaluations_dir]
		
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
						ExperttoTD3Hopper_evaluations1=(np.load(\
							os.path.join(evaluations_dir1,filename), allow_pickle=True))

				for filename in os.listdir(evaluations_dir2):
					print(filename)
					if filename.startswith('evaluations'):
						ExperttoTD3Hopper_evaluations2=(np.load(\
							os.path.join(evaluations_dir2,filename), allow_pickle=True))

				for filename in os.listdir(evaluations_dir3):
					print(filename)
					if filename.startswith('evaluations'):
						ExperttoTD3Hopper_evaluations3=(np.load(\
							os.path.join(evaluations_dir3,filename), allow_pickle=True))

				for filename in os.listdir(evaluations_dir4):
					print(filename)
					if filename.startswith('evaluations'):
						ExperttoTD3Hopper_evaluations4=(np.load(\
							os.path.join(evaluations_dir4,filename), allow_pickle=True))


				ExperttoTD3Hopper_eval1 = ExperttoTD3Hopper_evaluations1[:,1]
				ExperttoTD3Hopper_eval1_range = ExperttoTD3Hopper_evaluations1[:,0]

				ExperttoTD3Hopper_eval2 = ExperttoTD3Hopper_evaluations2[:,1]
				ExperttoTD3Hopper_eval2_range = ExperttoTD3Hopper_evaluations2[:,0]

				ExperttoTD3Hopper_eval3 = ExperttoTD3Hopper_evaluations3[:,1]
				ExperttoTD3Hopper_eval3_range = ExperttoTD3Hopper_evaluations3[:,0]

				ExperttoTD3Hopper_eval4 = ExperttoTD3Hopper_evaluations4[:,1]
				ExperttoTD3Hopper_eval4_range = ExperttoTD3Hopper_evaluations4[:,0]

				ExperttoTD3Hopper_evals = np.array([ExperttoTD3Hopper_eval1, ExperttoTD3Hopper_eval2, \
											ExperttoTD3Hopper_eval3, ExperttoTD3Hopper_eval4])

				ExperttoTD3Hopper_mean = np.mean(ExperttoTD3Hopper_evals,axis=0)

				#max drop
				max_drop = ExperttoTD3Hopper_mean[0]-np.min(ExperttoTD3Hopper_mean)
				max_drop *= -1
				#final performance
				# final_performance = ExperttoTD3Hopper_mean[-1]
				final_performance = np.max(ExperttoTD3Hopper_mean)

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
			# plt.xlim([-5000, 1000])

			ppo_max_drop = -10
			ppo_final_performance = 15


			# plt.ylim([4000, 11000])
			# plt.legend(loc='lower right')
			plt.title('Fetch PickAndPlace', fontsize=15)
			file_name = 'FetchPickAndPlace ExperttoTD3 Constraint Compare.png'

			# ####
			plt.scatter(ppo_max_drop, ppo_final_performance, color='tab:orange', marker='d',label='PPO')
			texts.append(plt.text(ppo_max_drop, ppo_final_performance, 'PPO', fontsize=14))
			Xs.append(ppo_max_drop)
			Ys.append(ppo_final_performance)
			# # ###
			plt.legend(fontsize=13, ncol=2,columnspacing=0.2,labelspacing=0.05, handletextpad=0.2)
			# plt.legend(fontsize=13,labelspacing=0.05)
			# plt.legend(loc='lower left', fontsize=13,labelspacing=0.05)
		else:
			ppo_max_drop=-1667.9042914598458

			ppo_final_performance=10200.48596471069

			# plt.legend(loc='upper right', fontsize=13)
			plt.title('FetchPickAndPlace Constraints Comparison', fontsize=15)
			# plt.legend(fontsize=15)
			file_name = 'FetchPickAndPlace ExperttoTD3 Constraint Compare.png'

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
		# plt.savefig('Hopper ExperttoTD3 learning rate.png')
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
	# dg.draw()