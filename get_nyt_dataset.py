from json_decode import load_json_to_dict

def get_data():
	# Getting data from JSON
	abstracts_dict = load_json_to_dict("nyt_dataset/abstracts.json")
	fulltexts_split_dict = load_json_to_dict("nyt_dataset/sentence_tokens.json")
	data_splits = load_json_to_dict("nyt_dataset/data_splits.json")

	# Creating full texts dictionary
	fulltexts_dict = {}
	for key in fulltexts_split_dict:
		fulltexts_dict[key] = ' '.join(fulltexts_split_dict[key])

	# Create training set
	train_abstracts = {}
	train_fulltexts = {}
	for key in data_splits["train"]:
		train_abstracts[key] = abstracts_dict[key]
		train_fulltexts[key] = fulltexts_dict[key]

	# Index the article IDs
	count = 0
	indexed_ids = {}
	for key in train_abstracts:
		indexed_ids[count] = key
		count += 1

	return train_abstracts, train_fulltexts, indexed_ids
