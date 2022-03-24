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
			ExperttoTD3Hopper_evaluations_dir11 = results_dir + 'FetchSlide-v1_results/TD3_BC_Pertubation_FetchSlide-v1_0_2022-02-25 13:49:25.1339402022-02-25 13:49:25.134048'
			ExperttoTD3Hopper_evaluations_dir12 = results_dir + 'FetchSlide-v1_results/TD3_BC_Pertubation_FetchSlide-v1_0_2022-02-25 13:49:25.1339402022-02-25 13:49:25.134048'
			ExperttoTD3Hopper_evaluations_dir13 = results_dir + 'FetchSlide-v1_results/TD3_BC_Pertubation_FetchSlide-v1_0_2022-02-25 13:49:25.1339402022-02-25 13:49:25.134048'
			ExperttoTD3Hopper_evaluations_dir14 = results_dir + 'FetchSlide-v1_results/TD3_BC_Pertubation_FetchSlide-v1_0_2022-02-25 13:49:25.1339402022-02-25 13:49:25.134048'
			#alpha: 0.1
			ExperttoTD3Hopper_evaluations_dir21 = results_dir + 'FetchSlide-v1_results/TD3_BC_Pertubation_FetchSlide-v1_0_2022-02-25 13:49:31.1462972022-02-25 13:49:31.146395'
			ExperttoTD3Hopper_evaluations_dir22 = results_dir + 'FetchSlide-v1_results/TD3_BC_Pertubation_FetchSlide-v1_0_2022-02-25 13:49:31.1462972022-02-25 13:49:31.146395'
			ExperttoTD3Hopper_evaluations_dir23 = results_dir + 'FetchSlide-v1_results/TD3_BC_Pertubation_FetchSlide-v1_0_2022-02-25 13:49:31.1462972022-02-25 13:49:31.146395'
			ExperttoTD3Hopper_evaluations_dir24 = results_dir + 'FetchSlide-v1_results/TD3_BC_Pertubation_FetchSlide-v1_0_2022-02-25 13:49:31.1462972022-02-25 13:49:31.146395'
			#alpha: 0.2
			ExperttoTD3Hopper_evaluations_dir31 = results_dir + 'FetchSlide-v1_results/TD3_BC_Pertubation_FetchSlide-v1_0_2022-02-25 13:49:30.6942732022-02-25 13:49:30.694410'
			ExperttoTD3Hopper_evaluations_dir32 = results_dir + 'FetchSlide-v1_results/TD3_BC_Pertubation_FetchSlide-v1_0_2022-02-25 13:49:30.6942732022-02-25 13:49:30.694410'
			ExperttoTD3Hopper_evaluations_dir33 = results_dir + 'FetchSlide-v1_results/TD3_BC_Pertubation_FetchSlide-v1_0_2022-02-25 13:49:30.6942732022-02-25 13:49:30.694410'
			ExperttoTD3Hopper_evaluations_dir34 = results_dir + 'FetchSlide-v1_results/TD3_BC_Pertubation_FetchSlide-v1_0_2022-02-25 13:49:30.6942732022-02-25 13:49:30.694410'
			#alpha: 0.25
			ExperttoTD3Hopper_evaluations_dir41 = results_dir + 'FetchSlide-v1_results/TD3_BC_Pertubation_FetchSlide-v1_0_2022-02-25 13:49:24.7961972022-02-25 13:49:24.796918'
			ExperttoTD3Hopper_evaluations_dir42 = results_dir + 'FetchSlide-v1_results/TD3_BC_Pertubation_FetchSlide-v1_0_2022-02-25 13:49:24.7961972022-02-25 13:49:24.796918'
			ExperttoTD3Hopper_evaluations_dir43 = results_dir + 'FetchSlide-v1_results/TD3_BC_Pertubation_FetchSlide-v1_0_2022-02-25 13:49:24.7961972022-02-25 13:49:24.796918'
			ExperttoTD3Hopper_evaluations_dir44 = results_dir + 'FetchSlide-v1_results/TD3_BC_Pertubation_FetchSlide-v1_0_2022-02-25 13:49:24.7961972022-02-25 13:49:24.796918'
			#alpha: 1
			ExperttoTD3Hopper_evaluations_dir51 = results_dir + 'FetchSlide-v1_results/TD3_BC_Pertubation_FetchSlide-v1_0_2022-02-25 13:49:36.1377952022-02-25 13:49:36.137881'
			ExperttoTD3Hopper_evaluations_dir52 = results_dir + 'FetchSlide-v1_results/TD3_BC_Pertubation_FetchSlide-v1_0_2022-02-25 13:49:36.1377952022-02-25 13:49:36.137881'
			ExperttoTD3Hopper_evaluations_dir53 = results_dir + 'FetchSlide-v1_results/TD3_BC_Pertubation_FetchSlide-v1_0_2022-02-25 13:49:36.1377952022-02-25 13:49:36.137881'
			ExperttoTD3Hopper_evaluations_dir54 = results_dir + 'FetchSlide-v1_results/TD3_BC_Pertubation_FetchSlide-v1_0_2022-02-25 13:49:36.1377952022-02-25 13:49:36.137881'

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
			ExperttoTD3Hopper_evaluations_dir11 = results_dir + 'FetchSlide-v1_results/TD3_BC_Constraint_FetchSlide-v1_0_2022-02-25 13:41:05.6910062022-02-25 13:41:05.691098'
			ExperttoTD3Hopper_evaluations_dir12 = results_dir + 'FetchSlide-v1_results/TD3_BC_Constraint_FetchSlide-v1_0_2022-02-25 13:41:05.6910062022-02-25 13:41:05.691098'
			ExperttoTD3Hopper_evaluations_dir13 = results_dir + 'FetchSlide-v1_results/TD3_BC_Constraint_FetchSlide-v1_0_2022-02-25 13:41:05.6910062022-02-25 13:41:05.691098'
			ExperttoTD3Hopper_evaluations_dir14 = results_dir + 'FetchSlide-v1_results/TD3_BC_Constraint_FetchSlide-v1_0_2022-02-25 13:41:05.6910062022-02-25 13:41:05.691098'
			#alpha: 0.01
			ExperttoTD3Hopper_evaluations_dir21 = results_dir + 'FetchSlide-v1_results/TD3_BC_Constraint_FetchSlide-v1_0_2022-02-25 13:41:05.3795472022-02-25 13:41:05.380189'
			ExperttoTD3Hopper_evaluations_dir22 = results_dir + 'FetchSlide-v1_results/TD3_BC_Constraint_FetchSlide-v1_0_2022-02-25 13:41:05.3795472022-02-25 13:41:05.380189'
			ExperttoTD3Hopper_evaluations_dir23 = results_dir + 'FetchSlide-v1_results/TD3_BC_Constraint_FetchSlide-v1_0_2022-02-25 13:41:05.3795472022-02-25 13:41:05.380189'
			ExperttoTD3Hopper_evaluations_dir24 = results_dir + 'FetchSlide-v1_results/TD3_BC_Constraint_FetchSlide-v1_0_2022-02-25 13:41:05.3795472022-02-25 13:41:05.380189'
			#alpha: 0.1
			ExperttoTD3Hopper_evaluations_dir31 = results_dir + 'FetchSlide-v1_results/TD3_BC_Constraint_FetchSlide-v1_0_2022-02-25 13:41:11.6951432022-02-25 13:41:11.695280'
			ExperttoTD3Hopper_evaluations_dir32 = results_dir + 'FetchSlide-v1_results/TD3_BC_Constraint_FetchSlide-v1_0_2022-02-25 13:41:11.6951432022-02-25 13:41:11.695280'
			ExperttoTD3Hopper_evaluations_dir33 = results_dir + 'FetchSlide-v1_results/TD3_BC_Constraint_FetchSlide-v1_0_2022-02-25 13:41:11.6951432022-02-25 13:41:11.695280'
			ExperttoTD3Hopper_evaluations_dir34 = results_dir + 'FetchSlide-v1_results/TD3_BC_Constraint_FetchSlide-v1_0_2022-02-25 13:41:11.6951432022-02-25 13:41:11.695280'
			#alpha: 0.5
			ExperttoTD3Hopper_evaluations_dir41 = results_dir + 'FetchSlide-v1_results/TD3_BC_Constraint_FetchSlide-v1_0_2022-02-25 13:41:11.0272362022-02-25 13:41:11.027331'
			ExperttoTD3Hopper_evaluations_dir42 = results_dir + 'FetchSlide-v1_results/TD3_BC_Constraint_FetchSlide-v1_0_2022-02-25 13:41:11.0272362022-02-25 13:41:11.027331'
			ExperttoTD3Hopper_evaluations_dir43 = results_dir + 'FetchSlide-v1_results/TD3_BC_Constraint_FetchSlide-v1_0_2022-02-25 13:41:11.0272362022-02-25 13:41:11.027331'
			ExperttoTD3Hopper_evaluations_dir44 = results_dir + 'FetchSlide-v1_results/TD3_BC_Constraint_FetchSlide-v1_0_2022-02-25 13:41:11.0272362022-02-25 13:41:11.027331'
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

		# #LEARNING RATE
		# # ###########4000
		if is_4000:
			#lr: 3e-7
			ExperttoTD3Hopper_evaluations_dir11 = results_dir + 'FetchSlide-v1_results/TD3_learning_rate_FetchSlide-v1_1_2022-02-25 13:46:32.7782642022-02-25 13:46:32.778364'
			ExperttoTD3Hopper_evaluations_dir12 = results_dir + 'FetchSlide-v1_results/TD3_learning_rate_FetchSlide-v1_2_2022-02-25 16:28:54.2491392022-02-25 16:28:54.249212'
			ExperttoTD3Hopper_evaluations_dir13 = results_dir + 'FetchSlide-v1_results/TD3_learning_rate_FetchSlide-v1_3_2022-02-25 18:56:12.1371022022-02-25 18:56:12.137203'
			ExperttoTD3Hopper_evaluations_dir14 = results_dir + 'FetchSlide-v1_results/TD3_learning_rate_FetchSlide-v1_4_2022-02-25 21:21:56.4402782022-02-25 21:21:56.440369'
			#lr: 3e-6
			ExperttoTD3Hopper_evaluations_dir21 = results_dir + 'FetchSlide-v1_results/TD3_learning_rate_FetchSlide-v1_1_2022-02-25 13:46:32.4974752022-02-25 13:46:32.497758'
			ExperttoTD3Hopper_evaluations_dir22 = results_dir + 'FetchSlide-v1_results/TD3_learning_rate_FetchSlide-v1_2_2022-02-25 16:28:58.9487172022-02-25 16:28:58.948831'
			ExperttoTD3Hopper_evaluations_dir23 = results_dir + 'FetchSlide-v1_results/TD3_learning_rate_FetchSlide-v1_3_2022-02-25 18:56:29.4050292022-02-25 18:56:29.405109'
			ExperttoTD3Hopper_evaluations_dir24 = results_dir + 'FetchSlide-v1_results/TD3_learning_rate_FetchSlide-v1_4_2022-02-25 21:22:00.1298302022-02-25 21:22:00.130192'
			#lr: 3e-5
			ExperttoTD3Hopper_evaluations_dir31 = results_dir + 'FetchSlide-v1_results/TD3_learning_rate_FetchSlide-v1_1_2022-02-25 13:46:20.6605152022-02-25 13:46:20.660608'
			ExperttoTD3Hopper_evaluations_dir32 = results_dir + 'FetchSlide-v1_results/TD3_learning_rate_FetchSlide-v1_2_2022-02-25 16:28:41.4330402022-02-25 16:28:41.433138'
			ExperttoTD3Hopper_evaluations_dir33 = results_dir + 'FetchSlide-v1_results/TD3_learning_rate_FetchSlide-v1_3_2022-02-25 18:56:16.2909402022-02-25 18:56:16.291019'
			ExperttoTD3Hopper_evaluations_dir34 = results_dir + 'FetchSlide-v1_results/TD3_learning_rate_FetchSlide-v1_4_2022-02-25 21:22:00.4549402022-02-25 21:22:00.455032'
			#lr: 3e-4
			ExperttoTD3Hopper_evaluations_dir41 = results_dir + 'FetchSlide-v1_results/TD3_learning_rate_FetchSlide-v1_1_2022-02-25 13:46:24.6222662022-02-25 13:46:24.622348'
			ExperttoTD3Hopper_evaluations_dir42 = results_dir + 'FetchSlide-v1_results/TD3_learning_rate_FetchSlide-v1_2_2022-02-25 16:28:45.9116312022-02-25 16:28:45.911725'
			ExperttoTD3Hopper_evaluations_dir43 = results_dir + 'FetchSlide-v1_results/TD3_learning_rate_FetchSlide-v1_3_2022-02-25 18:56:21.2238032022-02-25 18:56:21.224253'
			ExperttoTD3Hopper_evaluations_dir44 = results_dir + 'FetchSlide-v1_results/TD3_learning_rate_FetchSlide-v1_4_2022-02-25 21:22:08.2756582022-02-25 21:22:08.275742'
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
			ExperttoTD3Hopper_evaluations_dir11 = results_dir + 'FetchSlide-v1_results/TD3_gradient_clipping_FetchSlide-v1_1_2022-02-27 15:30:56.5447342022-02-27 15:30:56.544837'
			ExperttoTD3Hopper_evaluations_dir12 = results_dir + 'FetchSlide-v1_results/TD3_gradient_clipping_FetchSlide-v1_1_2022-02-27 15:30:56.5447342022-02-27 15:30:56.544837'
			ExperttoTD3Hopper_evaluations_dir13 = results_dir + 'FetchSlide-v1_results/TD3_gradient_clipping_FetchSlide-v1_1_2022-02-27 15:30:56.5447342022-02-27 15:30:56.544837'
			ExperttoTD3Hopper_evaluations_dir14 = results_dir + 'FetchSlide-v1_results/TD3_gradient_clipping_FetchSlide-v1_1_2022-02-27 15:30:56.5447342022-02-27 15:30:56.544837'
			#gradient: 3e-8
			ExperttoTD3Hopper_evaluations_dir21 = results_dir + 'FetchSlide-v1_results/TD3_gradient_clipping_FetchSlide-v1_1_2022-02-27 15:30:56.6830212022-02-27 15:30:56.683111'
			ExperttoTD3Hopper_evaluations_dir22 = results_dir + 'FetchSlide-v1_results/TD3_gradient_clipping_FetchSlide-v1_1_2022-02-27 15:30:56.6830212022-02-27 15:30:56.683111'
			ExperttoTD3Hopper_evaluations_dir23 = results_dir + 'FetchSlide-v1_results/TD3_gradient_clipping_FetchSlide-v1_1_2022-02-27 15:30:56.6830212022-02-27 15:30:56.683111'
			ExperttoTD3Hopper_evaluations_dir24 = results_dir + 'FetchSlide-v1_results/TD3_gradient_clipping_FetchSlide-v1_1_2022-02-27 15:30:56.6830212022-02-27 15:30:56.683111'
			#gradient: 3e-6
			ExperttoTD3Hopper_evaluations_dir31 = results_dir + 'FetchSlide-v1_results/TD3_gradient_clipping_FetchSlide-v1_1_2022-02-27 15:30:54.0068312022-02-27 15:30:54.007378'
			ExperttoTD3Hopper_evaluations_dir32 = results_dir + 'FetchSlide-v1_results/TD3_gradient_clipping_FetchSlide-v1_1_2022-02-27 15:30:54.0068312022-02-27 15:30:54.007378'
			ExperttoTD3Hopper_evaluations_dir33 = results_dir + 'FetchSlide-v1_results/TD3_gradient_clipping_FetchSlide-v1_1_2022-02-27 15:30:54.0068312022-02-27 15:30:54.007378'
			ExperttoTD3Hopper_evaluations_dir34 = results_dir + 'FetchSlide-v1_results/TD3_gradient_clipping_FetchSlide-v1_1_2022-02-27 15:30:54.0068312022-02-27 15:30:54.007378'
			#gradient: 3e-3
			ExperttoTD3Hopper_evaluations_dir41 = results_dir + 'FetchSlide-v1_results/TD3_gradient_clipping_FetchSlide-v1_1_2022-02-27 15:30:56.2922982022-02-27 15:30:56.292395'
			ExperttoTD3Hopper_evaluations_dir42 = results_dir + 'FetchSlide-v1_results/TD3_gradient_clipping_FetchSlide-v1_1_2022-02-27 15:30:56.2922982022-02-27 15:30:56.292395'
			ExperttoTD3Hopper_evaluations_dir43 = results_dir + 'FetchSlide-v1_results/TD3_gradient_clipping_FetchSlide-v1_1_2022-02-27 15:30:56.2922982022-02-27 15:30:56.292395'
			ExperttoTD3Hopper_evaluations_dir44 = results_dir + 'FetchSlide-v1_results/TD3_gradient_clipping_FetchSlide-v1_1_2022-02-27 15:30:56.2922982022-02-27 15:30:56.292395'
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

			# alpha=0.01
			CCL_evaluations_dir11 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_0_2022-02-25 13:43:37.1231412022-02-25 13:43:37.123218'
			CCL_evaluations_dir12 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_1_2022-02-25 16:37:25.5898372022-02-25 16:37:25.589929'
			CCL_evaluations_dir13 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_2_2022-02-25 19:20:04.6730892022-02-25 19:20:04.673168'
			CCL_evaluations_dir14 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_3_2022-02-25 22:02:12.5018952022-02-25 22:02:12.501992'
			CCL_evaluations_dir15 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_4_2022-02-26 00:47:04.7317882022-02-26 00:47:04.732108'
					
			# alpha=0.001
			CCL_evaluations_dir21 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_0_2022-02-25 13:43:24.7503682022-02-25 13:43:24.750601'
			CCL_evaluations_dir22 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_1_2022-02-25 16:37:37.8291192022-02-25 16:37:37.829198'
			CCL_evaluations_dir23 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_2_2022-02-25 19:19:56.6678302022-02-25 19:19:56.667911'
			CCL_evaluations_dir24 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_3_2022-02-25 22:02:17.0399402022-02-25 22:02:17.040023'
			CCL_evaluations_dir25 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_4_2022-02-26 00:46:56.9317122022-02-26 00:46:56.931811'
					
			# alpha=0.0001
			CCL_evaluations_dir31 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_0_2022-02-25 13:43:29.2679492022-02-25 13:43:29.268035'
			CCL_evaluations_dir32 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_1_2022-02-25 16:37:29.9582002022-02-25 16:37:29.958281'
			CCL_evaluations_dir33 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_2_2022-02-25 19:19:52.7087622022-02-25 19:19:52.708855'
			CCL_evaluations_dir34 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_3_2022-02-25 22:02:24.9767592022-02-25 22:02:24.976871'
			CCL_evaluations_dir35 = results_dir + 'FetchSlide-v1_results/TD3CCL_PQD_FetchSlide-v1_4_2022-02-26 00:46:48.8000942022-02-26 00:46:48.800178'
			
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
		if is_4000:

			ExperttoTD3Fetch_evaluations_dir1 = results_dir + 'FetchSlide-v1_results/TD3_FetchSlide-v1_0_2022-02-27 13:37:41.1768132022-02-27 13:37:41.176899'
			ExperttoTD3Fetch_evaluations_dir2 = results_dir + 'FetchSlide-v1_results/TD3_FetchSlide-v1_1_2022-02-27 13:37:38.4446422022-02-27 13:37:38.445160'
			ExperttoTD3Fetch_evaluations_dir3 = results_dir + 'FetchSlide-v1_results/TD3_FetchSlide-v1_2_2022-02-27 13:37:42.2376532022-02-27 13:37:42.237808'
			ExperttoTD3Fetch_evaluations_dir4 = results_dir + 'FetchSlide-v1_results/TD3_FetchSlide-v1_3_2022-02-27 13:37:40.6054162022-02-27 13:37:40.605512'
			ExperttoTD3Fetch_evaluations_dir5 = results_dir + 'FetchSlide-v1_results/TD3_FetchSlide-v1_4_2022-02-27 13:37:40.7992212022-02-27 13:37:40.799335'
			
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
			# plt.xlim([-5000, 1000])

			ppo_max_drop = -10
			ppo_final_performance = 5


			# plt.ylim([4000, 11000])
			# plt.legend(loc='lower right')
			plt.title('Fetch Slide', fontsize=15)
			file_name = 'FetchSlide ExperttoTD3 Constraint Compare.png'

			# ####
			# COMMENT IN FOR PPO
			plt.scatter(ppo_max_drop, ppo_final_performance, color='tab:orange', marker='d',label='PPO')
			texts.append(plt.text(ppo_max_drop, ppo_final_performance, 'PPO', fontsize=14))
			Xs.append(ppo_max_drop)
			Ys.append(ppo_final_performance)
			# # ###

			plt.legend(fontsize=13,labelspacing=0.05)
			# plt.legend(loc='lower left', fontsize=13,labelspacing=0.05)
		else:
			ppo_max_drop=-2

			ppo_final_performance=10

			# plt.legend(loc='upper right', fontsize=13)
			plt.title('Fetch Slide', fontsize=15)
			# plt.legend(fontsize=15)
			file_name = 'FetchSlide ExperttoTD3 Constraint Compare.png'

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