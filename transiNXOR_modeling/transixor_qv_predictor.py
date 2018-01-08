import sys
sys.path.append('../')
import numpy as np
from itertools import product
from ac_qv_api import predict_qs
import matplotlib.pyplot as plt
import glob

# vds = np.linspace(0, 0.4, 41)
vds = np.linspace(0.4, 0.4, 1)
# vbg = np.linspace(0, 0.4, 41)
vbg = np.linspace(0.0, 0.0, 1)
vtg = np.linspace(0.0, 0.4, 67)
iter_lst = list(product(vds, vbg, vtg))
vds_pred = np.array([e[0] for e in iter_lst], dtype=np.float32)
vbg_pred = np.array([e[1] for e in iter_lst], dtype=np.float32)
vtg_pred = np.array([e[2] for e in iter_lst], dtype=np.float32)
vss_pred = np.zeros_like(vtg_pred)
v_pred = np.column_stack((vds_pred, vbg_pred, vtg_pred, vss_pred))

# terminal_list = ['b', 'd', 'g', 's']
terminal_list = ['b']
for term in terminal_list:
	## ------------  True data  ---------------
	# cv_files = glob.glob('./transiXOR_data/*_C'+term+'?_*')
	# capa_data = [np.expand_dims(
	# 	np.load(f).flatten(), axis=1).astype(np.float32) for f in cv_files]
	# vds, vbg, vtg, C

	## ------------  Prediction ---------------
	q_pred, grads_pred = predict_qs(
		'./transiXOR_QV_Models/model_'+term+'_0', v_pred)
	print(q_pred.shape, grads_pred.shape)
