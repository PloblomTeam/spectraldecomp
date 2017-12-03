from functions import *

def returnComponents():
	components = {
		"Starlight":[
			starlight,
			(0.5,0.0417),
			[[0.0,5.0],[0.04,0.043]]],
		"Power law continuum":[
			powerLaw,
			(1.60, -1.0),
			[[0.0,1e9],[-2.5,-0.5]]],
		"Fe II":[
			feII,
			(0.01,0.01,0.01,0.01,0.01,0.0417),
			[[0.0,10.0],[0.0,10.0],[0.0,10.0],[0.0,10.0],[0.0,10.0],[0.04,0.043]]],
		#"Constant offset":[
		#	offset,
		#	(0.,),
		#	[[-100.,100.],]],
		"He I 4922":[
			gauss,
			(2.,5127.,8.),
			[[0,10.],[5120,5135],[0.,50.]]],
		"He I 5016":[
			gauss,
			(2.,5225.,8.),
			[[0,10.],[5120,5135],[0.,50.]]],
		"Hbeta broad":[
			gaussHermite,
			(3.47867701e+00,5.06218249e+03,1.59043036e+01,7.97637947e+00,1.48117206e+00,3.10551023e+00,3.97014980e-01,3.40209679e+00),
			[[0.0,1e9],[-1e9,1e9],[-1e9,1e9],[-1e9,1e9],[-1e9,1e9],[-1e9,1e9],[-1e9,1e9],[-1e9,1e9]]],
		"Hbeta narrow":[
			gauss,
			(5.47071302e+00,5.06379950e+03,3.35876967e+00),
			[[0.0,1e9],[-1e9,1e9],[-1e9,1e9]]],
		"OIII Gaussian 1":[
			gauss,
			(1.13432618e+01,   5.16554166e+03,   4.41982618e+00),
			[[0.0,1e9],[-1e9,1e9],[-1e9,1e9]]],
		"OIII Gaussian 2":[
			gauss,
			(3.08712819e+01,5.21578755e+03,3.96952956e+00),
			[[0.0,1e9],[-1e9,1e9],[-1e9,1e9]]]
	}
	return components