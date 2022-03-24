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
			ExperttoTD3Hopper_evaluations_dir11 = results_dir + 'FetchPush-v1_results/TD3_BC_Pertubation_FetchPush-v1_0_2022-02-17 18:42:19.9051232022-02-17 18:42:19.905204'
			ExperttoTD3Hopper_evaluations_dir12 = results_dir + 'FetchPush-v1_results/TD3_BC_Pertubation_FetchPush-v1_0_2022-02-17 18:42:19.9051232022-02-17 18:42:19.905204'
			ExperttoTD3Hopper_evaluations_dir13 = results_dir + 'FetchPush-v1_results/TD3_BC_Pertubation_FetchPush-v1_0_2022-02-17 18:42:19.9051232022-02-17 18:42:19.905204'
			ExperttoTD3Hopper_evaluations_dir14 = results_dir + 'FetchPush-v1_results/TD3_BC_Pertubation_FetchPush-v1_0_2022-02-17 18:42:19.9051232022-02-17 18:42:19.905204'
			#alpha: 0.1
			ExperttoTD3Hopper_evaluations_dir21 = results_dir + 'FetchPush-v1_results/TD3_BC_Pertubation_FetchPush-v1_0_2022-02-17 18:42:20.3425702022-02-17 18:42:20.342673'
			ExperttoTD3Hopper_evaluations_dir22 = results_dir + 'FetchPush-v1_results/TD3_BC_Pertubation_FetchPush-v1_0_2022-02-17 18:42:20.3425702022-02-17 18:42:20.342673'
			ExperttoTD3Hopper_evaluations_dir23 = results_dir + 'FetchPush-v1_results/TD3_BC_Pertubation_FetchPush-v1_0_2022-02-17 18:42:20.3425702022-02-17 18:42:20.342673'
			ExperttoTD3Hopper_evaluations_dir24 = results_dir + 'FetchPush-v1_results/TD3_BC_Pertubation_FetchPush-v1_0_2022-02-17 18:42:20.3425702022-02-17 18:42:20.342673'
			#alpha: 0.2
			ExperttoTD3Hopper_evaluations_dir31 = results_dir + 'FetchPush-v1_results/TD3_BC_Pertubation_FetchPush-v1_0_2022-02-17 18:42:20.5415082022-02-17 18:42:20.541624'
			ExperttoTD3Hopper_evaluations_dir32 = results_dir + 'FetchPush-v1_results/TD3_BC_Pertubation_FetchPush-v1_0_2022-02-17 18:42:20.5415082022-02-17 18:42:20.541624'
			ExperttoTD3Hopper_evaluations_dir33 = results_dir + 'FetchPush-v1_results/TD3_BC_Pertubation_FetchPush-v1_0_2022-02-17 18:42:20.5415082022-02-17 18:42:20.541624'
			ExperttoTD3Hopper_evaluations_dir34 = results_dir + 'FetchPush-v1_results/TD3_BC_Pertubation_FetchPush-v1_0_2022-02-17 18:42:20.5415082022-02-17 18:42:20.541624'
			#alpha: 0.25
			ExperttoTD3Hopper_evaluations_dir41 = results_dir + 'FetchPush-v1_results/TD3_BC_Pertubation_FetchPush-v1_0_2022-02-17 18:42:20.0908012022-02-17 18:42:20.090938'
			ExperttoTD3Hopper_evaluations_dir42 = results_dir + 'FetchPush-v1_results/TD3_BC_Pertubation_FetchPush-v1_0_2022-02-17 18:42:20.0908012022-02-17 18:42:20.090938'
			ExperttoTD3Hopper_evaluations_dir43 = results_dir + 'FetchPush-v1_results/TD3_BC_Pertubation_FetchPush-v1_0_2022-02-17 18:42:20.0908012022-02-17 18:42:20.090938'
			ExperttoTD3Hopper_evaluations_dir44 = results_dir + 'FetchPush-v1_results/TD3_BC_Pertubation_FetchPush-v1_0_2022-02-17 18:42:20.0908012022-02-17 18:42:20.090938'
			#alpha: 1
			ExperttoTD3Hopper_evaluations_dir51 = results_dir + 'FetchPush-v1_results/TD3_BC_Pertubation_FetchPush-v1_0_2022-02-17 18:42:15.7924732022-02-17 18:42:15.792812'
			ExperttoTD3Hopper_evaluations_dir52 = results_dir + 'FetchPush-v1_results/TD3_BC_Pertubation_FetchPush-v1_0_2022-02-17 18:42:15.7924732022-02-17 18:42:15.792812'
			ExperttoTD3Hopper_evaluations_dir53 = results_dir + 'FetchPush-v1_results/TD3_BC_Pertubation_FetchPush-v1_0_2022-02-17 18:42:15.7924732022-02-17 18:42:15.792812'
			ExperttoTD3Hopper_evaluations_dir54 = results_dir + 'FetchPush-v1_results/TD3_BC_Pertubation_FetchPush-v1_0_2022-02-17 18:42:15.7924732022-02-17 18:42:15.792812'

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
			ExperttoTD3Hopper_evaluations_dir11 = results_dir + 'FetchPush-v1_results/TD3_BC_Constraint_FetchPush-v1_0_2022-02-17 18:44:15.2306662022-02-17 18:44:15.230777'
			ExperttoTD3Hopper_evaluations_dir12 = results_dir + 'FetchPush-v1_results/TD3_BC_Constraint_FetchPush-v1_0_2022-02-17 18:44:15.2306662022-02-17 18:44:15.230777'
			ExperttoTD3Hopper_evaluations_dir13 = results_dir + 'FetchPush-v1_results/TD3_BC_Constraint_FetchPush-v1_0_2022-02-17 18:44:15.2306662022-02-17 18:44:15.230777'
			ExperttoTD3Hopper_evaluations_dir14 = results_dir + 'FetchPush-v1_results/TD3_BC_Constraint_FetchPush-v1_0_2022-02-17 18:44:15.2306662022-02-17 18:44:15.230777'
			#alpha: 0.01
			ExperttoTD3Hopper_evaluations_dir21 = results_dir + 'FetchPush-v1_results/TD3_BC_Constraint_FetchPush-v1_0_2022-02-17 18:44:15.6908262022-02-17 18:44:15.690936'
			ExperttoTD3Hopper_evaluations_dir22 = results_dir + 'FetchPush-v1_results/TD3_BC_Constraint_FetchPush-v1_0_2022-02-17 18:44:15.6908262022-02-17 18:44:15.690936'
			ExperttoTD3Hopper_evaluations_dir23 = results_dir + 'FetchPush-v1_results/TD3_BC_Constraint_FetchPush-v1_0_2022-02-17 18:44:15.6908262022-02-17 18:44:15.690936'
			ExperttoTD3Hopper_evaluations_dir24 = results_dir + 'FetchPush-v1_results/TD3_BC_Constraint_FetchPush-v1_0_2022-02-17 18:44:15.6908262022-02-17 18:44:15.690936'
			#alpha: 0.1
			ExperttoTD3Hopper_evaluations_dir31 = results_dir + 'FetchPush-v1_results/TD3_BC_Constraint_FetchPush-v1_0_2022-02-17 18:44:15.3855152022-02-17 18:44:15.385608'
			ExperttoTD3Hopper_evaluations_dir32 = results_dir + 'FetchPush-v1_results/TD3_BC_Constraint_FetchPush-v1_0_2022-02-17 18:44:15.3855152022-02-17 18:44:15.385608'
			ExperttoTD3Hopper_evaluations_dir33 = results_dir + 'FetchPush-v1_results/TD3_BC_Constraint_FetchPush-v1_0_2022-02-17 18:44:15.3855152022-02-17 18:44:15.385608'
			ExperttoTD3Hopper_evaluations_dir34 = results_dir + 'FetchPush-v1_results/TD3_BC_Constraint_FetchPush-v1_0_2022-02-17 18:44:15.3855152022-02-17 18:44:15.385608'
			#alpha: 0.5
			ExperttoTD3Hopper_evaluations_dir41 = results_dir + 'FetchPush-v1_results/TD3_BC_Constraint_FetchPush-v1_0_2022-02-17 18:44:15.0483612022-02-17 18:44:15.048447'
			ExperttoTD3Hopper_evaluations_dir42 = results_dir + 'FetchPush-v1_results/TD3_BC_Constraint_FetchPush-v1_0_2022-02-17 18:44:15.0483612022-02-17 18:44:15.048447'
			ExperttoTD3Hopper_evaluations_dir43 = results_dir + 'FetchPush-v1_results/TD3_BC_Constraint_FetchPush-v1_0_2022-02-17 18:44:15.0483612022-02-17 18:44:15.048447'
			ExperttoTD3Hopper_evaluations_dir44 = results_dir + 'FetchPush-v1_results/TD3_BC_Constraint_FetchPush-v1_0_2022-02-17 18:44:15.0483612022-02-17 18:44:15.048447'
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
			ExperttoTD3Hopper_evaluations_dir11 = results_dir + 'FetchPush-v1_results/TD3_learning_rate_FetchPush-v1_1_2022-02-16 14:14:37.1975152022-02-16 14:14:37.197599'
			ExperttoTD3Hopper_evaluations_dir12 = results_dir + 'FetchPush-v1_results/TD3_learning_rate_FetchPush-v1_2_2022-02-16 17:10:24.9891012022-02-16 17:10:24.989224'
			ExperttoTD3Hopper_evaluations_dir13 = results_dir + 'FetchPush-v1_results/TD3_learning_rate_FetchPush-v1_3_2022-02-16 19:58:37.4241882022-02-16 19:58:37.424283'
			ExperttoTD3Hopper_evaluations_dir14 = results_dir + 'FetchPush-v1_results/TD3_learning_rate_FetchPush-v1_4_2022-02-16 22:51:55.2033892022-02-16 22:51:55.203473'
			#lr: 3e-6
			ExperttoTD3Hopper_evaluations_dir21 = results_dir + 'FetchPush-v1_results/TD3_learning_rate_FetchPush-v1_1_2022-02-16 14:14:37.0459112022-02-16 14:14:37.046003'
			ExperttoTD3Hopper_evaluations_dir22 = results_dir + 'FetchPush-v1_results/TD3_learning_rate_FetchPush-v1_2_2022-02-16 17:10:29.2232072022-02-16 17:10:29.223288'
			ExperttoTD3Hopper_evaluations_dir23 = results_dir + 'FetchPush-v1_results/TD3_learning_rate_FetchPush-v1_3_2022-02-16 19:58:32.5819652022-02-16 19:58:32.582077'
			ExperttoTD3Hopper_evaluations_dir24 = results_dir + 'FetchPush-v1_results/TD3_learning_rate_FetchPush-v1_4_2022-02-16 22:51:54.9551882022-02-16 22:51:54.955280'
			#lr: 3e-5
			ExperttoTD3Hopper_evaluations_dir31 = results_dir + 'FetchPush-v1_results/TD3_learning_rate_FetchPush-v1_1_2022-02-16 14:14:36.8254332022-02-16 14:14:36.825523'
			ExperttoTD3Hopper_evaluations_dir32 = results_dir + 'FetchPush-v1_results/TD3_learning_rate_FetchPush-v1_2_2022-02-16 17:10:29.4251792022-02-16 17:10:29.425285'
			ExperttoTD3Hopper_evaluations_dir33 = results_dir + 'FetchPush-v1_results/TD3_learning_rate_FetchPush-v1_3_2022-02-16 19:58:36.6006212022-02-16 19:58:36.600706'
			ExperttoTD3Hopper_evaluations_dir34 = results_dir + 'FetchPush-v1_results/TD3_learning_rate_FetchPush-v1_4_2022-02-16 22:51:54.7315832022-02-16 22:51:54.731671'
			#lr: 3e-4
			ExperttoTD3Hopper_evaluations_dir41 = results_dir + 'FetchPush-v1_results/TD3_learning_rate_FetchPush-v1_1_2022-02-16 14:14:32.4619122022-02-16 14:14:32.462163'
			ExperttoTD3Hopper_evaluations_dir42 = results_dir + 'FetchPush-v1_results/TD3_learning_rate_FetchPush-v1_2_2022-02-16 17:10:29.6530402022-02-16 17:10:29.653144'
			ExperttoTD3Hopper_evaluations_dir43 = results_dir + 'FetchPush-v1_results/TD3_learning_rate_FetchPush-v1_3_2022-02-16 19:58:36.7886042022-02-16 19:58:36.788698'
			ExperttoTD3Hopper_evaluations_dir44 = results_dir + 'FetchPush-v1_results/TD3_learning_rate_FetchPush-v1_4_2022-02-16 22:51:50.4871552022-02-16 22:51:50.487237'
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
			ExperttoTD3Hopper_evaluations_dir11 = results_dir + 'FetchPush-v1_results/TD3_gradient_clipping_FetchPush-v1_1_2022-02-15 22:19:48.3999442022-02-15 22:19:48.400041'
			ExperttoTD3Hopper_evaluations_dir12 = results_dir + 'FetchPush-v1_results/TD3_gradient_clipping_FetchPush-v1_2_2022-02-16 02:06:19.2929942022-02-16 02:06:19.293089'
			ExperttoTD3Hopper_evaluations_dir13 = results_dir + 'FetchPush-v1_results/TD3_gradient_clipping_FetchPush-v1_3_2022-02-16 05:52:06.0747152022-02-16 05:52:06.074804'
			ExperttoTD3Hopper_evaluations_dir14 = results_dir + 'FetchPush-v1_results/TD3_gradient_clipping_FetchPush-v1_4_2022-02-16 08:45:49.2245952022-02-16 08:45:49.224684'
			#gradient: 3e-8
			ExperttoTD3Hopper_evaluations_dir21 = results_dir + 'FetchPush-v1_results/TD3_gradient_clipping_FetchPush-v1_1_2022-02-15 22:19:48.6655882022-02-15 22:19:48.665724'
			ExperttoTD3Hopper_evaluations_dir22 = results_dir + 'FetchPush-v1_results/TD3_gradient_clipping_FetchPush-v1_2_2022-02-16 02:06:14.6907072022-02-16 02:06:14.690835'
			ExperttoTD3Hopper_evaluations_dir23 = results_dir + 'FetchPush-v1_results/TD3_gradient_clipping_FetchPush-v1_3_2022-02-16 05:52:01.7467892022-02-16 05:52:01.746869'
			ExperttoTD3Hopper_evaluations_dir24 = results_dir + 'FetchPush-v1_results/TD3_gradient_clipping_FetchPush-v1_4_2022-02-16 08:45:44.8587722022-02-16 08:45:44.858860'
			#gradient: 3e-6
			ExperttoTD3Hopper_evaluations_dir31 = results_dir + 'FetchPush-v1_results/TD3_gradient_clipping_FetchPush-v1_1_2022-02-15 22:19:48.2382422022-02-15 22:19:48.238329'
			ExperttoTD3Hopper_evaluations_dir32 = results_dir + 'FetchPush-v1_results/TD3_gradient_clipping_FetchPush-v1_2_2022-02-16 02:06:19.1250132022-02-16 02:06:19.125352'
			ExperttoTD3Hopper_evaluations_dir33 = results_dir + 'FetchPush-v1_results/TD3_gradient_clipping_FetchPush-v1_3_2022-02-16 05:52:05.9042282022-02-16 05:52:05.904337'
			ExperttoTD3Hopper_evaluations_dir34 = results_dir + 'FetchPush-v1_results/TD3_gradient_clipping_FetchPush-v1_4_2022-02-16 08:45:49.3807412022-02-16 08:45:49.380829'
			#gradient: 3e-3
			ExperttoTD3Hopper_evaluations_dir41 = results_dir + 'FetchPush-v1_results/TD3_gradient_clipping_FetchPush-v1_1_2022-02-15 22:19:44.0052622022-02-15 22:19:44.005744'
			ExperttoTD3Hopper_evaluations_dir42 = results_dir + 'FetchPush-v1_results/TD3_gradient_clipping_FetchPush-v1_2_2022-02-16 02:06:18.9244542022-02-16 02:06:18.924559'
			ExperttoTD3Hopper_evaluations_dir43 = results_dir + 'FetchPush-v1_results/TD3_gradient_clipping_FetchPush-v1_3_2022-02-16 05:52:06.4307432022-02-16 05:52:06.430841'
			ExperttoTD3Hopper_evaluations_dir44 = results_dir + 'FetchPush-v1_results/TD3_gradient_clipping_FetchPush-v1_4_2022-02-16 08:45:49.0757442022-02-16 08:45:49.076010'
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
			CCL_evaluations_dir11 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_0_2022-02-15 22:02:25.9402272022-02-15 22:02:25.940467'
			CCL_evaluations_dir12 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_1_2022-02-16 01:23:50.4597002022-02-16 01:23:50.459793'
			CCL_evaluations_dir13 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_2_2022-02-16 04:46:22.3117432022-02-16 04:46:22.311840'
			CCL_evaluations_dir14 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_3_2022-02-16 08:04:07.4408542022-02-16 08:04:07.441288'
			CCL_evaluations_dir15 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_4_2022-02-16 11:26:37.2449252022-02-16 11:26:37.245029'		
			
			# alpha=0.001
			CCL_evaluations_dir21 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_0_2022-02-15 22:02:29.9934402022-02-15 22:02:29.993525'
			CCL_evaluations_dir22 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_1_2022-02-16 01:23:46.3490712022-02-16 01:23:46.349185'
			CCL_evaluations_dir23 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_2_2022-02-16 04:46:18.1847532022-02-16 04:46:18.184888'
			CCL_evaluations_dir24 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_3_2022-02-16 08:04:11.3784132022-02-16 08:04:11.378517'
			CCL_evaluations_dir25 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_4_2022-02-16 11:26:32.9627592022-02-16 11:26:32.963018'

			# alpha=0.0001
			CCL_evaluations_dir31 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_0_2022-02-15 22:02:30.1508222022-02-15 22:02:30.150915'
			CCL_evaluations_dir32 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_1_2022-02-16 01:23:50.6473152022-02-16 01:23:50.647408'
			CCL_evaluations_dir33 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_2_2022-02-16 04:46:22.4742092022-02-16 04:46:22.474305'
			CCL_evaluations_dir34 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_3_2022-02-16 08:04:11.5692702022-02-16 08:04:11.569370'
			CCL_evaluations_dir35 = results_dir + 'FetchPush-v1_results/TD3CCL_PQD_FetchPush-v1_4_2022-02-16 11:26:37.0066002022-02-16 11:26:37.006981'
				

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
			ExperttoTD3Fetch_evaluations_dir1 = results_dir + 'FetchPush-v1_results/TD3_FetchPush-v1_0_2022-02-15 22:03:53.3557772022-02-15 22:03:53.355863'
			ExperttoTD3Fetch_evaluations_dir2 = results_dir + 'FetchPush-v1_results/TD3_FetchPush-v1_1_2022-02-16 01:09:08.5588012022-02-16 01:09:08.558902'
			ExperttoTD3Fetch_evaluations_dir3 = results_dir + 'FetchPush-v1_results/TD3_FetchPush-v1_2_2022-02-16 04:20:47.6671742022-02-16 04:20:47.667272'
			ExperttoTD3Fetch_evaluations_dir4 = results_dir + 'FetchPush-v1_results/TD3_FetchPush-v1_3_2022-02-16 07:26:59.2407832022-02-16 07:26:59.240877'
			ExperttoTD3Fetch_evaluations_dir5 = results_dir + 'FetchPush-v1_results/TD3_FetchPush-v1_4_2022-02-16 10:23:05.6956892022-02-16 10:23:05.695777'
			
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

			ppo_max_drop = -5
			ppo_final_performance = 60


			# plt.ylim([4000, 11000])
			# plt.legend(loc='lower right')
			plt.title('Fetch Push', fontsize=15)
			file_name = 'FetchPush ExperttoTD3 Constraint Compare.png'

			# ####
			#COMMENT BACK IN FOR PPO
			plt.scatter(ppo_max_drop, ppo_final_performance, color='tab:orange', marker='d',label='PPO')
			texts.append(plt.text(ppo_max_drop, ppo_final_performance, 'PPO', fontsize=14))
			Xs.append(ppo_max_drop)
			Ys.append(ppo_final_performance)
			# # ###
			plt.legend(loc='lower right',fontsize=13, ncol=2,columnspacing=0.2,labelspacing=0.05, handletextpad=0.2)
			# plt.legend(fontsize=13,labelspacing=0.05)
			# plt.legend(loc='lower left', fontsize=13,labelspacing=0.05)
		else:
			ppo_max_drop=-1667.9042914598458

			ppo_final_performance=10200.48596471069

			# plt.legend(loc='upper right', fontsize=13)
			plt.title('FetchPush Constraints Comparison', fontsize=15)
			# plt.legend(fontsize=15)
			file_name = 'FetchPush ExperttoTD3 Constraint Compare.png'

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