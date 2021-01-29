import time
import datetime
from yarkovsky import Yarkovsky
start = time.time()

for i in range(1, 11):
	print('Making Yarkovsky object scale: {}'.format(i))
	yarkovsky_obj=Yarkovsky(i)
	print('Running yarkovskyforce function')
	vector_answer=yarkovsky_obj.yarkovskyforce()
	torque_answer = yarkovsky_obj.yorptorque()
	def save_yark_vector(np_vec, np_vec2):
		with open('final_yark_vector.txt', 'w') as f:
			f.write("Yarkovsky vector:\n")
			for item in list(np_vec):
				f.write("%s\n" % item)
			f.write("\n")
			f.write("YORP vector:\n")
			for item in list(np_vec2):
				f.write("%s\n" % item)
	print()
	print("====================================================")
	print("Vector answer: {}".format(vector_answer))
	print("====================================================")
	print("Torque answer: {}".format(torque_answer))
	print("====================================================")
	# save_yark_vector(vector_answer, torque_answer)

end = time.time()
print("Runtime: " + str(datetime.timedelta(seconds=end-start)))