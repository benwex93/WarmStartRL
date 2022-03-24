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
			ExperttoTD3Hopper_evaluations_dir11 = results_dir + 'Hopper-v3_results/TD3_BC_Pertubation_Hopper-v3_0_2022-01-27 21:38:54.1416202022-01-27 21:38:54.141709'
			ExperttoTD3Hopper_evaluations_dir12 = results_dir + 'Hopper-v3_results/TD3_BC_Pertubation_Hopper-v3_0_2022-01-27 21:38:54.1416202022-01-27 21:38:54.141709'
			ExperttoTD3Hopper_evaluations_dir13 = results_dir + 'Hopper-v3_results/TD3_BC_Pertubation_Hopper-v3_0_2022-01-27 21:38:54.1416202022-01-27 21:38:54.141709'
			ExperttoTD3Hopper_evaluations_dir14 = results_dir + 'Hopper-v3_results/TD3_BC_Pertubation_Hopper-v3_0_2022-01-27 21:38:54.1416202022-01-27 21:38:54.141709'
			#alpha: 0.1
			ExperttoTD3Hopper_evaluations_dir21 = results_dir + 'Hopper-v3_results/TD3_BC_Pertubation_Hopper-v3_0_2022-01-27 21:38:54.4309512022-01-27 21:38:54.431040'
			ExperttoTD3Hopper_evaluations_dir22 = results_dir + 'Hopper-v3_results/TD3_BC_Pertubation_Hopper-v3_0_2022-01-27 21:38:54.4309512022-01-27 21:38:54.431040'
			ExperttoTD3Hopper_evaluations_dir23 = results_dir + 'Hopper-v3_results/TD3_BC_Pertubation_Hopper-v3_0_2022-01-27 21:38:54.4309512022-01-27 21:38:54.431040'
			ExperttoTD3Hopper_evaluations_dir24 = results_dir + 'Hopper-v3_results/TD3_BC_Pertubation_Hopper-v3_0_2022-01-27 21:38:54.4309512022-01-27 21:38:54.431040'
			#alpha: 0.2
			ExperttoTD3Hopper_evaluations_dir31 = results_dir + 'Hopper-v3_results/TD3_BC_Pertubation_Hopper-v3_0_2022-01-27 21:38:49.6913852022-01-27 21:38:49.691814'
			ExperttoTD3Hopper_evaluations_dir32 = results_dir + 'Hopper-v3_results/TD3_BC_Pertubation_Hopper-v3_0_2022-01-27 21:38:49.6913852022-01-27 21:38:49.691814'
			ExperttoTD3Hopper_evaluations_dir33 = results_dir + 'Hopper-v3_results/TD3_BC_Pertubation_Hopper-v3_0_2022-01-27 21:38:49.6913852022-01-27 21:38:49.691814'
			ExperttoTD3Hopper_evaluations_dir34 = results_dir + 'Hopper-v3_results/TD3_BC_Pertubation_Hopper-v3_0_2022-01-27 21:38:49.6913852022-01-27 21:38:49.691814'
			#alpha: 0.25
			ExperttoTD3Hopper_evaluations_dir41 = results_dir + 'Hopper-v3_results/TD3_BC_Pertubation_Hopper-v3_0_2022-01-27 21:38:53.9856742022-01-27 21:38:53.985757'
			ExperttoTD3Hopper_evaluations_dir42 = results_dir + 'Hopper-v3_results/TD3_BC_Pertubation_Hopper-v3_0_2022-01-27 21:38:53.9856742022-01-27 21:38:53.985757'
			ExperttoTD3Hopper_evaluations_dir43 = results_dir + 'Hopper-v3_results/TD3_BC_Pertubation_Hopper-v3_0_2022-01-27 21:38:53.9856742022-01-27 21:38:53.985757'
			ExperttoTD3Hopper_evaluations_dir44 = results_dir + 'Hopper-v3_results/TD3_BC_Pertubation_Hopper-v3_0_2022-01-27 21:38:53.9856742022-01-27 21:38:53.985757'
			#alpha: 1
			ExperttoTD3Hopper_evaluations_dir51 = results_dir + 'Hopper-v3_results/TD3_BC_Pertubation_Hopper-v3_0_2022-01-27 21:38:54.6397872022-01-27 21:38:54.639875'
			ExperttoTD3Hopper_evaluations_dir52 = results_dir + 'Hopper-v3_results/TD3_BC_Pertubation_Hopper-v3_0_2022-01-27 21:38:54.6397872022-01-27 21:38:54.639875'
			ExperttoTD3Hopper_evaluations_dir53 = results_dir + 'Hopper-v3_results/TD3_BC_Pertubation_Hopper-v3_0_2022-01-27 21:38:54.6397872022-01-27 21:38:54.639875'
			ExperttoTD3Hopper_evaluations_dir54 = results_dir + 'Hopper-v3_results/TD3_BC_Pertubation_Hopper-v3_0_2022-01-27 21:38:54.6397872022-01-27 21:38:54.639875'

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
			ExperttoTD3Hopper_evaluations_dir11 = results_dir + 'Hopper-v3_results/TD3_BC_Constraint_Hopper-v3_0_2022-01-27 23:33:24.7529012022-01-27 23:33:24.758375'
			ExperttoTD3Hopper_evaluations_dir12 = results_dir + 'Hopper-v3_results/TD3_BC_Constraint_Hopper-v3_0_2022-01-27 23:33:24.7529012022-01-27 23:33:24.758375'
			ExperttoTD3Hopper_evaluations_dir13 = results_dir + 'Hopper-v3_results/TD3_BC_Constraint_Hopper-v3_0_2022-01-27 23:33:24.7529012022-01-27 23:33:24.758375'
			ExperttoTD3Hopper_evaluations_dir14 = results_dir + 'Hopper-v3_results/TD3_BC_Constraint_Hopper-v3_0_2022-01-27 23:33:24.7529012022-01-27 23:33:24.758375'
			#alpha: 0.01
			ExperttoTD3Hopper_evaluations_dir21 = results_dir + 'Hopper-v3_results/TD3_BC_Constraint_Hopper-v3_0_2022-01-28 05:38:19.2284132022-01-28 05:38:19.228531'
			ExperttoTD3Hopper_evaluations_dir22 = results_dir + 'Hopper-v3_results/TD3_BC_Constraint_Hopper-v3_0_2022-01-28 05:38:19.2284132022-01-28 05:38:19.228531'
			ExperttoTD3Hopper_evaluations_dir23 = results_dir + 'Hopper-v3_results/TD3_BC_Constraint_Hopper-v3_0_2022-01-28 05:38:19.2284132022-01-28 05:38:19.228531'
			ExperttoTD3Hopper_evaluations_dir24 = results_dir + 'Hopper-v3_results/TD3_BC_Constraint_Hopper-v3_0_2022-01-28 05:38:19.2284132022-01-28 05:38:19.228531'
			#alpha: 0.1
			ExperttoTD3Hopper_evaluations_dir31 = results_dir + 'Hopper-v3_results/TD3_BC_Constraint_Hopper-v3_0_2022-01-28 11:05:33.9160272022-01-28 11:05:33.916143'
			ExperttoTD3Hopper_evaluations_dir32 = results_dir + 'Hopper-v3_results/TD3_BC_Constraint_Hopper-v3_0_2022-01-28 11:05:33.9160272022-01-28 11:05:33.916143'
			ExperttoTD3Hopper_evaluations_dir33 = results_dir + 'Hopper-v3_results/TD3_BC_Constraint_Hopper-v3_0_2022-01-28 11:05:33.9160272022-01-28 11:05:33.916143'
			ExperttoTD3Hopper_evaluations_dir34 = results_dir + 'Hopper-v3_results/TD3_BC_Constraint_Hopper-v3_0_2022-01-28 11:05:33.9160272022-01-28 11:05:33.916143'
			#alpha: 0.5
			ExperttoTD3Hopper_evaluations_dir41 = results_dir + 'Hopper-v3_results/TD3_BC_Constraint_Hopper-v3_0_2022-01-28 16:41:19.8200982022-01-28 16:41:19.820241'
			ExperttoTD3Hopper_evaluations_dir42 = results_dir + 'Hopper-v3_results/TD3_BC_Constraint_Hopper-v3_0_2022-01-28 16:41:19.8200982022-01-28 16:41:19.820241'
			ExperttoTD3Hopper_evaluations_dir43 = results_dir + 'Hopper-v3_results/TD3_BC_Constraint_Hopper-v3_0_2022-01-28 16:41:19.8200982022-01-28 16:41:19.820241'
			ExperttoTD3Hopper_evaluations_dir44 = results_dir + 'Hopper-v3_results/TD3_BC_Constraint_Hopper-v3_0_2022-01-28 16:41:19.8200982022-01-28 16:41:19.820241'
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

		Expert2toTD3Hopper_evaluations_dir = [('BC Constraint', 'tab:blue', 'v'), \
										ExperttoTD3Hopper_evaluations_dir1, ExperttoTD3Hopper_evaluations_dir2, \
										ExperttoTD3Hopper_evaluations_dir3, ExperttoTD3Hopper_evaluations_dir4]
		# ###########################		

		# #LEARNING RATE
		# # ###########4000
		if is_4000:
			#lr: 3e-7
			ExperttoTD3Hopper_evaluations_dir11 = results_dir + 'Hopper-v3_results/TD3_learning_rate_Hopper-v3_1_2022-01-27 12:18:29.8385812022-01-27 12:18:29.838678'
			ExperttoTD3Hopper_evaluations_dir12 = results_dir + 'Hopper-v3_results/TD3_learning_rate_Hopper-v3_1_2022-01-27 12:18:29.8385812022-01-27 12:18:29.838678'
			ExperttoTD3Hopper_evaluations_dir13 = results_dir + 'Hopper-v3_results/TD3_learning_rate_Hopper-v3_1_2022-01-27 12:18:29.8385812022-01-27 12:18:29.838678'
			ExperttoTD3Hopper_evaluations_dir14 = results_dir + 'Hopper-v3_results/TD3_learning_rate_Hopper-v3_1_2022-01-27 12:18:29.8385812022-01-27 12:18:29.838678'
			#lr: 3e-6
			ExperttoTD3Hopper_evaluations_dir21 = results_dir + 'Hopper-v3_results/TD3_learning_rate_Hopper-v3_1_2022-01-27 12:18:30.0688412022-01-27 12:18:30.068943'
			ExperttoTD3Hopper_evaluations_dir22 = results_dir + 'Hopper-v3_results/TD3_learning_rate_Hopper-v3_1_2022-01-27 12:18:30.0688412022-01-27 12:18:30.068943'
			ExperttoTD3Hopper_evaluations_dir23 = results_dir + 'Hopper-v3_results/TD3_learning_rate_Hopper-v3_1_2022-01-27 12:18:30.0688412022-01-27 12:18:30.068943'
			ExperttoTD3Hopper_evaluations_dir24 = results_dir + 'Hopper-v3_results/TD3_learning_rate_Hopper-v3_1_2022-01-27 12:18:30.0688412022-01-27 12:18:30.068943'
			#lr: 3e-5
			ExperttoTD3Hopper_evaluations_dir31 = results_dir + 'Hopper-v3_results/TD3_learning_rate_Hopper-v3_1_2022-01-27 12:18:29.6216722022-01-27 12:18:29.622713'
			ExperttoTD3Hopper_evaluations_dir32 = results_dir + 'Hopper-v3_results/TD3_learning_rate_Hopper-v3_1_2022-01-27 12:18:29.6216722022-01-27 12:18:29.622713'
			ExperttoTD3Hopper_evaluations_dir33 = results_dir + 'Hopper-v3_results/TD3_learning_rate_Hopper-v3_1_2022-01-27 12:18:29.6216722022-01-27 12:18:29.622713'
			ExperttoTD3Hopper_evaluations_dir34 = results_dir + 'Hopper-v3_results/TD3_learning_rate_Hopper-v3_1_2022-01-27 12:18:29.6216722022-01-27 12:18:29.622713'
			#lr: 3e-4
			ExperttoTD3Hopper_evaluations_dir41 = results_dir + 'Hopper-v3_results/TD3_learning_rate_Hopper-v3_1_2022-01-27 12:18:29.6216262022-01-27 12:18:29.622708'
			ExperttoTD3Hopper_evaluations_dir42 = results_dir + 'Hopper-v3_results/TD3_learning_rate_Hopper-v3_1_2022-01-27 12:18:29.6216262022-01-27 12:18:29.622708'
			ExperttoTD3Hopper_evaluations_dir43 = results_dir + 'Hopper-v3_results/TD3_learning_rate_Hopper-v3_1_2022-01-27 12:18:29.6216262022-01-27 12:18:29.622708'
			ExperttoTD3Hopper_evaluations_dir44 = results_dir + 'Hopper-v3_results/TD3_learning_rate_Hopper-v3_1_2022-01-27 12:18:29.6216262022-01-27 12:18:29.622708'
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
										ExperttoTD3Hopper_evaluations_dir1, ExperttoTD3Hopper_evaluations_dir2, \
										ExperttoTD3Hopper_evaluations_dir3, ExperttoTD3Hopper_evaluations_dir4]
		# # ###########################

		# #GRADIENT CLIPPING
		# # # ############4000
		if is_4000:
			#gradient: 3e-9
			ExperttoTD3Hopper_evaluations_dir11 = results_dir + 'Hopper-v3_results/TD3_gradient_clipping_Hopper-v3_1_2022-01-27 12:17:08.0671722022-01-27 12:17:08.067260'
			ExperttoTD3Hopper_evaluations_dir12 = results_dir + 'Hopper-v3_results/TD3_gradient_clipping_Hopper-v3_1_2022-01-27 12:17:08.0671722022-01-27 12:17:08.067260'
			ExperttoTD3Hopper_evaluations_dir13 = results_dir + 'Hopper-v3_results/TD3_gradient_clipping_Hopper-v3_1_2022-01-27 12:17:08.0671722022-01-27 12:17:08.067260'
			ExperttoTD3Hopper_evaluations_dir14 = results_dir + 'Hopper-v3_results/TD3_gradient_clipping_Hopper-v3_1_2022-01-27 12:17:08.0671722022-01-27 12:17:08.067260'
			#gradient: 3e-8
			ExperttoTD3Hopper_evaluations_dir21 = results_dir + 'Hopper-v3_results/TD3_gradient_clipping_Hopper-v3_1_2022-01-27 12:17:03.9368912022-01-27 12:17:03.937195'
			ExperttoTD3Hopper_evaluations_dir22 = results_dir + 'Hopper-v3_results/TD3_gradient_clipping_Hopper-v3_1_2022-01-27 12:17:03.9368912022-01-27 12:17:03.937195'
			ExperttoTD3Hopper_evaluations_dir23 = results_dir + 'Hopper-v3_results/TD3_gradient_clipping_Hopper-v3_1_2022-01-27 12:17:03.9368912022-01-27 12:17:03.937195'
			ExperttoTD3Hopper_evaluations_dir24 = results_dir + 'Hopper-v3_results/TD3_gradient_clipping_Hopper-v3_1_2022-01-27 12:17:03.9368912022-01-27 12:17:03.937195'
			#gradient: 3e-6
			ExperttoTD3Hopper_evaluations_dir31 = results_dir + 'Hopper-v3_results/TD3_gradient_clipping_Hopper-v3_1_2022-01-27 12:17:08.7078602022-01-27 12:17:08.707949'
			ExperttoTD3Hopper_evaluations_dir32 = results_dir + 'Hopper-v3_results/TD3_gradient_clipping_Hopper-v3_1_2022-01-27 12:17:08.7078602022-01-27 12:17:08.707949'
			ExperttoTD3Hopper_evaluations_dir33 = results_dir + 'Hopper-v3_results/TD3_gradient_clipping_Hopper-v3_1_2022-01-27 12:17:08.7078602022-01-27 12:17:08.707949'
			ExperttoTD3Hopper_evaluations_dir34 = results_dir + 'Hopper-v3_results/TD3_gradient_clipping_Hopper-v3_1_2022-01-27 12:17:08.7078602022-01-27 12:17:08.707949'
			#gradient: 3e-3
			ExperttoTD3Hopper_evaluations_dir41 = results_dir + 'Hopper-v3_results/TD3_gradient_clipping_Hopper-v3_1_2022-01-27 12:17:07.8814132022-01-27 12:17:07.881504'
			ExperttoTD3Hopper_evaluations_dir42 = results_dir + 'Hopper-v3_results/TD3_gradient_clipping_Hopper-v3_1_2022-01-27 12:17:07.8814132022-01-27 12:17:07.881504'
			ExperttoTD3Hopper_evaluations_dir43 = results_dir + 'Hopper-v3_results/TD3_gradient_clipping_Hopper-v3_1_2022-01-27 12:17:07.8814132022-01-27 12:17:07.881504'
			ExperttoTD3Hopper_evaluations_dir44 = results_dir + 'Hopper-v3_results/TD3_gradient_clipping_Hopper-v3_1_2022-01-27 12:17:07.8814132022-01-27 12:17:07.881504'
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
										ExperttoTD3Hopper_evaluations_dir1, ExperttoTD3Hopper_evaluations_dir2, \
										ExperttoTD3Hopper_evaluations_dir3, ExperttoTD3Hopper_evaluations_dir4]
		# ##################################################################
		# ##################################################################

		if is_4000:
			#0.01
			CCL_evaluations_dir11 = results_dir + 'Hopper-v3_results/TD3CP_Hopper-v3_0_2022-01-09 17:05:52.2413032022-01-09 17:05:52.241725'
			CCL_evaluations_dir12 = results_dir + 'Hopper-v3_results/TD3CP_Hopper-v3_1_2022-01-09 19:30:08.9340972022-01-09 19:30:08.934234'
			CCL_evaluations_dir13 = results_dir + 'Hopper-v3_results/TD3CP_Hopper-v3_2_2022-01-09 22:32:47.1933082022-01-09 22:32:47.193661'
			CCL_evaluations_dir14 = results_dir + 'Hopper-v3_results/TD3CP_Hopper-v3_3_2022-01-10 01:33:08.3446112022-01-10 01:33:08.344933'
			CCL_evaluations_dir15 = results_dir + 'Hopper-v3_results/TD3CP_Hopper-v3_4_2022-01-10 05:14:21.3675142022-01-10 05:14:21.367699'
		
			#0.001
			CCL_evaluations_dir21 = results_dir + 'Hopper-v3_results/TD3CCL_PQD_Hopper-v3_0_2022-01-27 21:32:34.6013632022-01-27 21:32:34.601490'
			CCL_evaluations_dir22 = results_dir + 'Hopper-v3_results/TD3CCL_PQD_Hopper-v3_0_2022-01-27 21:32:34.6013632022-01-27 21:32:34.601490'
			CCL_evaluations_dir23 = results_dir + 'Hopper-v3_results/TD3CCL_PQD_Hopper-v3_0_2022-01-27 21:32:34.6013632022-01-27 21:32:34.601490'
			CCL_evaluations_dir24 = results_dir + 'Hopper-v3_results/TD3CCL_PQD_Hopper-v3_0_2022-01-27 21:32:34.6013632022-01-27 21:32:34.601490'
			CCL_evaluations_dir25 = results_dir + 'Hopper-v3_results/TD3CCL_PQD_Hopper-v3_0_2022-01-27 21:32:34.6013632022-01-27 21:32:34.601490'
		
			#0.0001
			CCL_evaluations_dir31 = results_dir + 'Hopper-v3_results/TD3CCL_PQD_Hopper-v3_0_2022-01-27 21:32:39.1242362022-01-27 21:32:39.124328'
			CCL_evaluations_dir32 = results_dir + 'Hopper-v3_results/TD3CCL_PQD_Hopper-v3_0_2022-01-27 21:32:39.1242362022-01-27 21:32:39.124328'
			CCL_evaluations_dir33 = results_dir + 'Hopper-v3_results/TD3CCL_PQD_Hopper-v3_0_2022-01-27 21:32:39.1242362022-01-27 21:32:39.124328'
			CCL_evaluations_dir34 = results_dir + 'Hopper-v3_results/TD3CCL_PQD_Hopper-v3_0_2022-01-27 21:32:39.1242362022-01-27 21:32:39.124328'
			CCL_evaluations_dir35 = results_dir + 'Hopper-v3_results/TD3CCL_PQD_Hopper-v3_0_2022-01-27 21:32:39.1242362022-01-27 21:32:39.124328'
		

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
		method_evaluations = [Expert1toTD3Hopper_evaluations_dir, Expert2toTD3Hopper_evaluations_dir, \
																	Expert4toTD3Hopper_evaluations_dir, \
								Expert5toTD3Hopper_evaluations_dir, Expert6toTD3Hopper_evaluations_dir]

								# Expert3toTD3Hopper_evaluations_dir, Expert4toTD3Hopper_evaluations_dir, \
		# plt.title('Hopper ExperttoTD3 learning rate')



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
			plt.xlim([-5000, 1000])

			ppo_max_drop = -572
			ppo_final_performance = 3000


			# plt.ylim([4000, 11000])
			# plt.legend(loc='lower right')
			plt.title('Hopper 4000 Constraints Comparison', fontsize=15)
			file_name = 'Hopper ExperttoTD3 Constraint Compare4000.png'

			####
			plt.scatter(ppo_max_drop, ppo_final_performance, color='tab:orange', marker='d',label='PPO')
			texts.append(plt.text(ppo_max_drop, ppo_final_performance, 'PPO', fontsize=14))
			Xs.append(ppo_max_drop)
			Ys.append(ppo_final_performance)
			# ###

			plt.legend(loc='lower left', fontsize=13,labelspacing=0.05)
		else:
			ppo_max_drop=-1667.9042914598458

			ppo_final_performance=10200.48596471069

			# plt.legend(loc='upper right', fontsize=13)
			plt.title('Hopper 10000 Constraints Comparison', fontsize=15)
			# plt.legend(fontsize=15)
			file_name = 'Hopper ExperttoTD3 Constraint Compare10000.png'

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