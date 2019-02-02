from rouge import Rouge
import glob

BASE_DIR = "./logs/pretrained_model_tf1.2.1/decode_val_400maxenc_4beam_35mindec_100maxdec_ckpt-238518/"

rouge = Rouge()

generated_abs = []
actual_abs = []

generated_files = sorted(glob.glob(BASE_DIR + "decoded/*.txt"))
for name in generated_files:
	with open(name) as f:
		data = f.read().replace('\n', '')
		generated_abs.append(data)

actual_files = sorted(glob.glob(BASE_DIR + "reference/*.txt"))
for name in actual_files:
	with open(name) as f:
		data = f.read().replace('\n', '')
		actual_abs.append(data)

num_docs_using = len(generated_abs)

val_rouge_f = {'rouge-1': 0,'rouge-2': 0,'rouge-l': 0}
val_rouge_p = {'rouge-1': 0,'rouge-2': 0,'rouge-l': 0}
val_rouge_r = {'rouge-1': 0,'rouge-2': 0,'rouge-l': 0}

for i in range(num_docs_using):
	generated = generated_abs[i]
	reference = actual_abs[i]
	rouge_scores = rouge.get_scores(generated, reference)[0]
	for r in ['rouge-1','rouge-2','rouge-l']:
		val_rouge_f[r] += rouge_scores[r]['f']
		val_rouge_p[r] += rouge_scores[r]['p']
		val_rouge_r[r] += rouge_scores[r]['r']

for i in val_rouge_f:
	val_rouge_f[i] /= num_docs_using
	val_rouge_p[i] /= num_docs_using
	val_rouge_r[i] /= num_docs_using
	val_rouge_f[i] *= 100
	val_rouge_p[i] *= 100
	val_rouge_r[i] *= 100

print("Precision:", val_rouge_p)
print("Recall:", val_rouge_r)
print("F score:", val_rouge_f)

length = 0
for i in range(num_docs_using):
	generated = generated_abs[i].split(" ")
	length += len(generated)
length /= num_docs_using
print(length)
